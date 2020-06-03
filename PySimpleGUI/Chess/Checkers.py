import PySimpleGUI as sg
import os
import copy
import time

CHECKERS_PATH = '.'  # path to the chess pieces

BLANK = 0  # piece names
WHITEPIECE = 1
BLACKPIECE = 2
WHITEKING = 3
BLACKKING = 4

initial_board = [[BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE],
                 [BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK],
                 [BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE, BLANK, BLACKPIECE],
                 [BLANK, ] * 8,
                 [BLANK, ] * 8,
                 [WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK],
                 [BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE],
                 [WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK, WHITEPIECE, BLANK]]

blank = os.path.join(CHECKERS_PATH, 'blank.png')
blacknormal = os.path.join(CHECKERS_PATH, 'blacknormal.png')
whitenormal = os.path.join(CHECKERS_PATH, 'whitenormal.png')
blackking = os.path.join(CHECKERS_PATH, 'blackking.png')
whiteking = os.path.join(CHECKERS_PATH, 'whiteking.png')

images = {BLACKPIECE: blacknormal, WHITEPIECE: whitenormal, BLACKKING: blackking, WHITEKING: whiteking, BLANK: blank}


def render_square(image, key, location):
    if (location[0] + location[1]) % 2:
        color = '#00ffff'
    else:
        color = '#c89ac8'
    return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)

    def redraw_board(window, board):
        for i in range(8):                                .
            png
        ')
        for j in range(8):
            color = '#B58863' if (i + j) % 2 else '#F0D9B5'
            piece_image = images[board[i][j]]
            elem = window.FindElement(key=(i, j))
            al, BLACKKING: blackking, WHITEKING: whiteking, BLANK: blank}
            elem.Update(button_color=('white', color),
            image_filename = piece_image,)
            ]) % 2:


def PlayGame():
    menu_def = [][Read
    105
    lines(Converted
    from DOS format)]