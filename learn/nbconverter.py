# convert from decimal number to any other number system
def dtox(str_nb,x,get_x):
	ret = ''
	str_nb = str(str_nb)
	if(not str_nb.isdigit()):
		print("ERROR: Invalid input")
	d_nb = int(str_nb)
	if (d_nb<0):
		print("Not implemented yet")
		return ret
	if(x<2):
		print("Invalid system number")
		return ret
	if(x==16):
		get_x = get_hexa
	while (d_nb>0):
		r = d_nb % x
		d_nb = d_nb // x
		if(x > 9):
			# print("r: ",str(r))
			r=get_x(r)

		ret = str(r) + ret
	if(x>9 and get_x is None):
		print("Don't know how to convert 10 to a number in system of " + x)
		return ret
	return ret

# Count number of character in a number
def c_counter(nb):
	if(not nb.isdigit()):
		return len(nb)
	if(int(nb)<0):
		print("Error: Invalid input")
		return 0
	nb = str(nb)
	return len(nb)

# get character for 16 system
def get_hexa(nb):
	if(nb < 10):
		return nb
	if (nb==10):
		return 'A'
	if (nb==11):
		return 'B'
	if (nb==12):
		return 'C'
	if (nb==13):
		return 'D'
	if (nb==14):
		return 'E'
	if (nb== 15):
		return 'F'
	if (nb>15):
		print("Error: cannot get character of "+nb+" in hexa system")
		return None

# Convert a number from system x to decimal number
def xtod(n_x,x,get_x):
	if(x<0 | x<2 ):
		print("ERROR: Invalid input")
		return None
	ret = 0;
	str_x = str(n_x)
	len_x = c_counter(n_x)
	for i in range(c_counter(n_x)):
		c = str_x[i]
		if(c.isdigit()):
			if (int(c) >= x ):
				print("ERROR: Invalid format: " + c + " > "+ str(x))
				return None
		if(x<10):
			ret += int(c) * pow(x,len_x-1)
			# print("DEBUG: " + c + " | "+str(x)+" = "+str(ret))
		else:
			if(x == 16):
				get_x = convert_hex
			elif(get_x == None):
				print("ERROR: Cannot find convert function")
				return None
			nb = get_x(c)
			if(nb==0):
				return None
			else:
				ret += nb * pow(x,len_x-1)
		len_x = len_x-1
	return ret

# Convert from a Hexa character to decimal number
def convert_hex(c):
	if(c.isdigit()):
		return int(c)
	if(c=='A'):
		return 10
	if(c=='B'):
		return 11
	if(c=='C'):
		return 12
	if(c=='D'):
		return 13
	if(c=='E'):
		return 14
	if(c=='F'):
		return 15
	print("ERROR: The character does not exist in hexa system: " + c)
	return 0

# Convert from Binary to hexa
def atob(n_b,a,b):
	if(a<2 | b< 2):
		print("ERROR: Invaid system")
	if(a==b):
		return str(n_b)
	if (a==10):
		return dtox(n_b,b,None)
	if (b==10):
		return str(xtod(n_b,a,None)) 
	db = xtod(n_b,a,None)
	ret = dtox(db,b,None)
	return ret 

# Tes
print("nbconverter module\n")
if __name__=="__main__":
	cont = 1
	while cont:
		print("***** CONVERT FROM A SYSTEM TO OTHER SYSTEM *****")
		e = input("Number:")
		f = int(input("System 1:"))
		g = int(input("System 2:"))
		print(atob(e,f,g))
		cont = int(input("Try again? 0-No/1-Yes: "))
