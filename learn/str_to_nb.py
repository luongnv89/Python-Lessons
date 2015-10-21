import nbconverter

# Convert a string to decimal number
def str_to_decimal(my_str):
	ret = ''
	for i in range(len(my_str)):
		d_nb = ord(my_str[i])
		ret = ret + ' ' + str(d_nb)
	return ret

# Convert a string to hexa number
def str_to_hexa(my_str):
	ret = ''
	for i in range(len(my_str)):
		d_nb = ord(my_str[i])
		h_nb = nbconverter.dtox(d_nb,16,None)
		ret = ret + ' ' + h_nb
	return ret

# Convert a string to binary number
def str_to_binary(my_str):
	ret = ''
	for i in range(len(my_str)):
		d_nb = ord(my_str[i])
		h_nb = nbconverter.dtox(d_nb,2,None)
		ret = ret + ' ' + h_nb
	return ret

# Test
print("str_to_nb module is imported\n")
if __name__=="__main__":
	m_str = input("Enter a string:\n")
	print("Decimal:\n",str_to_decimal(m_str)) 
	print("Hexa:\n",str_to_hexa(m_str)) 
	print("Binary:\n",str_to_binary(m_str)) 
