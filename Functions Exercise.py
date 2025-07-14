#1. Creating Your First Function

def greet():
    print("Hello! Welcome to Python functions.")

# Call the function
greet()

# Create a function named `welcome_user` that prints "Welcome to ACA!"
def welcome_user():
    print("Welcome to ACA!")
#2. Function with Parameters

def greet_user(name):
    print(f"Hello, {name}! Great to see you.")

# Call the function with an argument
greet_user("Tolu")

# Call `greet_user()` with your own name
greet_user("Tolu")

#3. Function with Multiple Parameters

def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(10, 5)

#Modify `add_numbers` to subtract numbers instead

def subtract_numbers(a, b):
    result = a - b
    print(f"The difference between {a} and {b} is {result}")

subtract_numbers(20, 7)

