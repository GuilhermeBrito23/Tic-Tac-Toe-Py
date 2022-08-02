
from re import X


win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7, ]]

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def owin_game():
    check_list = []
    for item_list in win_list:
        
        for item in item_list:
            
            if board[item-1] == 'O':
                check_list.append(True)
            else:
                check_list.append(False)
                
        if all(check_list) == True:
            
            return True
        
        check_list = []
        
    return False

def xwin_game():
    check_list = []
    
    for item_list in win_list:
        
        for item in item_list:
            
            if board[item-1] == 'X':
                check_list.append(True)
            else:
                check_list.append(False)
                
        if all(check_list) == True:
            
            return True
        
        check_list = []
        
    return False


def show_board():
    print('{}|{}|{}'.format(board[0], board[1], board[2]))
    print('{}|{}|{}'.format(board[3], board[4], board[5]))
    print('{}|{}|{}'.format(board[6], board[7], board[8]))


print('############################')
print('#     TIC-TAC-TOE GAME     #')
print('############################')

player1 = ''
player2 = ''
while True:
    player1 = input('Player 1: you want to be X or O? ').upper()
    if player1 == 'X' or player1 == 'O':
        break

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
print('Player 2: Will be {}'.format(player2))
start = input('Who want to start?(X or O): ').upper()
count = 0
if start == 'X':
    count = 1
else:
    count = 2

xwin = False
owin = False
draw = False
while xwin == False and owin == False:
    if count % 2 == 0:
        start = 'O'
    else:
        start = 'X'
    show_board()
    place = int(input('select The number to place {} : '.format(start)))

    board[place-1] = start
    xwin = xwin_game()
    owin = owin_game()
    if player1 == 'X' and xwin == True:
        show_board()
        print('Player 1 Won!')
    if player1 == 'O' and owin == True:
        show_board()
        print('Player 1 Won!')
    if player2 == 'X' and xwin == True:
        show_board()
        print('Player 2 Won!')
    if player2 == 'O' and owin == True:
        show_board()
        print('Player 2 Won!')
    
    drawcheck = [True if i == 'O' or i == 'X' else False for i in board]
    draw = all(drawcheck)
    if draw == True:
        print('Draw Game!')
        break
             
    count += 1
