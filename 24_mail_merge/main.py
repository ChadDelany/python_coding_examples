"""Mail Merge for Letter"""

# Constants
PLACEHOLDER = '[name]'

# Read the names file
with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

# Read in the form letter
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()

    # Format list of names
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Write individual letters with replaced names
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
            