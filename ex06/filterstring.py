import sys
from ft_filter import ft_filter

def main():
    """
    this function will filter the words of a string  depending on the number is giving to it 
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        if not all(char.isalpha() or char.isspace() for char in sys.argv[1]):
            raise AssertionError("AssertionError: the arguments are bad")
        if not sys.argv[2].isdigit():
            raise AssertionError("AssertionError: the arguments are bad")
        
        S = sys.argv[1]
        N = int(sys.argv[2])
        
        words = S.split()
        result = ft_filter(lambda word: len(word) > N, words)
        print(result)
        
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()