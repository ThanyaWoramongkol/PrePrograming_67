# Define a dictionary mapping Morse code to characters

def decode(morse_code):
    output = []
    word = ""
    sentence = ""
    code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F"
            , "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L"
           , "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R"
           , "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X"
           , "-.--": "Y", "--..": "Z", ".----": "1", "..---": "2", "...--": "3"
           , "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8"
           , "----.": "9", "-----": "0"}
    for character in morse_code:
        if character in code:
            word += code[character]
        elif character ==  "/":
            output.append(word + " ")
            word = ""
    output.append(word)
    for kum in output:
        sentence += kum.capitalize()
    print(morse_code)
    return sentence

def encode(text):
    text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

    morse_code = []
    for char in text.upper():
        if char in text_to_morse:
            morse_code.append(text_to_morse[char])
        else:
            morse_code.append(char)  # Preserve non-alphanumeric characters
    return ' '.join(morse_code)

while True:
    input_text = input()
    if input_text == "-1":
        break
    encoded_text = encode(input_text)
    decoded_text = decode(encoded_text.split())
    print(f"Input text: {decoded_text}")
    print(f"Encoded Morse code: {encoded_text}")
    print("==================================")
