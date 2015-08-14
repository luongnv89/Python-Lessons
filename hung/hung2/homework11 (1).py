print("Enter the electricity of the first family:")
family=float(input())
def m(a,x):
	a=a*x
	return a
print("Enter the electricity of the second family:")
family2=float(input())

if family<=50:
	z=m(family,4)
elif 50<family<=100:
	z=m(family,7)
else:
	z=m(family,9)
print("The money for pay of family 1 is:"+str(z))

if family2<=50:
	x=m(family2,4)

elif 50<family2<=100:
	x=m(family2,7)
else:
	x=m(family2,9)
print("The money for pay of family 2 is"+str(x))
if family!=family2:
	print(str(min(z,x))+"<"+str(max(z,x)))
else:
	print("The money for pay of two family is equal.")

