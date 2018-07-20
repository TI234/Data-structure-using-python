#----------------------------------------------
# Logic For quick Sort:
#----------------------------------------------
def Partition(A,low,high):
	i = (low-1)
	pivot = A[high]
	for j in range (low,high):
		if A[j]<=pivot:
			i+=1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[high] = A[high],A[i+1]
	return (i+1)
def QuickSort(A,low,high):
	if low<high:
		pi = Partition(A,low,high)
		QuickSort(A,low,pi-1)
		QuickSort(A,pi+1,high)

#----------------------------------------------
#Quick_Sort.py
# Takimg input array
#----------------------------------------------
A = []
x = int(input("Enter the size of array:"))
for i in range (x):
	y = int(input("Enter the element:"))
	A.append(y)
print("Before Sorting:",A)
n = len(A)-1
QuickSort(A,0,n)
print("After Sorting:",A)