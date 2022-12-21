def xor_encrypt(file_text, key):
	"""
	Encrypts text
	file_text - text
	key - key for encrypting
	"""
    encrypt_str = ""
    for line in file_text:
        for letter in line:
            encrypt_str += chr(ord(letter)^key)
    return  encrypt_str

f = open("File.txt", "r") 
text = f.read()
key  = 8
print("Оригинал:\t", text)
encr_strg = xor_encrypt(text, key) 
print("Зашифрованное:\t", encr_strg)
print("Расщифрованное:\t", xor_encrypt(encr_strg, key))
f.close()
