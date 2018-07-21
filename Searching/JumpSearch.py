#----------------------------------------------
# JumpSearch.py
#----------------------------------------------
def Jump_Search(Array,oldjump,newjump,item):
	length = len(Array)
	if Array[length-1]<item:
		print("Item not found in Array...")
	elif Array[newjump] == item:
		print("Item found at {0} position...".format(newjump+1))
	elif Array[newjump]>item:
		i = newjump-1
		while i>oldjump:
			if Array[i] == item:
				print("Item found at {0} position...".format(i+1))
				break
			i-=1
		if i==oldjump:
			print("Item not found in Array.... ")
	else:
		length = len(Array)
		oldjump = newjump
		newjump = newjump*2
		if newjump<=length-1:
			Jump_Search(Array,oldjump,newjump,item)
		else:
			i=oldjump+1
			while i<=length-1:
				if Array[i]==item:
					print("Item found at {0} position".format(i+1))
					break
				i+=1
			if i==length:
				print("Item not found in Array.... ")			
#----------------------------------------------
#input Array should be Sorted
#----------------------------------------------
inptArray = []
sizeOf_inpt_Array = int(input("Enter the size of Array:"))
for i in range (sizeOf_inpt_Array):
	element = int(input("Enter the element:"))
	inptArray.append(element)
print("Input Array:",inptArray)
item  = int(input("Enter the item which you want to search:"))
Jump_Search(inptArray,0,4,item)
