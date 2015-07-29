print("First number: ",end="",flush=True)
a = input()
if a.isdigit():
	a = int(a)
	print("Second number: ",end="",flush=True)
	b =input()
	if b.isdigit():
		b = int(b)
		print("Sum: "+str(a+b))
