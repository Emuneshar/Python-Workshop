import os

print("*+*+*+*+*+*+*+*+*+*+*+*+*\n")
g = "Welcome to Hangman"
g.center(200)
print(g)
print("Rules!\n")
print("1. One Player will enter a secret word and a hint")
print("2. The second player will guess a letter or the complete word")
print("3. To use your hint, enter the word 'hint!'")
print("*+*+*+*+*+*+*+*+*+*+*+*+*\n")


goodLetters = []
badLetters = []

secretWord = input("Please enter the secret word\n")
hint = input("What is the hint for our secret word?\n")
os.system('clear')


while True:
  guess = input("Please guess a letter\n")

  if guess == "hint!":
    print("The hint is", hint)
    continue

  if guess in goodLetters:
    print("You've already guessed that letter and it was correct!")

  elif guess in badLetters:
    print("You've already guessed that letter and it was wrong")

  if guess in secretWord:
    print("That letter is correct! Good job!")
    goodLetters.append(guess)

  if guess not in secretWord:
    

  

