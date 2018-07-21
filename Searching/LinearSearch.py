#----------------------------------------------
# LinearSearch.py
#----------------------------------------------
def LinearSearch(Array,item):
	size = len(Array)
	for i in range (size):
		if Array[i]==item:
			print("Item found at position {0}".format(i+1))
	if item not in Array:
			print ("Item not found in Array")
#----------------------------------------------
Array = []
Array_Size = int(input("Enter the size of Array:"))
for i in range (Array_Size):
	y = int(input("Enter the Element:"))
	Array.append(y)
print("input Array:",Array)
item = int(input("Enter the item which you want to search:"))
LinearSearch(Array,item)