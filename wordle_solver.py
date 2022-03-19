from os import system, name
from wordle import wordle

def main():
    grey = []
    yellow = []
    green = {}
    guesses = []

    #Clear Console Screen
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    print("""
    **************************************************************
    *                                                            *
    *                      WORDLE SOLVER                         *
    *                           by                               *
    *                      Bradley Bell                          *
    *                                                            *    
    **************************************************************
    """)

    while True:
        
        grey_input = str(input('Enter Grey Letter(s) or hit Enter: '))

        if grey_input != '':
            for g in grey_input.split(','):
                grey.append(g)

        yellow_input = str(input('Enter Yellow Letters or hit Enter: '))

        if yellow_input != '':
            for y in yellow_input.split(','):
                yellow.append(y)
        
        green_input = str(input('Enter Green Letter(s) or hit Enter: '))

        if green_input != '':
            for g in green_input.split(','):
                k = int(g[0])
                green[k] = g[2]

        guesses_input = str(input('Enter Guess or hit Enter: '))

        if len(guesses_input) != '':
            for guess in guesses_input.split(','):
                guesses.append(guess)
        
        print('\nPossible Solutions: ')

        wordle(grey, yellow, green, guesses)

        print(f'\nGrey Letters: {grey}\nYellow Letters: {yellow}\nGreen Letters: {green}\nGuessed Words: {guesses}\n')

        continue_game = input('Continue game? ')

        if continue_game in ('no', 'n', 'No', 'NO'):
            print('Goodbye!\n')
            break

if __name__ == '__main__':
    main()