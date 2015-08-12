# This example aims to show the list of prime numbers which is smaller than an input number
from ex0 import isPrime

# Input a number:
print("Enter a numer:")
m = int(input())
print("List of prime number which is smaller than "+str(m)+" is:")

# Check all numbers in range from 1 to m
for x in range(1,m):
	if isPrime(x):
		print("%d "%(x),end="",flush=True)

print("\nEnd!")
