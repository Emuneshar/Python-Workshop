import os

def wordChecker(SW, goodLetters):
  for x in SW:
    if x not in goodLetters:
      return False






print("*+*+*+*+*+*+*+*+*+*+*+*+*\n")
g = "Welcome to Hangman"
g.center(200)
print(g)
print("Rules!\n")
print("1. One Player will enter a secret word and a hint")
print("2. The second player will guess a letter or the complete word")
print("3. To use your hint, enter the word 'hint!'")
print("*+*+*+*+*+*+*+*+*+*+*+*+*\n")

lives = 10
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
    print("That letter is wrong")
    lives = lives - 1
    badLetters.append(guess)
    print("You  have", lives, "lives left")

  if guess == secretWord:
    print("You guessed the secret word correctly! You Win!")
  else:
    print("You guessed that incorrectly")
    lives = lives -1 
    print("You  have", lives, "lives left")


  if wordChecker(secretWord, goodLetters)
    

  

