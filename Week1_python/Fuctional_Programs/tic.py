import random
global board
board = [1,2,3,4,5,6,7,8,9]
global currentPlayer 
currentPlayer = 'computer'

global win 
win = False
print('*******TIC_TAC_TOE GAME********')

def printBoard():
            print(board[:3])
            print(board[3:6])
            print(board[6:])

printBoard()
                
def choices(choice):
    switcher = {
        1 : 'Z',
        2 : 'X'
    }
    return switcher.get(choice,'nothing')


def selectchoise():

    choice=int(input('Enter Your Choice: 1 for Z and 2 for X '))
    if choice==1 or choice==2:
        choices(choice)
        selectchoise.player = choices(choice)
        if(choices(choice)== 'X'):
            selectchoise.computer = 'Z'
        else:
            selectchoise.computer = 'X'
        print('Player: ',selectchoise.player,' and Computer: ',selectchoise.computer)
        print('Player Plays First: ')
    else:
        print('Enter Correct Choice')

def wingame(win):
    print(win)
    if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
        win = True
        print(currentPlayer ,' won')
    elif board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8]:  
        win = True
        print(currentPlayer ,' won')
    elif board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:  
        win = True
        print(currentPlayer ,' won')
    
    return win           

def selectposition(board):

    place = int(input('Enter a Choise between 1 to 9 ::  '))
    place = place - 1
    if board[place] in range(1,10):
        board[place] = selectchoise.player
    else:
        print('Enter Correct Choise or see if the position is already filled')   
        selectposition(board)

def current(currentPlayer):
    if currentPlayer == 'player':
        currentPlayer = 'computer'
    elif currentPlayer == 'computer':
        currentPlayer = 'player'

    return currentPlayer    



def cpu(): 
    cpu.place = random.randint(0,9)
    if board[cpu.place] == 1 or board[cpu.place] == 2 or board[cpu.place] == 3 or board[cpu.place] == 4:
        board[cpu.place] = selectchoise.computer
    elif board[cpu.place] == 5 or board[cpu.place] == 6 or board[cpu.place] == 7 or board[cpu.place] == 8 or board[cpu.place == 9]:
        board[cpu.place] = selectchoise.computer
    elif board[cpu.place]=='X' or board[cpu.place]=='Z':
        return cpu()    


def playgame(): 
    Player = current(currentPlayer)
    w = wingame(win)
    print(Player)
    
    while w!=True:
        if Player == 'player':
            print("Player Playing........")
            selectposition(board)
            Player = 'computer'
            current(Player)
            printBoard()
            print
        elif Player == 'computer':
            print("Computer Playing........")
            cpu()
            Player = 'player'
            current(Player)
            printBoard()
            print
    return w        
    print(w)

   

    

def Game():
    selectchoise()
    playgame()

Game()
