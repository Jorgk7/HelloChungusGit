# Python Interpreter executes the code line to line from the top

# Dictionaries - Can be anything, but you cannot repeat a key, also case-Sensitive
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# customer["name"] = "Jack Smith" - don't do this just change the value in the main object it just make your code messy
# print(customer["name"]) - Returns an error if such key doesnt exist/ misspell
print(customer.get("birthday", "Jan 4 1975"))
# ^ Get removes the error and just returns none, you can also add a value to that non-existent key so it returns
# ^^ that value, pretty much create a new key
