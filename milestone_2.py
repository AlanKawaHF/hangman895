import random
word_list = ["Apple", "Strawberry", "Pineapple", "Grape", "Orange"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")
print(f"You have entered: {guess}")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    "Oops! That is not a valid input."
