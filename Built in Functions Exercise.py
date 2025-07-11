# 1. len() - Get the length of a list, string, or other iterable
fruits = ["apple", "banana", "cherry"]
print("Length of the list:", len(fruits))

# Print the length of the word "Analytics"
word = "Analytics"
print("Length of 'Analytics':", len(word))

#2. sum() - Sum of all elements in a list
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Sum of numbers:", total)

# Use sum() to find the total of [5, 15, 25, 35]
print("Sum of [5, 15, 25, 35]:", sum([5, 15, 25, 35]))

#3. max() and min() - Find the largest and smallest values
print("Max number:", max(numbers))
print("Min number:", min(numbers))

# Use max() to find the highest fruit name alphabetically
print("Alphabetically highest fruit:", max(fruits))

#4. sorted() - Returns a sorted copy (does NOT change original list)
sorted_fruits = sorted(fruits)
print("Sorted fruits:", sorted_fruits)
print("Original fruits list remains:", fruits)

# Sort the fruits in reverse alphabetical order
print("Reverse sorted fruits:", sorted(fruits, reverse=True))

#5 type() - Find the data type of a variable
x = 100
print("Type of x:", type(x))

y = [1, 2, 3]
print("Type of y:", type(y))

# Print the type of "Hello" and 3.14
print("Type of 'Hello':", type("Hello"))
print("Type of 3.14:", type(3.14))



