def Merge_Sort(A):
	n = len(A)
	if n==1:
		return
	mid = int(n/2)
	left_Array = A[:mid]
	print(left_Array)
	right_Array = A[mid:]
	print(right_Array)
	Merge_Sort(left_Array)
	Merge_Sort(right_Array)
	i,j,k = 0,0,0
	while (i<len(left_Array) and j<len(right_Array)):
		if left_Array[i]<right_Array[j]:
			print("comparing:",left_Array[i],right_Array[j])
			A[k] = left_Array[i]
			i+=1
			print("i is",i)
		else:
			A[k] = right_Array[j]
			j+=1
			print("j is:",j)
		k+=1
		print("k is:",k)
	while(i<len(left_Array)):
		A[k] = left_Array[i]
		i+=1;print("2i:",i)
		k+=1;print("2k:",k)
	while(j<len(right_Array)):
		A[k] = right_Array[j]
		j+=1;print("2j:",j)
		k+=1;print("2k:",k)
#---------------------------------------------------
A = []
size = int(input("Enter the size of array:"))
for i in range (size):
	x = int(input("enter the element:"))
	A.append(x)
print("Before sorting:",A)
Merge_Sort(A)
print("After sorting:",A)
#---------------------------------------------------