#Programmer name: Susan Li
#Program creation date: August 25, 2022

#Encrypt and decyrpt a phrase

#ask for a phrase
phrase = input("Enter a phrase: ")

#encrypt the phrase
def cipher_text():
    encrypted_phrase = ""
    for letter in phrase:
        if letter == " " or letter == "." or letter == "," or letter == ":" or letter == ";":
            encrypted_letter = letter
        elif letter == "x":
            encrypted_letter = "a"
        elif letter == "y":
            encrypted_letter = "b"
        elif letter == "z":
            encrypted_letter = "c"
        else:
            int_value = ord(letter)
            converted_int = int_value + 3
            encrypted_letter = chr(converted_int)
        encrypted_phrase = encrypted_phrase + encrypted_letter
    return(encrypted_phrase)
encrypted_phrase = cipher_text()
#decrypt the phrase
def plain_text():
    decrypted_phrase = ""
    for letter in encrypted_phrase:
        if letter == " " or letter == "." or letter == "," or letter == ":" or letter == ";":
            decrypted_letter = letter
        elif letter == "a":
            decrypted_letter = "x"
        elif letter == "b":
            decrypted_letter = "y"
        elif letter == "c":
            decrypted_letter = "z"
        else:
            int_value = ord(letter)
            converted_int = int_value - 3
            decrypted_letter = chr(converted_int)
        decrypted_phrase = decrypted_phrase + decrypted_letter
    return(decrypted_phrase)
decrypted_phrase = plain_text()
#print the encrypted and decrypted phrases
print("Cipher text: {}".format(encrypted_phrase))
print("Plain text: {}".format(decrypted_phrase))
