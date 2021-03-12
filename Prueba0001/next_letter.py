"""
    Document:    DDATM-ES-0001-E
    Description: This class handles the behavior of replace letters in an alphabet for the next letter.
    Create Date: 12/03/21
    Author:      Juan castro
"""

class NextLetter:
    
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

    def next_word(self, word: str, abcdary: list = abc) -> str:
        try:
            if type(word) != type(''):
                raise TypeError

            next_word = ''
            for letter in word:
                try:
                    is_lower = letter.islower()
                    position = (abcdary.index(letter if is_lower else letter.lower()) + 1) % len(abcdary)
                    next_word += abcdary[position] if is_lower else abcdary[position].upper()
                except ValueError:
                    next_word += letter
            return next_word
            
        except TypeError:
            return "Please, send a string as the first parameter"

    def run(self):
        word = input('Enter a word, please: \n')
        print(self.next_word(word))