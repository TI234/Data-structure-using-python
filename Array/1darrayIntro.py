#simply creating an array with given size

A = [] # initializing Array
x = int(input("Enter the size of array:"))#Taking user input and store into x
for i in range (x):
	y = int(input("Enter the element:"))
	A.append(y) #appending element in Array
print(A) # print array

# Simply finding largest element from given arrray:
maximum = 0
for i in A: # Travrse from 0 index to Last index
        if i>maximum:
            maximum = i
print("largest Element of the given array is:",maximum)

# Searching element in array
search_Element = int(input("Enter the element which you want to search:"))
for i in range (len(A)-1): # here len() is predefind function which finds length of Array
	if A[i] == search_Element: # found searched Element
		print("Element found at position:",i)
if search_Element not in A:	
	print("Element not found in array")