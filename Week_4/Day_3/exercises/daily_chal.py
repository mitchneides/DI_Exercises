choice = input("Enter 1 for encryption, 2 for decryption: ")
while choice != '1' and choice != '2':
    print("Must enter 1 or 2. Try again...")
    choice = input("Enter 1 for encryption, 2 for decryption: ")

def encrypt(str,num):
    encrypted_string = ''
    for letter in str:
        num_val = int(ord(letter))
        shifted_num = num_val + num
        replaced_letter = chr(shifted_num)
        encrypted_string = encrypted_string+replaced_letter
    print("Your encrypted message: " + encrypted_string)

def decrypt(str,num):
    decrypted_string = ''
    for letter in str:
        num_val = int(ord(letter))
        shifted_num = num_val - num
        replaced_letter = chr(shifted_num)
        decrypted_string = decrypted_string + replaced_letter
    print("Your decrypted message: " + decrypted_string)

if choice == '1':
    str1 = input("Enter a string to be encrypted: ")
    num1 = int(input("Enter your desired shift number: "))
    encrypt(str1,num1)
else:
    str2 = input("Enter a string to be decrypted: ")
    num2 = int(input("Enter the required shift number: "))
    decrypt(str2,num2)

