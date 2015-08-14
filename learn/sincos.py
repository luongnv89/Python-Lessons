import math

def mysin(x):
	return math.sin(math.radians(x))

def mycos(x):
	return math.cos(math.radians(x))

print("Enter value of angle in degree: ",)
degr = int(input())
s = mysin(degr)
c = mycos(degr)
print("sin(%d) = %f"%(degr,s))
print("cos(%d) = %f"%(degr,c))
print("sin(%d)^2 + cos(%d)^2 = %f"%(degr,degr,s*s+c*c))
