import art
from operator import index
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# Created a function called 'encrypt() and decrypt' that takes 'original_text' and 'shift_amount' as 2 inputs and shift the letter.
# Commenting the below lines as I have combined the function into one

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"You encoded message is : {cipher_text}")


# def decrypt(original_text,shift_amount):
#     decrypt_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decrypt_text += alphabet[shifted_position]
#     print(f"You encoded message is : {decrypt_text}")


# Creating one definition which is combined logic for both Encrypt or Decrypt
# Single Function
def cipher(original_text,shift_amount,encode_or_decode):
    output_text = ""

    # Handling if user enters in correct cipher method
    if encode_or_decode not in ["encode", "decode"]:
        print("Invalid operation. Please choose 'encode' or 'decode'.")
        return

    for letter in original_text:

        # For Decode (Backward Movement)
        if encode_or_decode == "decode":
            shift_amount *= -1

        # Handling character except alphabets
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"You {direction}d message is : {output_text}")

# Calling the 'encrypt() and decrypt' function and pass in the user inputs. You should be able to test the code and encrypt a message.
# Commenting the below lines as I have combined the function into one
# encrypt(original_text=text,shift_amount=shift)
# decrypt(original_text=text,shift_amount=shift)


# Creating option to Restart or Exit the game

should_continue = True

while should_continue:

    #Input from User
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    # One calling Function
    cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'Yes' to continue or 'No' to exit : ").lower()
    if restart == "no":
        should_continue = False
        print("We are signing off, Thank you!")


