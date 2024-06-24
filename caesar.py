from caesar_art import logo

print(logo)

# def encrypt(plain_text, shift_number):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_number
#         if new_position <= 26:
#             new_letter = alphabet[new_position]
#         else:
#             new_letter = alphabet[new_position - 26]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_number):
#     decipher_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_number
#         if new_position >= 0:
#             new_letter = alphabet[new_position]
#         else:
#             new_letter = alphabet[26 + new_position]
#         decipher_text += new_letter
#     print(f"your decoded text is {decipher_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)


def caesar(plain_text, shift_number, direction):    
    if direction == "encode":
        final_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_number
                if new_position <= 26:
                    new_letter = alphabet[new_position]
                else:
                    new_letter = alphabet[new_position - 26]
                final_text += new_letter
            else:
                final_text += letter
        print(f"the encoded text is {final_text}")
    elif direction == "decode":
        final_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_number
                if new_position >= 0:
                    new_letter = alphabet[new_position]
                else:
                    new_letter = alphabet[26 + new_position]
                final_text += new_letter
            else:
                final_text += letter
        print(f"your decoded text is {final_text}")


should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    result = input("do you wanna continue with the game? yes or no?/n")
    if result == "no":
        should_continue = False
    