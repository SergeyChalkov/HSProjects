def show_field():
    print("---------")
    print("| " + ' '.join([elem if elem else '_' for elem in field[:3]]) + " |")
    print("| " + ' '.join([elem if elem else '_' for elem in field[3:6]]) + " |")
    print("| " + ' '.join([elem if elem else '_' for elem in field[6:]]) + " |")
    print('---------')


def manage_turn(player):
    while True:
        turn = input("Enter the coordinates:").replace(' ', '')
        if not turn.isnumeric() or len(turn) != 2:
            print("You should enter numbers!")
        elif turn[0] not in {'1', '2', '3'} or turn[1] not in {'1', '2', '3'}:
            print("Coordinates should be from 1 to 3!")
        else:
            turn = ((int(turn[0]) - 1) * 3) + int(turn[1]) - 1
            if field[turn]:
                print("This cell is occupied! Choose another one!")
            else:
                field[turn] = player
                if field[0] or field[4] or field[8]:
                    analyze(player)
                break


def analyze(player):
    if [player, player, player] in ((field[:3]), (field[3:6]), (field[6:]),
           (field[::3]), (field[1::3]), (field[2::3]), (field[::4]), (field[2:7:2])):
        show_field()
        print(f'{player} wins')
        quit()
    else:
        return


def start_play():
    for tic_tac in 'XOXOXOXOX':
        show_field()
        manage_turn(tic_tac)
    else:
        show_field()
        print("Draw")
        quit()


field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
start_play()
