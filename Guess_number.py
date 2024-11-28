import random

number_to_guess = random.randint(1, 100)

while True:
  try:
    guess = int(input('Guess a number between 1 to 100: '))
    if guess < number_to_guess:
      print('Too low!')
    elif guess >number_to_guess:
      print('Too hight!')
    else:
      print(f'Yay you won the corrent number was {number_to_guess}')
  except ValueError:
    print('Pleace enter a valid number!')
    break

