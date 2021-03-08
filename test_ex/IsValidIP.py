def isValidIP(ip):
	octs = ip.split('.')
	if len(octs) == 4:
		for o in octs:
			try:
				if int(o) < 0 or int(o) > 255 or len(o) != len(str(int(o))):
					return False
			except:
				return False
		return True
	return False

print(isValidIP("1.2.3.4"))
print(isValidIP("1.2.3"))
print(isValidIP("1.2.3.4.5"))
print(isValidIP("123.45.67.89"))
print(isValidIP("123.456.78.90"))
print(isValidIP("123.045.067.089"))