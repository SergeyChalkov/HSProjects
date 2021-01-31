from random import randint


msg = {'not_in': "That letter doesn't appear in the word", 'hangman': "H A N G M A N",
       'no_imp': "You've already guessed this letter", 'lost': "You lost!\n",
       'win': "\nYou guessed the word!\nYou survived!\n",
       'let_err': "Please enter a lowercase English letter",
       'c_err': "You should input a single letter"}
word_list = ['python', 'java', 'kotlin', 'javascript']
letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'


def change_w(lttr, wrd, xtra):
    ex_list = list(xtra)
    ind_lttr = -1
    for _ in range(wrd.count(lttr)):
        ind_lttr = wrd.find(lttr, ind_lttr + 1)
        ex_list[ind_lttr] = wrd[ind_lttr]
    return ''.join(ex_list)


def game():
    lives = 8
    word = word_list[randint(0, 3)]
    already_set = set()
    extra = '-' * len(word)
    while lives != 0:
        letter = input(f"\n{extra}\nInput a letter: ")
        if len(letter) != 1:
            print(msg['c_err'])
            continue
        if letter not in letters_lowercase:
            print(msg['let_err'])
            continue
        if letter in already_set:
            print(msg['no_imp'])
            continue
        elif letter in word:
            extra = change_w(letter, word, extra)
            already_set.add(letter)
            if extra == word:
                print(f"\n{extra}", msg['win'])
                return
        else:
            lives -= 1
            already_set.add(letter)
            print(msg['not_in'])
    print(msg['lost'])


def menu():
    while True:
        test_inp = input('Type "play" to play the game, "exit" to quit:')
        if test_inp == 'play':
            game()
        elif test_inp == 'exit':
            quit()
        else:
            continue


print(msg['hangman'])
menu()
