alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    plain_text = text
    cipher_text = ""
    for letter in text:
        og_index = int(alphabet.index(letter))
        print(og_index)
        new_index = int(alphabet.index(letter)) + shift
        print(f"new index raw: {new_index}")
        if new_index > 25:
            #print(f"new index: {new_index}")
            div = new_index // 26
            #print(f"div: {div}")
            new_index -= ((26 * div) - 1)
            print(f"final new index: {new_index}")
            cipher_text += alphabet[new_index]
            #print(f"cipher: {cipher_text}")
        else:
            cipher_text += alphabet[new_index]
            #print(f"cipher: {cipher_text}")
    print(f"Final Plain: {plain_text}")
    print(f"Final Cypher: {cipher_text}")
        

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    cipher_text = text
    plain_text = ""
    for letter in text:
        og_index = int(alphabet.index(letter))
        print(og_index)
        new_index = int(alphabet.index(letter)) - shift
        print(f"new index raw: {new_index}")
        if new_index < 0:
            #print(f"new index: {new_index}")
            div = new_index // 26
            print(f"div: {div}")
            new_index -= ((26 * div) + 1)
            print(f"final new index: {new_index} - {alphabet[new_index]}")
            plain_text += alphabet[new_index]
        else:
            plain_text += alphabet[new_index]
    print(f"Plain: {plain_text}")
    print(f"Cypher: {cipher_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
#Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
def main():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text,shift)

main()