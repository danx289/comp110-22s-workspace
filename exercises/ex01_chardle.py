"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730479873"

given_word: str = input("Enter a 5-character word: ")
if len(given_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
given_letter: str = input("Enter a single character: ")
if len(given_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + given_letter + " in " + given_word)

count: int=0

if given_letter == given_word[0]:
    print(given_letter + " found at index 0")
    count+=1
if given_letter == given_word[1]:
    print(given_letter + " found at index 1")
    count+=1
if given_letter == given_word[2]:
    print(given_letter + " found at index 2")
    count+=1
if given_letter == given_word[3]:
    print(given_letter + " found at index 3")
    count+=1
if given_letter == given_word[4]:
    print(given_letter + " found at index 4")
    count+=1

if count == 0:
    print("No instances of " + given_letter + " found in " + given_word)
if count == 1:
    print("1 instance of " + given_letter + " found in " + given_word)
else: 
    print(str(count) + "instances of "+ given_letter + " found in " + given_word)

