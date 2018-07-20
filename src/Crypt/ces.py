# Seesar Sifer :)

def encrypt(text, shf):
	text = str(text)
	shf = int(shf)
	r = ''
	for i in text:
		if (ord(i) >= 97 and ord(i) <= 122):
			r += chr(((ord(i) + shf - 97) % 26) + 97)
		elif (ord(i) >= 65 and ord(i) <= 90):
			r += chr(((ord(i) + shf - 65) % 26) + 65)
		else:
			r += i

	return r

def decrypt(text, shf):
	text = str(text)
	shf = int(shf)
	r = ''
	for i in text:
		if (ord(i) >= 97 and ord(i) <= 122):
			r += chr(((ord(i) - shf - 97) % 26) + 97)
		elif (ord(i) >= 65 and ord(i) <= 90):
			r += chr(((ord(i) - shf - 65) % 26) + 65)
		else:
			r += i

	return r
	return


#for i in range(0, 5):
#	inp = input('$')
#	if (inp == "e"):
#		inp = input("EW: ")
#		inp2 = input("SHF: ")
#		print(encrypt(inp, inp2))
#
#	elif (inp == "d"):
#		inp = input("DW: ")
#		inp2 = input("SHF: ")
#		print(decrypt(inp, inp2))
