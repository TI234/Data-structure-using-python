#Counting_Sort.py
#----------------------------------------------
# Logic for counting Sort:
#----------------------------------------------
def CountingSort(A,maxValue,minValue):
	Temp_Array = []
	length_A = len(A)
#----------------------------------------------
# Creating Temp array:
#----------------------------------------------
	for i in range (minValue,(maxValue+1)):
		Temp_Array.append(0)
	print(Temp_Array)
#----------------------------------------------
#Counting the elements and storing in temporary Array
#----------------------------------------------
	for i in range(len(A)):
		Temp_Array[A[i]-minValue]+=1
	print("counting:\t",Temp_Array)
#----------------------------------------------
# Logic for Counting Sort
#----------------------------------------------
	x = 0
	for i in range (len(Temp_Array)):
		if Temp_Array[i] != 0:
			for j in range (Temp_Array[i]):
				A[x] = minValue+i
				x+=1
	print("After Sorting:",A)
#----------------------------------------------
#Taking input of unSorted Array:
#----------------------------------------------
A = []
num = int(input("Enter the size of unsorted Array:"))
for i in range (num):
	Element = int(input("Enter the Element:"))
	A.append(Element)
print("Before Sorting:\t",A)
minValue = min(A)
maxValue = max(A)
CountingSort(A,maxValue,minValue)
#----------------------------------------------