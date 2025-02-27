import sys
import string

def count_characters(text):
    """
    Count the number of upper case letters, lower case letters, punctuation marks, spaces and digits in a given text.
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    return upper, lower, punctuation, spaces, digits

def main():
    """
    Main function to count the number of upper case letters, lower case letters, punctuation marks, spaces and digits in a given text.
    """
    try:
        if len(sys.argv) == 1:
            text = "Hello World! "
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("More than one argument provided")

        upper, lower, punctuation, spaces, digits = count_characters(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()