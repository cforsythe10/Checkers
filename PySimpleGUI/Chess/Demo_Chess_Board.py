import PySimpleGUI as sg
import os
import chess
import chess.pgn
import copy
import time

button_names = ('close', 'cookbook', 'cpu', 'github', 'pysimplegui', 'run', 'storage', 'timer')

CHESS_PATH = '.'        # path to the chess pieces

BLANK = 0               # piece names
WHITEPIECE = 1
BLACKPIECE = 2
WHITEKING = 3
BLACKKING = 4

initial_board = [[BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE],
                [BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK],
                [BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE],
                [BLANK,]*8,
                [BLANK,]*8,
                [WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK],
                [BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE],
                [WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK]]

blank = os.path.join(CHESS_PATH, 'blank.png')
blacknormal = os.path.join(CHESS_PATH, 'blacknormal.png')
whitenormal = os.path.join(CHESS_PATH, 'whitenormal.png')
blackking = os.path.join(CHESS_PATH, 'blackking.png')
whiteking = os.path.join(CHESS_PATH, 'whiteking.png')

images = {BLACKPIECE: blacknormal, WHITEPIECE: whitenormal, BLACKKING: blackking, WHITEKING: whiteking, BLANK: blank}

def render_square(image, key, location):
    if (location[0] + location[1]) % 2:
        color =  '#00ffff'
    else:
        color = '#c89ac8'
    return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)

def redraw_board(window, board):
    for i in range(8):
        for j in range(8):
            color = '#B58863' if (i+j) % 2 else '#F0D9B5'
            piece_image = images[board[i][j]]
            elem = window.FindElement(key=(i,j))
            elem.Update(button_color = ('white', color),
                        image_filename=piece_image,)

def PlayGame():

    menu_def = []

    # sg.SetOptions(margins=(0,0))
    sg.ChangeLookAndFeel('GreenTan')
    # create initial board setup
    board = copy.deepcopy(initial_board)
    # the main board display layout
    board_layout = [[sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh']]
    # loop though board and create buttons with images
    for i in range(8):
        row = [sg.T(str(8-i)+'   ', font='Any 13')]
        for j in range(8):
            piece_image = images[board[i][j]]
            row.append(render_square(piece_image, key=(i,j), location=(i,j)))
        row.append(sg.T(str(8-i)+'   ', font='Any 13'))
        board_layout.append(row)
    # add the labels across bottom of board
    board_layout.append([sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh'])

    # setup the controls on the right side of screen
    openings = ('Any', 'Defense', 'Attack', 'Trap', 'Gambit','Counter', 'Sicillian', 'English','French', 'Queen\'s openings', 'King\'s Openings','Indian Openings')

    board_controls = [[sg.RButton('Forfeit Game', key='Open PGN File')],]

    # layouts for the tabs
    controls_layout = [[sg.Text('Performance Parameters', font='_ 20')],
                       [sg.T('Put stuff like AI engine tuning parms on this tab')]]

    statistics_layout = [[sg.Text('Statistics', font=('_ 20'))],
                         [sg.T('Game statistics go here?')]]

    board_tab = [[sg.Column(board_layout)]]

    # the main window layout
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.TabGroup([[sg.Tab('Game',board_tab)]], title_color='red'),
               sg.Column(board_controls)],
              [sg.Text('Click anywhere on board for next move', font='_ 14')]]

    window = sg.Window('Chess', default_button_element_size=(12,1), auto_size_buttons=False, icon='kingb.ico').Layout(layout)

    # ---===--- Loop taking in user input --- #
    i = 0
    while True:
        button, value = window.Read()
        print(button, value)
        if button in (None, 'Exit'):
            break
        if type(button) is tuple:

            window.FindElement('_movelist_').Update(value='{}   {}\n'.format(i+1, str(move)), append=True)
            row, col =  button[0], button[1]
            piece = board[row][col]         # get the move-from piece
            button = window.FindElement(key=(row,col))
            for x in range(3):
                button.Update(button_color = ('white' , 'red' if x % 2 else 'white'))
                window.Refresh()
                time.sleep(.05)
            board[row][col] = BLANK         # place blank where piece was
            row, col = move_to // 8, move_to % 8  # compute move-to square
            board[row][col] = piece         # place piece in the move-to square
            redraw_board(window, board)
            i += 1

PlayGame()