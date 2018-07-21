#----------------------------------------------
# InterPolationSearch.py
#----------------------------------------------
def InterPolationSearch(Array,start,last,item):
	try:
		pos = int(start+(((last-start)/(Array[last]-Array[start]))*(item-Array[start])))
		if Array[pos]==item:
			print("item found at position {0}".format(pos+1))
		elif item>Array[pos]:
			pos+=1
			InterPolationSearch(Array,pos,last,item)
		# if item < Array[pos]
		else:
			pos-=1
			InterPolationSearch(Array,pos,last,item)
	except RecursionError:
		print("Item not found in Array...")
#----------------------------------------------
Arr = list()
size_Arr = int(input("Enter the Size of Array:"))
for i in range (size_Arr):
	element = int(input("Enter the Element:"))
	Arr.append(element)
print("Input Array:",Arr)
startIndex = 0
lastIndex = len(Arr)-1
item = int(input("Enter the Element which you want to Search:"))
InterPolationSearch(Arr,startIndex,lastIndex,item)