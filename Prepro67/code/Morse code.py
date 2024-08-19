"""Morse code"""

def main(txt):
    """-"""
    first = True
    output = ''
    code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F"
            , "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L"
           , "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R"
           , "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X"
           , "-.--": "Y", "--..": "Z", ".----": "1", "..---": "2", "...--": "3"
           , "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8"
           , "----.": "9", "-----": "0"}
    for character in txt:
        if character in code and first:
            output += code[character]
            first = False
        elif character in code:
            output += code[character].lower()
        elif character ==  "/":
            output += " "
            first = True
    print(output)
main(input().split())
