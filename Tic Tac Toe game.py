# # Tic Tac Toe game using Python without a graphical user interface (GUI)

body = ['_', '_', '_',
        '_', '_', '_',
        '_', '_', '_']
    
current_player = "X"
winner = None
no_winner = True

def tic_tac_toe_body(body):
    """
    Function to print the game board to the console.
    This function take the game board as a parameter.
    """
    print(body[0] + ' | ' + body[1] + ' | ' + body[2])
    print('----------')
    print(body[3] + ' | ' + body[4] + ' | ' + body[5])
    print('----------')
    print(body[6] + ' | ' + body[7] + ' | ' + body[8])

def playing(body):
    """
    Function to handle player moves.
    This function take the game board as a parameter.
    """
    global current_player
    try:
        play = input(f"play {current_player} now, please enter the index of place")
        play = int(play)
        if play >= 1 and play <= 9 and body[play-1] == '_':
            body[play-1] = current_player
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Oops, Your game is wrong")
    except:
        print("Oops, Enter the index of place only")

def check_winner(body):
    """
    Function to check for a win.
    This function take the game board as a parameter.
    """
    global winner
    global no_winner
    # Horizontal
    if body[0] == body[1] == body[2] and body[0] != '_':
        winner = body[0]
    elif body[3] == body[4] == body[5] and body[3] != '_':
        winner = body[3]
    elif body[6] == body[7] == body[8] and body[6] != '_':
        winner = body[6]
    # Vertical
    elif body[0] == body[3] == body[6] and body[0] != '_':
        winner = body[0]
    elif body[1] == body[4] == body[7] and body[1] != '_':
        winner = body[1]
    elif body[2] == body[5] == body[8] and body[2] != '_':
        winner = body[2]
    # Diameter
    elif body[0] == body[4] == body[8] and body[0] != '_':
        winner = body[0]
    elif body[2] == body[4] == body[6] and body[2] != '_':
        winner = body[2]
    # finally
    if winner != None:
        print(f'player {winner} is winner')
        no_winner = False
        tic_tac_toe_body(body)

def check_no_winner(body):
    """
    Function to check for a tie.
    This function take the game board as a parameter,
    and check if every square on the board has been filled.
    """
    global no_winner
    count = 0
    for x in body:
        if x != '_':
            count += 1
    if count == 9:
        print("no winner")
        no_winner = False
        tic_tac_toe_body(body)

# main game loop.
while no_winner:
    tic_tac_toe_body(body)
    playing(body)
    check_winner(body)
    check_no_winner(body)

