#insertion_sort.py
#----------------------------------------------
# Creating an array with given Size:
#----------------------------------------------
A = []
x = int(input("Enter the size of array:"))
for i in range (x):
	y = int(input("Enter the element:"))
	A.append(y)
print("Before Sorting:",A)
#----------------------------------------------
# Logic for Selection Sort:
#----------------------------------------------
for i in range (len(A)):
	min = i
	for j in range (i+1,len(A)):
		if A[min]>A[j]:
			min = j
	A[min],A[i] = A[i],A[min]
print("After Sorting:",A)