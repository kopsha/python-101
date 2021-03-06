"""
"coconuts" has 8 letters.
A byte in binary has 8 bits.
A byte can represent a character.
We can use the word "coconuts" to communicate with each other in binary if we
use upper case letters as 1s and lower case letters as 0s.

Create a function that translates a word in plain text, into Coconut.

Worked Example
The binary for "coconuts" is
01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
c         o        c       o       n        u        t       s

Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS

coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
Examples
coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"

coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
Notes
All inputs will be strings.
Make sure to separate the coconuts with spaces.
"""


def convert_char_as_binary(character):
    """converts character to ascii and then to binary"""
    ascii_code = ord(character)
    return f"{ascii_code:08b}"


def convert_binary_to_coconuts(binary_code):
    """composes string based on coconut style"""
    reference = "coconuts"
    translation = [
        reference[i].upper() if bit == "1" else reference[i]
        for i, bit in enumerate(binary_code)
    ]
    return "".join(translation)


def coconut_translator(text):
    """translates whole given string input in coconuts mode"""
    translations = []
    for character in text:
        bin_code = convert_char_as_binary(character)
        translations.append(convert_binary_to_coconuts(bin_code))
    return " ".join(translations)


def main():
    print(coconut_translator("Good day!"))


if __name__ == "__main__":
    main()
