

with open('wordle_dict.txt', 'r') as f:
    words_ = f.read().splitlines()

with open('google_word.txt', 'r') as f:
    google = f.read().splitlines()

with open('google_most_common.txt', 'w') as w:
    for word in words_:
        if word in google:
            w.write(f'{word}\n')