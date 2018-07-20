# Bubble sorting
#---------------------------------------------------
# Taking User input of an arry:
#---------------------------------------------------
array = []
x = int(input("Emter the no. of element in array:"))
for i in range (x):
	y = int(input("Enter the Element:"))
	array.append(y)
print("Before sorting:",array)
#---------------------------------------------------
#Logic for bubble Sort
#---------------------------------------------------
for i in range (len(array)):
	for j in range (len(array)-i-1):
		if array[j]>=array[j+1]:
			array[j],array[j+1] = array[j+1],array[j] 
print("After Sorting:",array)
