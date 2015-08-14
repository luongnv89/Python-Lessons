import math
def pi(a,x):
	return math.pi*x*a

print("Enter a number for calcul perimeter:")
nb=float(input())
print(pi(2,nb))
a=pi(2,nb)

print("Enter a number for calcul acreage:")
nb2=float(input())
print(pi(nb2,nb2))
b=pi(nb2,nb2)

print("Enter a number for calcul perimeter:")
nb3=float(input())
print(pi(2,nb3))
c=pi(2,nb3)

print("Enter a number for cacul acreage:")
nb4=float(input())
print(pi(nb4,nb4))
d=pi(nb4,nb4)
print("") #For read easier

print(str(max(a,c))+">"+str(min(a,c)))

print("") #For read easier

print(str(max(b,d))+">"+str(min(b,d)))
