#---------------------------------------------
# BinarySearch.py
#---------------------------------------------
def Binary_Search(A,low,high,item):
	if low<high:
		mid = (low+high)//2
		if A[mid] == item:
			print("Item found at position {0}:".format(mid+1))
		elif A[mid+1] == item:
			print("Item found at position {0}:".format(mid+2))
		elif A[mid]>item:
			Binary_Search(A,low,mid-1,item)
		else:
			Binary_Search(A,mid+1,high,item)
	else:
		print("Item not found in Array........")
#---------------------------------------------
# Input Array should be Sorted
#---------------------------------------------
Array = list()
sizeOf_Array = int(input("Enter the size of Array:"))
print ("Enter the sorted Array.........")
for i in range (sizeOf_Array):
	itemOf_Array = int(input("Enter the element of Array:"))
	Array.append(itemOf_Array)
print("Input Array:",Array)
item = int(input("Enter the element which you want to search:"))
Binary_Search(Array,0,len(Array)-1,item)
#---------------------------------------------