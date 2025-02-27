import sys

def textToMorse(text):
    morsDic = {
        'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
        'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",
        'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
        'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
        'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..",
        '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-",
        '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.",
        ' ': "/"
    }
    text = text.upper()
    morse_code = ' '.join(morsDic[char] for char in text if char in morsDic)
    return morse_code

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        if not all(char.isalnum() or char.isspace() for char in sys.argv[1]):
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
        sys.exit(1)
    
    text = sys.argv[1]
    print(textToMorse(text))