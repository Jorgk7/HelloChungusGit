# # Python Interpreter executes the code line to line from the top
#
# # Exercise
# # Define 3 valuables: We check in a patient named John Smith. He's 20 years old and is a new patient
# name = 'John Smith'
# age = 20
# is_new_patient = True
# print(name, age, is_new_patient)
#
# # Exercise
# # Ask two questions: Persons name and favourite color, then print a message like: Jorge likes red
# name = input('Cual es tu nombre? ')
# color = input('Cual es tu color favorito? ')
# print(' el color favorito de ' + name + ' es ' + color)
#
# # Exercise
# # Ask a user their weight (in pounds), convert it to kilograms and print it on the terminal
# lbs = input('Your Weight in lbs?: ')
# kg = int(lbs) * 0.45
# print(kg)
#
# # Exercise
# # Make an if statement with these rules: Price of a house is $1M, If buyer has good credit, they need to put down 10%,
# # otherwise they need to put 20%, and then print the down payment
# is_good_credit = False  # has_good_credit = False
# # price = 1000000
#
# if is_good_credit:  # if has_good_credit
#     print(1000000 * 0.10)  # down_payment = 0.1 * price
# else:
#     print(1000000 * 0.20)  # down_payment = 0.2 * price
# # print("housing")/print(f"Down Payment: ${down_payment}")
#
# # Exercise
# # Make an if statement with these rules: If name is less than 3 characters return: name must be at least 3
# # characters long otherwise if its more than 50 characters long return: name can be a maximum of 50 characters
# # otherwise return: name looks good!
#
# name = input("What is your name? ")
#
# if len(name) < 3:
#     error = f"{name} is too short, name must be at least 3 characters long"
#     print(error)
# elif len(name) > 25:
#     error = f"{name} is too long, names can be a maximum of 25 characters"
#     print(error)
# else:
#     print("Name looking good!")
#
# # Exercise
# # Make a weight converter program, if they enter their weight in KG convert it to LBS
# w = input('Peso: ')
# KG_LBS = input("(K) Kilogramos o (L) Libras: ")
#
# if KG_LBS == "k" or KG_LBS == "K":
#     KG = int(w) / 0.45
#     print(f'Tu peso en libras es: {int(KG)} L')
# elif KG_LBS == "l" or KG_LBS == "L":
#     LBS = int(w) * 0.45
#     print(f'Tu peso en Kilos: {int(LBS)} KG')
# else:
#     print('Debes especificar si es KG o LBS')
#
# # Exercise
# # Build the car game using While Loops.
# command = ""
# on = 1
# off = -1
# while True:
#     command = input("> ")
#     if command == "start":
#         off = -1
#         on += 1
#         print('Checking car...')
#         if on == 2:
#             print("Car Started")
#         elif on >= 3:
#             print("Car Already Started")
#     elif command == "stop":
#         on = 1
#         off += 2
#         print('Checking car...')
#         if off == 1:
#             off += 1
#             print("Car Stopped")
#         elif off >= 2:
#             print("Checking car is off...")
#             print("Car already stopped")
#     elif command == "help":
#         print('''
# start - start the car
# stop - stop the car
# quit - quit the game''')
#     elif command == "quit":
#         break
#     else:
#         print("i don't understand that")
#
# # Exercise
# # Use for loops to calculate the total cost of all the items in your imaginary shopping cart
# prices = [10, 20, 30]
#
# suma = 0
# for item in prices:
#     suma += item
# print(f'Total: {suma}')
#
# # Challenge
# # Make a F with x's using nested loops
# numbers = [5, 2, 5, 2, 2]
#
# for x_output in numbers:
#     output = ''
#     for number_output in range(x_output):
#         output += 'x'
#     print(output)

# Exercise
#  Make a program that finds the largest number in a list
# numbers2 = [1, 2, 50]
# max = numbers2[0]
# for number in numbers2:
#     if number > max:
#         max = number
# print(max)
# print(max(numbers2))

# Exercise
# Make a program that removes the duplicates in a list
numbers3 = [1, 1, 5, 4, 3, 3, 6]
uniques = [5, 6, 4]
for number in numbers3:
    if number not in uniques:
        numbers3.append(numbers3)
print(uniques)
