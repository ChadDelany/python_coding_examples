# by Joel Grus
# https://twitter.com/joelgrus/status/1608137058492489729?s=20&t=tsUSmwKj-CPZCfBwCbDs2w
# https://gist.github.com/joelgrus/fb5708e7e9f9fc0a7f15369008dae30c

from typing import TypeVar, Generic, Callable
from dataclasses import dataclass
from argparse import Namespace

T = TypeVar('T')
S = TypeVar('S')


@dataclass
class ListMap(Generic[S, T]):
    f: Callable[[T], S]

    def __rrshift__(self, other: list[T]) -> list[S]:
        return [self.f(x) for x in other]


@dataclass
class ListFilter(Generic[S]):
    f: Callable[[T], bool]

    def __rrshift__(self, other: list[T]) -> list[T]:
        return [x for x in other if self.f(x)]


@dataclass
class ListFlatten(Generic[S]):
    def __rrshift__(self, other: list[list[S]]) -> list[S]:
        return [x for xs in other for x in xs]


@dataclass
class ListFlatMap(Generic[S, T]):
    f: Callable[[T], list[S]]

    def __rrshift__(self, other: list[T]) -> list[S]:
        return [y for x in other for y in self.f(x)]


List = Namespace(
    map=ListMap,
    filter=ListFilter,
    flatten=ListFlatten,
    flatmap=ListFlatMap,
)

if __name__ == "__main__":
    xs = [1, 2, 3, 4, 5]

    ys = (
            xs
            >> List.map(lambda x: x * 2)  # should be 2, 4, 6, 8, 10
            >> List.filter(lambda x: x > 5)  # should be 6, 8, 10
            >> List.flatmap(lambda x: [x, x])  # should be 6, 6, 8, 8, 10, 10
    )

    assert ys == [6, 6, 8, 8, 10, 10]