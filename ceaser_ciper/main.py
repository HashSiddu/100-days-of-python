#caesar cipher is one of the encrypt and decrypt program
import logo_alphabets
print(logo_alphabets.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





def caesar(original_text,shift,encode_or_decode):
    final_output = ""
    if encode_or_decode == "decode":
        shift*=-1
    for letter in word:
        if letter not in alphabet:
            final_output+=letter
        else:

            letter_index = alphabet.index(letter) + shift
            letter_index%=len(alphabet)
            final_output+=alphabet[letter_index]
    print(f"{encode_or_decode}d word is {final_output}")    

should_stop = True
while should_stop:
    decision = input("type  'encode' to encrypt or decode to 'decrypt' ")
    word = input("Enter the word ")
    shift = int(input("Enter the shift number "))
    caesar(original_text=word,encode_or_decode=decision,shift=shift)
    restart = input("do you want to check again type 'yes' or 'no'").lower()
    if restart == "no":
        should_stop = False







