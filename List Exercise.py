#1 Create a List
fruits = ["apple","banana","cherry","mango"]
print("Initial List;", fruits)

#Add "orange" to the list and print the updated list
fruits.append("orange")
print("After adding 'orange':",fruits)

#2. Accessing List Elements
print("First fruit:", fruits[0])
# index starts at 0
print("Last fruit:", fruits[-1])
# negative index starts from end

# Print the second and third fruits using slicing
print("Second and third fruits:", fruits[1:3])

#3. Modifying Elements
fruits[1] = "blueberry"
# Changing banana to blueberry
print("After modification:", fruits)

#Change "cherry" to "pineapple"
index_cherry = fruits.index("cherry")
fruits[index_cherry] = "pineapple"
print("After changing 'cherry' to 'pineapple':", fruits)

#5. Removing Items
fruits.remove("apple")        # Removes first occurrence of "apple"
popped_fruit = fruits.pop()    # Removes first occurrence of "apple"
print("After removing 'apple' and popping last item:", fruits)
print("Popped fruit:", popped_fruit)

# ✅ Task 5: Remove "mango" and print the list
fruits.remove("mango")
print("After removing 'mango':", fruits)

#6. Sorting and Reversing
fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)

# Sort in reverse alphabetical order without changing original list
sorted_reversed = sorted(fruits, reverse=True)
print("Reverse-sorted (new list):", sorted_reversed)
print("Original list remains:", fruits)

#7. Iterating Over a List
print("Fruits one by one:")
for fruit in fruits:
    print("Fruit:", fruit)

# Print each fruit in uppercase
print("Fruits in uppercase:")
for fruit in fruits:
    print(fruit.upper())

#8. List Comprehension
fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of each fruit name:", fruit_lengths)

# New list with fruits containing the letter 'e'
fruits_with_e = [fruit for fruit in fruits if 'e' in fruit]
print("Fruits with 'e':", fruits_with_e)

#Given a list of prices, write a function to apply a discount
prices = [20, 30, 50, 100, 80]

def discount_prices(prices, discount):
    """Apply a discount % to each price and return a new list."""
    discounted = [round(price * (1 - discount/100), 2) for price in prices]
    return discounted

# Test the function
discounted_10 = discount_prices(prices, 10)
print("Original prices:", prices)
print("Prices after 10% discount:", discounted_10)

# Try changing the discount to 25% and print again
discounted_25 = discount_prices(prices, 25)
print("Prices after 25% discount:", discounted_25)










