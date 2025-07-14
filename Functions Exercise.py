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

#4. Function That Returns a Value

def multiply(a, b):
    return a * b

product = multiply(6, 7)
print("Product is:", product)

#Create a function `divide(a, b)` that returns the result

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Division result:", divide(10, 2))
print("Division result (zero):", divide(10, 0))

#5. Function with Default Parameters

def greet_city(name, city="Vancouver"):
    print(f"{name} lives in {city}")

greet_city("Ankita")
greet_city("Rose", "Toronto")

#Create a function `introduce(name, age=25)` that prints: "My name is ___ and I am ___ years old."

def introduce(name, age=25):
    print(f"My name is {name} and I am {age} years old.")

introduce("Subir")
introduce("Tanni", 18)
