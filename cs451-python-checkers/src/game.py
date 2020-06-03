from src.board import Board
import PySimpleGUI as sg


class Game:

    def __init__(self):
        self.board = Board()
        self.player_turn = 0

    def start_turn(self):


    def reset_board(self):
        self.board.reset_board()

    def check_move(self, player_turn):
        # Not quite necessary if we don't need to know this exactly. move_piece calls this function in Board
        ## Get input from GUI,
        return self.board.check_move(move_from, move_to, player_turn)


    def check_capture(self, player_turn):
        return self.board.check_capture(player_turn)

    def move_piece(self, move_from, move_to, player_turn):
        self.board.move_piece()
