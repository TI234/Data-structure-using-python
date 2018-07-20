#-----------------------------------------------------
#Taking input for matrix
#-----------------------------------------------------
row = int(input("Enter the no. of row:"))
column = int(input("Enter the no. of column:"))
matrix = []
for i in range (row):
	matrix.append([0]*column)
	for j in range (column):
		matrix[i][j] = int(input("Enter the element for [{0}][{1}] Position:".format(i,j)))
print("input matrix:\n\t",matrix)
#------------------------------------------------------
# creating a matrix to stote the result
#------------------------------------------------------
result=[]
for i in range (column):
	result.append([0]*row)
	for j in range (row):
		result[i][j]=matrix[j][i]
print("Transpose of input matrix:\n\t",result) 
