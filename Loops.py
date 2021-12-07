# Python Interpreter executes the code line to line from the top

# While Loops

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You guessed the secret number!')
        break
else:
    print('You failed, try again!')

# For Loops

for item in range(5, 10, 2):
    print(item)

# Nested Loop ( Adding a loop in a loop )

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
