import time
asd="1,23,4,5,6,7,868,8,9,456"
print("The number of element of the string is: "+str(len(asd)))

print("asd ["+str(0)+"] is : "+str(asd[0]))
a=0
while a!=23:
	a=a+1
	time.sleep(1)
	print("asd ["+str(a)+"] is : "+str(asd[a]))
	
print("45 is in asd is: " +str('45' in asd))
