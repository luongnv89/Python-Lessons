mylist = [1,23,4,5,6,7,8,868,8,9,456]

print("Number elements of list: %d"%(len(mylist)))

print("List element of mylist:")
for x in mylist:
	print(x)

print("List element of mylist (with index):")
for i in range(len(mylist)):
	print("mylist[%d] = %d"%(i,mylist[i]))
