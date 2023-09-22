def encrypt(text, key):
    cypher_text = ''
    for letter in text:
        cypher_text += chr(ord(letter) + key)
    return cypher_text

def decrypt(text, key):
    cypher_text = ''
    for letter in text:
        cypher_text += chr(ord(letter) - key)
    return cypher_text

def user_text():
    user_text = input("Put your text:\n")
    return user_text

def user_key():
    user_key = int(input("Put your key:\n"))
    return user_key

user_choise = int(input("Choose your operation:\n(1)Encrypt\n(2)Decrypt\n"))
if user_choise == 1:
    print(encrypt(user_text(), user_key()))
elif user_choise == 2:
    print(decrypt(user_text(), user_key()))
else:
    print("Wrong choise")