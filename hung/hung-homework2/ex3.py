# Create a list
mylist = [1,23,4,5,6,7,8,868,8,9,456]

# Print number element of list
print("Number element of list: %d"%(len(mylist)))

# Print the list element of mylist without index
print("List element of mylist:")
for x in mylist:
	print(x)

# Print the list eleement of mylist with the index
print("List element of mylist (with index):")
for i in range(len(mylist)):
	print("mylist[%d] = %d"%(i,mylist[i]))

# Check if an input number is in the list
print("Enter a number: ",end="",flush=True)
x = input()
while not x.isdigit():
	print("Your input is not a number. Please enter a number: ",end="",flush=True)
	x = input()
x = int(x)
print(str(x)+" is in the list? "+str(x in mylist))

