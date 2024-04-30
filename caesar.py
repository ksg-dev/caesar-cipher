alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction, text, shift):
    plain_text = ""
    cipher_text = ""
    if direction == "encode":
        for letter in text:
            new_index = int(alphabet.index(letter)) + shift
            if new_index > 25:
                div = new_index // 26
                new_index -= (26 * div)
                cipher_text += alphabet[new_index]
            else:
                cipher_text += alphabet[new_index]
        print(f"The encoded text is: {cipher_text}")
    elif direction == "decode":
        for letter in text:
            new_index = int(alphabet.index(letter)) - shift
            plain_text += alphabet[new_index]
       
        print(f"The decoded text is: {plain_text}")
    else:
        print("Something is broken.")

caesar(direction, text, shift)