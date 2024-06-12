def display(numpad):
    
    for i in range(1,4):
        print(numpad[(i*3)-3]+'|'+numpad[(i*3)-2]+'|'+numpad[(i*3)-1]+'|')
        print('------')

def choice_position(choices):
    
    position = 'wrong'
    
    while position not in str(list(range(1,10))) or position in choices:
        position = input('Pick a position: ')
        if position not in str(list(range(1,10))) or position in choices:
            print('Pick a valid position!!! ')
    
    choices.append(position)
    
    return int(position), choices

def update(numpad, position, flag ):
    
    numpad[position - 1] = flag
    
    return numpad

def game_win(numpad, marker, cont):

    if numpad[0] == marker and numpad[4] == marker and numpad[8] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    elif numpad[2] == marker and numpad[4] == marker and numpad[6] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    
    elif numpad[0] == marker and numpad[1] == marker and numpad[2] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    elif numpad[3] == marker and numpad[4] == marker and numpad[5] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    elif numpad[6] == marker and numpad[7] == marker and numpad[8] == marker:
        print(f"WINNER PLAYER: {marker}")
    
    elif numpad[0] == marker and numpad[3] == marker and numpad[6] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    elif numpad[1] == marker and numpad[4] == marker and numpad[7] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False
    elif numpad[2] == marker and numpad[5] == marker and numpad[8] == marker:
        print(f"WINNER PLAYER: {marker}")
        return False 
    elif cont == 9:
        print('DRAW!!!')
    
    return True

def gameon_choice():
    
    choice = 'wrong'
    
    while choice.upper() not in ['Y','N']:
        choice = input('Do you want to continue? [y/n]...')
        
        if choice.upper() not in ['Y','N']:
            print('Pick a correct answer!!!')
    
    if choice.upper() == 'Y':
        return True
    else:
        return False

#-------------------------------- ON GAME ----------------------------------
gameon = True

while gameon:

    numpad = [str(i) for i in range(1,10)]
    cont = 0
    choices = []
    win = True

    while cont < 9:

        display(numpad)
        position, choices = choice_position(choices)

        cont += 1

        if cont % 2 == 0:
            numpad = update(numpad, position, 'O')
            win = game_win(numpad, 'O', cont)
            marker = 'O'
        else:
            numpad = update(numpad, position, 'X')
            win = game_win(numpad, 'X', cont)
            marker = 'X'
        
        if not win:
            print('Winner: {}'.format(marker))
            display(numpad)
            break
        
    gameon = gameon_choice()