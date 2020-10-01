def caesarCipherEncryptor(string, key):
	alphabet = [chr(x) for x in range(97, 123)]
	newString = ""
	for char in string:
		newcharIndex = (alphabet.index(char) + key) % 26
		newString += alphabet[newcharIndex]
	return newString

print(caesarCipherEncryptor("johanna", 7))
