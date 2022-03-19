
def grey_letters(word: str, letters: list) -> bool:
    w = list(word)
    check =  any(letter in w for letter in letters)
    return check

def yellow_letters(word: str, letters: list) -> bool:
    w = list(word)
    check =  all(letter in w for letter in letters)
    return check

def green_letters(word: str, letters: dict) -> bool:
    check = []
    w = list(word)
    for key, value in letters.items():
        if w[key] == value:
            check.append(True)
        else:
            check.append(False)
    
    return all(check)

def wordle(grey: list, yellow: list, green: dict, guesses: list):

    with open('wordle_dict.txt', 'r') as f:
        _words = f.read().splitlines()

    for word in _words:
        if len(grey) > 0 and len(yellow) > 0 and len(green) > 0:
            if not grey_letters(word, grey) and yellow_letters(word, yellow) and green_letters(word, green):
                if word not in guesses:
                    print(word)

        elif len(grey) > 0 and len(yellow) > 0:
            if not grey_letters(word, grey) and yellow_letters(word, yellow):
                if word not in guesses:
                    print(word)

        elif len(yellow) > 0 and len(green) > 0:
            if yellow_letters(word, yellow) and green_letters(word, green):
                if word not in guesses:
                    print(word)

        elif len(grey) > 0 and len(green) > 0:
            if not grey_letters(word, grey) and green_letters(word, green):
                if word not in guesses:
                    print(word)

        elif len(green) > 0 and len(grey) == 0 and len(yellow) == 0:
            if green_letters(word,green):
                if word not in guesses:
                    print(word)

        else:
            print('Not enough parameters met')