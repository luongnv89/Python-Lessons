import math
def pi(a,x):
	return math.pi**a*x

print("Enter a number for calcul perimeter:")
nb=float(input())
print(pi(1,nb))
a=pi(1,nb)

print("Enter a number for cacul acreage:")
nb2=float(input())
print(pi(2,nb2))
b=pi(2,nb2)

print("Enter a number for calcul perimeter:")
nb3=float(input())
print(pi(1,nb3))
c=pi(1,nb3)

print("Enter a number for cacul acreage:")
nb4=float(input())
print(pi(2,nb4))
d=pi(2,nb4)
print("")#For read easier

print(min(a,c))

print("") #For read easier

print(min(b,d))
