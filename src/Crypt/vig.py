# Finyeere Sifer :)

def encrypt(text, key):
	def repeatToMatchSize(s, sz):
		r = ''
		while (len(r) < sz):
			r += s[len(r) % len(s)]
		return r

	def toAlpNum(_chr):
		if (_chr >= 97 and _chr <= 122):
			return _chr - 97
		elif (_chr >= 65 and _chr <= 90):
			return _chr - 65
		else:
			return _chr

	text = str(text)
	key = repeatToMatchSize(str(key), len(text))
	r = ''
	for i in range(0, len(text)):
		shf = toAlpNum(ord(key[i]))
		if (ord(text[i]) >= 97 and ord(text[i]) <= 122):
			r += chr(((ord(text[i]) + shf - 97) % 26) + 97)
		elif (ord(text[i]) >= 65 and ord(text[i]) <= 90):
			r += chr(((ord(text[i]) + shf - 65) % 26) + 65)
		else:
			r += text[i]

	return r

def decrypt(text, key):
	def repeatToMatchSize(s, sz):
		r = ''
		while (len(r) < sz):
			r += s[len(r) % len(s)]
		return r

	def toAlpNum(_chr):
		if (_chr >= 97 and _chr <= 122):
			return _chr - 97
		elif (_chr >= 65 and _chr <= 90):
			return _chr - 65
		else:
			return _chr

	text = str(text)
	key = repeatToMatchSize(str(key), len(text))
	r = ''
	for i in range(0, len(text)):
		shf = toAlpNum(ord(key[i]))
		if (ord(text[i]) >= 97 and ord(text[i]) <= 122):
			r += chr(((ord(text[i]) - shf - 97) % 26) + 97)
		elif (ord(text[i]) >= 65 and ord(text[i]) <= 90):
			r += chr(((ord(text[i]) - shf - 65) % 26) + 65)
		else:
			r += text[i]

	return r

"""
for i in range(0, 5):
	inp = input('$')
	if (inp == "e"):
		inp = input("EW: ")
		inp2 = input("KEY: ")
		print(encrypt(inp, inp2))

	elif (inp == "d"):
		inp = input("DW: ")
		inp2 = input("KEY: ")
		print(decrypt(inp, inp2))
"""
