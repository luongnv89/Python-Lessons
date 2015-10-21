import nbconverter

# Convert from binary number to string
def binary_to_str(b_nb):
	ret = ''
	array = b_nb.split(" ")
	for x in array:
		d_nb = nbconverter.xtod(x,2,None)
		ret = ret + chr(d_nb)
	return ret	

# Convert from hexa number to string
def hexa_to_str(h_nb):
	ret = ''
	array = h_nb.split(" ")
	for x in array:
		d_nb = nbconverter.xtod(x,16,None)
		ret = ret + chr(d_nb)
	return ret	


	
# Convert from decimal number to string
def decimal_to_str(d_nb):
	ret = ''
	array = d_nb.split(" ")
	for x in array:
		ret = ret + chr(int(x))
	return ret	

if __name__=="__main__":
	print(binary_to_str("1111011 1100011 1101010 1111011 1011101"))
	print(hexa_to_str("AB B1 F4 5D 7C 8E"))
	print(decimal_to_str("100 98 49 22 230"))
