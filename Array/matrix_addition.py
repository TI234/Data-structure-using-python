# initializing Array for matrices
matrix1 = [] # i
matrix2 = []
result = []

# Taking user input for first matrix:

row = int(input("Enter the no. of row:"))
column = int(input("Emter the no. of column:"))
print("Enter the elements for the first Matrix:")
for i in range (row):
	matrix1.append([0]*column) # Creating one row Like This [[0,0,0]] 
	for j in range (column):
		matrix1[i][j] = int(input("Enter the Element for [{0}][{1}] position:".format(i,j)))
print("------------------------------------------")

# Taking user input for second matrix:
print("Enter the elements for the second Matrix:")
for i in range (row):
	matrix2.append([0]*column)
	for j in range (column):
		matrix2[i][j] = int(input("Enter the Element for [{0}][{1}] position:".format(i,j)))

# Creating result matrix:

for i in range (row):
	result.append([0]*column)
	for j in range (column):
		result[i][j] = 0

# Logic for 2 Matrix Addition:

for i in range (row):
	for j in range (column):
		result[i][j] = matrix1[i][j] + matrix2[i][j] # Adding element and store in re
print("matrix1:\n\t",matrix1) # Print first Matrix
print("matrix2:\n\t",matrix2) # Print Second Matrix
print("Result matrix:\n\t",result) # Print result Matrix