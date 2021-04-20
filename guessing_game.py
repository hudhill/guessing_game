correct_guess = 4

guess = input("Guess a number:")

while True:

  if int(guess) == correct_guess:
    print("Correct!")
    break
  else:
    print("Try again")
    
  guess = input("Guess a number:")