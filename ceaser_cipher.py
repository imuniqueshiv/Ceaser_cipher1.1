from ceaser_cipher_art import art_str

print(art_str)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Corrected the placement of the comment
    if encode_or_decode == "decode":
        shift_amount *= -1  # Shift backwards for decoding

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter  # Add non-alphabet characters directly
            continue  # Skip to the next iteration if the letter is not in the alphabet

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)  # Ensure it wraps around within the alphabet
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' for encrypt, type 'decode' for decrypt:\n").lower()
    text = input("Type your message:\n").lower()  # Convert text to lowercase to match alphabet list
    shift = int(input("Type the shift number:\n"))

    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
