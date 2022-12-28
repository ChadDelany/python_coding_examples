# Tip Calculator

print('Welcome to the tip calculator.')
bill = float(input('What is the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, 15, or 20? '))
people = int(input('How many people to split the bill?'))
tip_percent = tip / 100
total_bill = bill * (1 + tip_percent)
bill_per_person = total_bill / people
print(f'The total bill per person is: ${bill_per_person: .2f}')