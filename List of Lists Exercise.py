#1. Creating a List of Lists (2D List)
# Let's say we have student scores for 3 students in 3 subjects
scores = [
    [85, 92, 78],   # Student 1
    [76, 88, 90],   # Student 2
    [90, 91, 95]    # Student 3
]
print("Initial scores:", scores)

#2. Accessing Elements
print("Score of Student 1 in Subject 2:", scores[0][1])  # 92

#Print score of Student 3 in Subject 3
print("Student 3, Subject 3:", scores[2][2])

#3. Iterating through a List of Lists
print("All scores row by row:")
for student_scores in scores:
    print(student_scores)

# Print each individual score in a tabular format
print("Individual scores:")
for i, student_scores in enumerate(scores):
    for j, score in enumerate(student_scores):
        print(f"Student {i+1}, Subject {j+1}: {score}")

#4. Adding a New Student's Scores
scores.append([88, 79, 85])
print("After adding Student 4:", scores)

# Add another student with scores [70, 80, 90]
scores.append([70, 80, 90])
print("After adding Student 5:", scores)

#5. Updating a Value
# Let's update Student 2's score in Subject 1 to 95
scores[1][0] = 95
print("After updating Student 2's Subject 1 score:", scores)

# Change Student 5's Subject 2 score to 82
scores[4][1] = 82
print("After updating Student 5's Subject 2 score:", scores)

