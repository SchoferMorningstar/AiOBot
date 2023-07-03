import random
def random_message(tab):
    a = 0
    b = len(tab) - 1
    rand = random.randint(a, b)
    message = tab[rand]
    return message

def kelvin_to_celsius(temp_kel):
    celsius = temp_kel - 237.15
    return celsius

def switch_turn(turn, players):
    if turn == players[0]:
        turn = players[1]
    else:
        turn = players[0]

    return turn

def switch_turn_sign(turn_sign):
    if turn_sign == "O":
        turn_sign = "X"
    else:
        turn_sign = "O"

    return turn_sign

def check_win(tab):
    if tab[0] == tab[1] == tab[2]:
        win = True
    elif tab[3] == tab[4] == tab[5]:
        win = True
    elif tab[6] == tab[7] == tab[8]:
        win = True
    elif tab[0] == tab[4] == tab[8]:
        win = True
    elif tab[2] == tab[4] == tab[6]:
        win = True
    elif tab[0] == tab[3] == tab[6]:
        win = True
    elif tab[1] == tab[4] == tab[7]:
        win = True
    elif tab[2] == tab[5] == tab[8]:
        win = True
    else:
        win = False

    return win

def board_generate(tab):
    message = f"```{tab[0]} | {tab[1]} | {tab[2]} \n{tab[3]} | {tab[4]} | {tab[5]} \n{tab[6]} | {tab[7]} | {tab[8]}```"
    return message

