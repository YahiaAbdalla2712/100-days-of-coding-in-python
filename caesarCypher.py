alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(original_text,shift_amount,direction):
    encrypted_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letters in original_text:
        if letters not in alphabet:
            encrypted_text+=letters
        else:
            new_position = alphabet.index(letters) + shift_amount
            new_position %= len(alphabet)  # will always make sure that we are in the range of alphabet length
            encrypted_text += alphabet[new_position]

    print(f"Here is the {direction}d text: {encrypted_text}")


operation = input("Type 'encode' to encrypt and 'decode' to decrypt ")
message = input("enter your message ")
shift_numebr = int(input("enter shift amount "))
caesar(message,shift_numebr,operation)


yes_or_no = input("type yes if u wanna do one more no to exit ")
while(yes_or_no == "yes"):
    operation = input("Type 'encode' to encrypt and 'decode' to decrypt ")
    message = input("enter your message ")
    shift_numebr = int(input("enter shift amount "))
    caesar(message, shift_numebr, operation)
    yes_or_no = input("type yes if u wanna do one more no to exit")

print("Thanks")
