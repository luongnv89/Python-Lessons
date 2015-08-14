print("Enter the electricity of the first family:")
family=float(input())

print("Enter the electricity of the second family:")
family2=float(input())

if family<=50:
	family*=4
elif 50<family<=100:
	family*=3+family*4
else:
	family*=2+family*3+family*4
print("The money for pay of family 1 is:"+str(family))

if family2<=50:
	family2*=4

elif 50<family2<=100:
	family2*=3+family*4
else:
	family2*=2+family*3+family*4
print("The money for pay of family 2 is"+str(family2))
if family!=family2:
	print(str(min(family,family2))+"<"+str(max(family,family2)))
else:
	print("The money for pay of two family is equal.")

