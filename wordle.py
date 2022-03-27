from dataclasses import dataclass
from wordledict import wordle_dict


@dataclass
class WordleTypes:
    word: str
    letters: list
    @property
    def grey_letters(self) -> bool:
        w = list(self.word)
        check =  any(letter in w for letter in self.letters)
        return check
    
    @property
    def letter_check(self) -> bool:
        w = list(self.word)
        check =  all(letter in w for letter in self.letters)
        return check

    @property
    def green_check(self) -> bool:
        check = []
        w = list(self.word)
        for key, value in self.letters.items():
            if w[key] == value:
                check.append(True)
            else:
                check.append(False)
    
        return all(check)

@dataclass
class WordleSolver(WordleTypes):
    
    _grey: list
    _yellow: list
    _green: list
    
    def letter_check(self):
        w = list(self.word)
        check =  all(letter in w for letter in self.letters)
        return check

def wordle(grey: list, yellow: list, green: list, guesses: list):

    for word in wordle_dict:

        grey_letters = WordleTypes(word, grey)

        yellow_letters = WordleTypes(word,yellow)

        green_letters = WordleTypes(word, green)

        if len(grey) > 0 and len(yellow) > 0 and len(green) > 0:
            if not grey_letters.letter_check and yellow_letters.letter_check and green_letters.green_check:
                if word not in guesses:
                    print(word)

        elif len(grey) > 0 and len(yellow) > 0:
            if not grey_letters.letter_check and yellow_letters.letter_check:
                if word not in guesses:
                    print(word)

        elif len(yellow) > 0 and len(green) > 0:
            if yellow_letters.letter_check and green_letters.green_check:
                if word not in guesses:
                    print(word)

        elif len(grey) > 0 and len(green) > 0:
            if not grey_letters.letter_check and green_letters.green_check:
                if word not in guesses:
                    print(word)

        elif len(green) > 0 and len(grey) == 0 and len(yellow) == 0:
            if green_letters.green_check:
                if word not in guesses:
                    print(word)

        else:
            print('Not enough parameters met')