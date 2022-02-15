from letter_types import *

with open('wordle_dict.txt', 'r') as f:
    words_ = f.read().splitlines()

grey = ['c', 'n', 'e']
yellow = ['o']
green = {1:'r', 0:'a'}

for word in words_:
    if len(grey) > 0 and len(yellow) > 0 and len(green) > 0:
        if not grey_letters(word, grey) and yellow_letters(word, yellow) and green_letters(word, green):
            print(word)
    elif len(grey) > 0 and len(yellow) > 0 and len(green) == 0:
        if not grey_letters(word, grey) and yellow_letters(word, yellow):
            print(word)
    elif len(yellow) > 0 and len(green) > 0 and len(grey) == 0:
        if yellow_letters(word, yellow) and green_letters(word, green):
            print(word)
    elif len(grey) > 0 and len(green) > 0 and len(yellow) == 0:
        if not grey_letters(word, grey) and green_letters(word, green):
            print(word)
    else:
        print('Minimum criteria not met for results')