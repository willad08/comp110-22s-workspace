"""chardle exercise"""

__author__ = "730229417"


word: str = input("Enter a 5-character word:")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character:")
if len(letter) > 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + letter + " in " + word)
if letter == word[0]:
    print(letter + " found at index 0")
if letter == word[1]:
    print(letter + " found at index 1")
if letter == word[2]:
    print(letter + " found at index 2")
if letter == word[3]:
    print(letter + " found at index 3")
if letter == word[4]:
    print(letter + " found at index 4") 

count: int = 0
if letter in word:
    count = count + 1
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        if count == 2:
            print("2 instances of " + letter + " found in " + word)
        if count == 3:
            print("3 instances of " + letter + " found in " + word)
        if count == 4: 
            print("4 instances of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)        
