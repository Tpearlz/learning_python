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







