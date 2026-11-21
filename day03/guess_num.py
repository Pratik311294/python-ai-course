import random
secret = random.randint(1, 10)
attempts = 0
max_attempts = 4
win=False

print('I have a secret number between 1 and 10. Can you guess it?')
while attempts < max_attempts:
    guess = int(input('Enter your guess:'))
    attempts+=1
    if guess == secret :
        print(f'you got it in {attempts} attempts!')
        win = True
        break
    elif guess < secret:
        print('you are below the secret number')
    else:
        print('you are above the secret number')
if not win:
    print(f'Sorry, you have used all your attempts. The secret number was {secret}.')