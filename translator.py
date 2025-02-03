#morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', 
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

#text to Morse code
def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        morse_code.append(MORSE_CODE_DICT.get(char, '?'))  # '?' for unsupported characters
    return ' '.join(morse_code)

#morse code to text
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    morse_words = morse.split(' / ')  # Split Morse into words
    decoded_words = []
    for word in morse_words:
        decoded_chars = [reverse_dict.get(char, '?') for char in word.split()]
        decoded_words.append(''.join(decoded_chars))
    return ' '.join(decoded_words)

#main program
if __name__ == "__main__":
    while True:
        print("\nMorse Code Translator")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print(f"Morse Code: {text_to_morse(text)}")
        elif choice == '2':
            morse = input("Enter Morse code to convert to text (separate letters with spaces, words with ' / '): ")
            print(f"Text: {morse_to_text(morse)}")
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")