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
# Logic for insertion sort
#----------------------------------------------
for i in range (0,(len(A)-1)):
	if A[i]>A[i+1]:
		A[i],A[i+1] = A[i+1],A[i]
	j = i-1
	if j>=0:
		while j>=0 and A[j]>A[j+1]:
			A[j],A[j+1] = A[j+1],A[j]
			j-=1
	else:
		continue
print("After Sorting:",A)