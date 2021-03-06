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