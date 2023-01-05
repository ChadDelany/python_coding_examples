# Higher Lower Game
from random import sample, randint
from art_higher_lower import logo
from data_higher_lower import data

print(logo)
# print(len(data))
# print(sample(range(len(data)), k=2))
# print(data[[sample(range(len(data)), k=2)]])

# select = sample(range(len(data)), k=2)
# account0 = data[select[0]]
# account1 = data[select[1]]
# print([account0, account1])


def select(previous=0):
    if previous == 0:
        # Select two accounts that are different
        select = sample(range(len(data)), k=2)
        account0 = data[select[0]]
        account1 = data[select[1]]
        return [account0, account1]
    else:
        # Select one new account
        select = data[previous]
        while select == data[previous]:
            select = randint(range(len(data)))
        account1 = data[select]
        return [previous, account1]
def compare():
    return

def game():
    return