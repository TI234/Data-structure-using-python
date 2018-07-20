# Multiplication of two matrix

# Taking input for first matrix

row1 = int(input("Enter the no. of row for MATRIX1:"))
column1 = int(input("Enter the no. of column for MATRIX1:"))
Matrix1 = []
Matrix2 = []
Result = []
print("Enter the elements for the first Matrix:")
for i in range (row1):
	Matrix1.append([0]*column1)# Creating one row Like This [[0,0,0]]
	for j in range (column1):
		Matrix1[i][j] = int(input("Enter the element for Matrix1:"))
print("-------------------------------")

# Taking input for second matrix
print("Enter the elements for the first Matrix:")
row2 = column1
column2 = row1
for i in range (row2):
	Matrix2.append([0]*column2)
	for j in range (column2):
		Matrix2[i][j] = int(input("Enter the element for Matrix2:"))

#Creating a mtrix to store Result matrix

for i in range (row1):
	Result.append([0]*column2)
	for j in range (column2):
		Result[i][j] = 0

#Logic for matrix miltiplication

for i in range (row1):
	for j in range (column2):
		for k in range (row2):
			Result[i][j]+=Matrix1[i][k]*Matrix2[k][j]
print("Matrix1:\t")
print(Matrix1)
print("Matrix2:\t")
print(Matrix2)# Print first Matrix
print("Result matrix:\t")
print(Result)# Print result Matrix