import PySimpleGUI as sg
import os
import copy
import time
import sys
import pdb
from board import Board
sys.path.insert(1, './src/network')
from server import Server
from network import Network
import json
import warnings

warnings.filterwarnings('ignore')

class CheckersGUI:

    CHECKERS_PATH = './img/'        # path to the chess pieces

    LOC_CONV = {
    (7, 6): 32,
    (7, 4): 31,
    (7, 2): 30,
    (7, 0): 29,

    (6, 7): 28,
    (6, 5): 27,
    (6, 3): 26,
    (6, 1): 25,

    (5, 6): 24,
    (5, 4): 23,
    (5, 2): 22,
    (5, 0): 21,

    (4, 7): 20,
    (4, 5): 19,
    (4, 3): 18,
    (4, 1): 17,

    (3, 6): 16,
    (3, 4): 15,
    (3, 2): 14,
    (3, 0): 13,

    (2, 7): 12,
    (2, 5): 11,
    (2, 3): 10,
    (2, 1): 9,

    (1, 6): 8,
    (1, 4): 7,
    (1, 2): 6,
    (1, 0): 5,

    (0, 7): 4,
    (0, 5): 3,
    (0, 3): 2,
    (0, 1): 1
    }

    BLANK = 0               # piece names
    WHITEPIECE = 1
    BLACKPIECE = 2
    WHITEKING = 3
    BLACKKING = 4

    blank = os.path.join(CHECKERS_PATH, 'blank.png')
    blacknormal = os.path.join(CHECKERS_PATH, 'blacknormal.png')
    whitenormal = os.path.join(CHECKERS_PATH, 'whitenormal.png')
    blackking = os.path.join(CHECKERS_PATH, 'blackking.png')
    whiteking = os.path.join(CHECKERS_PATH, 'whiteking.png')

    images = {BLACKPIECE: blacknormal, WHITEPIECE: whitenormal, BLACKKING: blackking, WHITEKING: whiteking, BLANK: blank}

    def __init__(self, board):
        self.board = board
        self.player = -1
        self.turn = False
        self.client = None

    # player ==1 - white piece
    # player == 0 - black piece
    def convert_board(self):
        bd = None
        ret_board = []
        bd = self.board.board

        rows = {1: [self.BLANK], 2: [], 3: [self.BLANK], 4: [], 5: [self.BLANK], 6: [], 7: [self.BLANK], 8: []}
        for i in range(1, 33):
            piece_info = bd[i]
            row = 0
            piece = None
            if piece_info:
                if piece_info['player'] == 1: # White piece
                    if piece_info['king'] == True:
                        piece = self.WHITEKING
                    else:
                        piece = self.WHITEPIECE
                else:
                    if piece_info['king'] == True:
                        piece = self.BLACKKING
                    else:
                        piece = self.BLACKPIECE
            else:
                piece = self.BLANK

            if i <= 4:
                rows[1].append(piece)
                if len(rows[1]) < 8:
                    rows[1].append(self.BLANK)
            elif i <= 8:
                if rows[2]:
                    rows[2].append(piece)
                    rows[2].append(self.BLANK)
                else:
                    rows[2] = [piece, self.BLANK]
            elif i <= 12:
                rows[3].append(piece)
                if len(rows[3]) < 8:
                    rows[3].append(self.BLANK)
            elif i <= 16:
                if rows[4]:
                    rows[4].append(piece)
                    rows[4].append(self.BLANK)
                else:
                    rows[4] = [piece, self.BLANK]
            elif i <= 20:
                rows[5].append(piece)
                if len(rows[5]) < 8:
                    rows[5].append(self.BLANK)
            elif i <= 24:
                if rows[6]:
                    rows[6].append(piece)
                    rows[6].append(self.BLANK)
                else:
                    rows[6] = [piece, self.BLANK]
            elif i <= 28:
                rows[7].append(piece)
                if len(rows[7]) < 8:
                    rows[7].append(self.BLANK)
            elif i <= 32:
                if rows[8]:
                    rows[8].append(piece)
                    rows[8].append(self.BLANK)
                else:
                    rows[8] = [piece, self.BLANK]

        for row in rows.keys():
            if ret_board:
                ret_board.append(rows[row])
            else:
                ret_board = [rows[row]]

        return ret_board

    def render_square(self, image, key, location):
        if (location[0] + location[1]) % 2:
            color =  '#00ffff'
        else:
            color = '#c89ac8'
        return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)

    def redraw_board(self, window, board):
        for i in range(8):
            for j in range(8):
                color = '#B58863' if (i+j) % 2 else '#F0D9B5'
                piece_image = self.images[board[i][j]]
                elem = window.FindElement(key=(i,j))
                elem.Update(button_color = ('white', color),
                            image_filename=piece_image,)

    def convert_raw_board(self, board):
        raw_dict = json.loads(board)
        new_board = {int(x):y for x,y in raw_dict.items()}
        print('Convert board: ', new_board)
        print('Type: ', type(new_board))
        return new_board

    def server_loop(self, window):
        i = 0
        print(self.client.__class__.__name__)
        sg.Popup('Your pieces start in rows 6-8 (Black). You go second')
        while True:
            took_turn = False
            board = self.convert_board()
            self.redraw_board(window, board)
            window.Read(timeout=500)
            print('Top of Server')
            raw_board = self.client.receive()
            if raw_board == 'YOU LOST!!!':
                print('YOU LOST!!!')
                sg.Popup('YOU LOST!!!')
                sys.exit(0)
            elif raw_board == 'Forfeit':
                print('WINNER BY FORFEIT!')
                sg.Popup('WINNER BY FORFEIT!')
                time.sleep(5)
                sys.exit(0)

            print('Raw board: ', raw_board)
            if raw_board:
                board = self.convert_raw_board(raw_board)
                print('\n', board, '\n')
                self.board.set_board(board)
            board = self.convert_board()
            self.redraw_board(window, board)

            sg.PopupNoWait('Player Turn: Black')
            while not took_turn:
                button1, value1 = window.Read()
                if button1 in (None, 'Exit'):
                    self.client.send_text('Forfeit')
                    window.close()
                    sys.exit(0)
                if button1  == 'Forfeit Game':
                    self.client.send_text('Forfeit')
                    print('Forfeited')
                    sg.Popup('You Forfeited!')
                    time.sleep(5)
                    sys.exit(0)
                elif button1 in self.LOC_CONV.keys():
                    button2, value2 = window.Read()

                    if button2  == 'Forfeit Game':
                        self.client.send_text('Forfeit')
                        print('Forfeited')
                        sg.Popup('You Forfeited')
                        time.sleep(5)
                        sys.exit(0)

                    if button2 != button1:
                        if button2 in self.LOC_CONV.keys():
                            move_from = self.LOC_CONV[button1]
                            move_to = self.LOC_CONV[button2]
                            took_turn = self.board.move_piece(move_from, move_to, self.player)

                            message = self.board.get_message()
                            if message:
                                sg.PopupNoWait('Alert', message)

                else:
                    sg.Popup('Please select two different pieces!')
            if self.board.piece_count[1] == 0:
                print('VICTORY!!!!')
                self.client.send_text('YOU LOST!!!')
                sg.Popup('VICTORY!!!!')
                time.sleep(5)
                sys.exit(0)
            board = self.convert_board()
            self.redraw_board(window, board)
            window.Read(timeout=500)
            # time.sleep(3)
            self.client.send(self.board.get_board())

    def client_loop(self, window):
        i = 0
        print(self.client.__class__.__name__)
        sg.Popup('Your pieces start in rows 1-3 (White). You go first!')
        while True:
            took_turn = False
            while not took_turn:
                sg.PopupNoWait('Player Turn: White')
                button1, value1 = window.Read()
                if button1 in (None, 'Exit'):
                    self.client.send_text('Forfeit')
                    window.close()
                    sys.exit(0)
                if button1  == 'Forfeit Game':
                    self.client.send_text('Forfeit')
                    print('Forfeited')
                    sg.Popup('You Forfeited!')
                    time.sleep(5)
                    sys.exit(0)
                elif button1 in self.LOC_CONV.keys():
                    button2, value2 = window.Read()

                    if button2  == 'Forfeit Game':
                        self.client.send_text('Forfeit')
                        print('Forfeited')
                        sg.Popup('You Forfeited!')
                        time.sleep(5)
                        sys.exit(0)

                    if button2 != button1:
                        if button2 in self.LOC_CONV.keys():
                            move_from = self.LOC_CONV[button1]
                            move_to = self.LOC_CONV[button2]
                            took_turn = self.board.move_piece(move_from, move_to, self.player)

                            message = self.board.get_message()
                            if message:
                                sg.PopupNoWait('Alert', message)

                else:
                    sg.Popup('Please select two different pieces!')
            if self.board.piece_count[0] == 0:
                print('VICTORY!!!!')
                self.client.send_text('YOU LOST!!!')
                sg.Popup('VICTORY!!!!')
                time.sleep(5)
                window.close()
                sys.exit(0)
            board = self.convert_board()
            self.redraw_board(window, board)
            window.Read(timeout=500)
            # time.sleep(1)
            raw_board = self.client.send(self.board.get_board())
            if raw_board:
                if raw_board == 'YOU LOST!!!':
                    print('YOU LOST!!!')
                    sg.Popup('YOU LOST!!!')
                    time.sleep(5)
                    sys.exit(0)
                elif raw_board == 'Forfeit':
                    print('WINNER BY FORFEIT!')
                    sg.Popup('WINNER BY FORFEIT')
                    time.sleep(5)
                    sys.exit(0)
                board = self.convert_raw_board(raw_board)
                self.board.set_board(board)
                board = self.convert_board()
                self.redraw_board(window, board)


    def PlayGame(self):
        menu_def = []
        # self.DisplayMain()
        # self.start_game()

        # sg.SetOptions(margins=(0,0))
        sg.ChangeLookAndFeel('GreenTan')
        # create initial board setup
        # board = copy.deepcopy(initial_board)
        board = self.convert_board()
        # the main board display layout
        board_layout = [[sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh']]
        # loop though board and create buttons with images
        for i in range(8):
            row = [sg.T(str(8-i)+'   ', font='Any 13')]
            for j in range(8):
                piece_image = self.images[board[i][j]]
                row.append(self.render_square(piece_image, key=(i,j), location=(i,j)))
            row.append(sg.T(str(8-i)+'   ', font='Any 13'))
            board_layout.append(row)
        # add the labels across bottom of board
        board_layout.append([sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh'])


       # forfeit button
        board_controls = [
        [sg.RButton('Forfeit Game')]
        ]

        board_tab = [[sg.Column(board_layout)]]

        # the main window layout
        layout = [
                [sg.Menu(menu_def, tearoff=False)],
                [sg.Column(board_layout), sg.Column(board_controls)],
                [sg.Text('Your Pieces: ', key='Your Pieces', font='_ 14')]
                ]

        window = sg.Window('Checkers', default_button_element_size=(12,1), auto_size_buttons=False, icon='kingb.ico').Layout(layout)

        # ---===--- Loop taking in user input --- #
        if self.client.__class__.__name__ == 'Network':

            self.client_loop(window)
        else:
            self.server_loop(window)

    def start_game():
        self.DisplayMain()

    def DisplayAbout(self):
        sg.ChangeLookAndFeel('GreenTan')

        about_controls = [[sg.RButton('Back to Main', key='Main')]]

        layout = [[sg.Text('This game was made by Justin Roszko, Sam Platek, Chris Forsythe, and the other Robert Roche.\n\nInstructions for this game can be found at https://www.fgbradleys.com/rules/Checkers.pdf')],
                  [sg.Column(about_controls)]]

        window = sg.Window('About', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()
            print(button, value)

            if button in (None, 'Exit'):
                quit()

            if button == 'Main':
                window.Close()
                Windows.DisplayMain(self)

    def DisplayHostOrClient(self):

        sg.ChangeLookAndFeel('GreenTan')

        hostOrClient_controls = [[sg.RButton('Host', key='Host')],
                                 [sg.RButton('Client', key='Client')]]

        layout = [[sg.Column(hostOrClient_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Host':
                self.player = 0
                window.Close()
                self.DisplayHost()
                break

            if button == 'Client':
                self.player = 1
                window.Close()
                self.DisplayClient()
                break

    def DisplayHost(self):

        sg.ChangeLookAndFeel('GreenTan')
        client = Server()
        ip = client.get_ip()
        # client.run_server()
        self.client = client

        layout = [[sg.Text(ip)],]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        button, value = window.Read(timeout=500)
        self.client.run_server(ip)
        window.close()

    def DisplayClient(self):

        sg.ChangeLookAndFeel('GreenTan')

        # client = Network()
        # self.client = client

        hostOrClient_controls = [[sg.RButton('Join', key='Join')]]

        layout = [[sg.InputText(default_text='Put host key here', key='Host Input')],
            [sg.Column(hostOrClient_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Join':
                hostKey = value['Host Input']
                client = Network(hostKey)
                self.client = client

                window.Close()
                break
                # self.DisplayWinner(self, 'Everybody')

    def DisplayMain(self):

        sg.ChangeLookAndFeel('GreenTan')

        main_controls = [[sg.RButton('New Game', key='New Game')],
                     [sg.RButton('About', key='About')],
                     [sg.RButton('Exit', key='Quit')]]

        layout = [[sg.Column(main_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()
            print(button)

            if button in (None, 'Exit'):
                break

            if button == 'Quit':
                quit()

            if button == 'About':
                window.Close()
                self.DisplayAbout(self)
                break

            if button == 'New Game':
                window.Close()
                self.DisplayHostOrClient()
                break

    def DisplayWinner(self, winner):
        #send winner as a parameter to this

        sg.ChangeLookAndFeel('GreenTan')

        main_controls = [[sg.RButton('Rematch', key='Rematch')],
                     [sg.RButton('Quit', key='Quit')]]

        layout = [[sg.Text(winner + ' wins!')],
            [sg.Column(main_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Rematch':
                #confirm that other player also selects this and initialize new game, if other user does not confirm use below code
                #window.Close()
                #Windows.DisplayMain(self)
                quit()

            if button == 'Quit':
                window.Close()
                self.DisplayMain(self)


if __name__ == '__main__':
    # print('Will you be running the server side? (Y/N)')
    # i = input()

    # wh_or_bl = -1
    # if i == 'Y':
    #     client = Server()
    #     client.run_server()
    #     wh_or_bl = 0
    # else:
    #     client = Network()
    #     wh_or_bl = 1
    #pdb.set_trace()
    b = Board()
    x = CheckersGUI(b)
    x.DisplayMain()
    x.PlayGame()
    # x.PlayGame(client)
# x = convert_board()
