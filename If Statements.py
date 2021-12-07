# Python Interpreter executes the code line to line from the top

# If Statements
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
# Logical Operators
# AND = Both need to be True
# OR: One has to be true
# NOT: Inverses boolean value
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income or has_good_credit:
    print("eligible for loan")

if has_good_credit and not has_criminal_record:
    print("eligible for loan too")

temperature = 30

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
