# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import re

with open("./Input/Names/invited_names.txt") as file:
    names = [i.strip() for i in file.readlines()]
# with open("../")

with open("./Input/Letters/starting_letter.txt")as letter:
    letter_1 = letter.read()

for name in names:
    # using regex or using string replace method
    ready_letter = re.sub(r"\[\w*\]",name, letter_1)
    ready_letter = letter_1.replace("[name]", name)
    with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(ready_letter)
