# In this modified version, we have a matrix called grades_matrix consisting
# of nested lists representing the grades of each student. We use a loop to
# iterate through each row of the matrix and calculate the average using the
# calculate_average function. The averages are stored in
# the averages list.

# A matrix of students' grades was created, where each row represents a student,
# and each column represents a respective student's grade. Note that we refer to
# this matrix as 'students' because this variable references a list where each item
# is a list of grades for a student."


# After calculating the averages for each row, we calculate the overall average
# of the matrix by summing all the averages and dividing by the number of rows.
# Finally, we display the average of each row and the overall average of the matrix.



def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

# Matrix of student grades
grades_matrix = [
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.5, 8.5, 7.0],
    [8.0, 7.0, 9.5, 8.5],
    [7.5, 9.0, 8.0, 7.0]
]

# Looping through the matrix to calculate averages
averages = []
for row in grades_matrix:
    average = calculate_average(row)
    averages.append(average)

# Calculation of the overall average of the matrix
overall_average = sum(averages) / len(averages)

# Displaying the results
print("Averages of each row:")
for i, average in enumerate(averages, 1):
    print(f"Average of row {i}: {average}")

print("Overall average of the matrix:", overall_average)
