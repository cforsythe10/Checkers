import copy
class Board:

    DEFAULT_BOARD = {
# Set player 1's side
    1: {'player': 0, 'king': False},
    2: {'player': 0, 'king': False},
    3: {'player': 0, 'king': False},
    4: {'player': 0, 'king': False},
    5: {'player': 0, 'king': False},
    6: {'player': 0, 'king': False},
    7: {'player': 0, 'king': False},
    8: {'player': 0, 'king': False},
    9: {'player': 0, 'king': False},
    10: {'player': 0, 'king': False},
    11: {'player': 0, 'king': False},
    12: {'player': 0, 'king': False},
    13: {},
    14: {},
    15: {},
    16: {},
    17: {},
    18: {},
    19: {},
    20: {},
    21: {'player': 1, 'king': False},
    22: {'player': 1, 'king': False},
    23: {'player': 1, 'king': False},
    24: {'player': 1, 'king': False},
    25: {'player': 1, 'king': False},
    26: {'player': 1, 'king': False},
    27: {'player': 1, 'king': False},
    28: {'player': 1, 'king': False},
    29: {'player': 1, 'king': False},
    30: {'player': 1, 'king': False},
    31: {'player': 1, 'king': False},
    32: {'player': 1, 'king': False}
}
    board_placement_converter = {
    32: 'G-1',
    31: 'E-1',
    30: 'C-1',
    29: 'A-1',

    28: 'H-2',
    27: 'F-2',
    26: 'D-2',
    25: 'B-2',

    24: 'G-3',
    23: 'E-3',
    22: 'C-3',
    21: 'A-3',

    20: 'H-4',
    19: 'F-4',
    18: 'D-4',
    17: 'B-4',

    16: 'G-5',
    15: 'E-5',
    14: 'C-5',
    13: 'A-5',

    12: 'H-6',
    11: 'F-6',
    10: 'D-6',
    9: 'B-6',

    8: 'G-7',
    7: 'E-7',
    6: 'C-7',
    5: 'A-7',

    4: 'H-8',
    3: 'F-8',
    2: 'D-8',
    1: 'B-8'
    }

    def __init__(self):
        self.board = {
        # Set player 1's side
            1: {'player': 0, 'king': False},
            2: {'player': 0, 'king': False},
            3: {'player': 0, 'king': False},
            4: {'player': 0, 'king': False},
            5: {'player': 0, 'king': False},
            6: {'player': 0, 'king': False},
            7: {'player': 0, 'king': False},
            8: {'player': 0, 'king': False},
            9: {'player': 0, 'king': False},
            10: {'player': 0, 'king': False},
            11: {'player': 0, 'king': False},
            12: {'player': 0, 'king': False},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {'player': 1, 'king': False},
            22: {'player': 1, 'king': False},
            23: {'player': 1, 'king': False},
            24: {'player': 1, 'king': False},
            25: {'player': 1, 'king': False},
            26: {'player': 1, 'king': False},
            27: {'player': 1, 'king': False},
            28: {'player': 1, 'king': False},
            29: {'player': 1, 'king': False},
            30: {'player': 1, 'king': False},
            31: {'player': 1, 'king': False},
            32: {'player': 1, 'king': False}
        }
        self.adjacents = {
        1: [5, 6],
        2: [6, 7],
        3: [7, 8],
        4: [8],
        5: [1, 9],
        6: [1, 2, 9, 10],
        7: [2, 3, 10, 11],
        8: [3, 4, 11, 12],
        9: [5, 6, 13, 14],
        10: [6, 7, 14, 15],
        11: [7, 8, 15, 16],
        12: [8, 16],
        13: [9, 17],
        14: [9, 10, 17, 18],
        15: [10, 11, 18, 19],
        16: [11, 12, 19, 20],
        17: [13, 14, 21, 22],
        18: [14, 15, 22, 23],
        19: [15, 16, 23, 24],
        20: [16, 24],
        21: [17, 25],
        22: [17, 18, 25, 26],
        23: [18, 19, 26, 27],
        24: [19, 20, 27, 28],
        25: [21, 22, 29, 20],
        26: [22, 23, 30, 31],
        27: [23, 24, 31, 32],
        28: [24, 32],
        29: [25],
        30: [25, 26],
        31: [26, 27],
        32: [27, 28],
        }
        self.jumped = False
        self.last_dir = 0
        self.message = ''
        self.read_message = False
        self.piece_count = {0: 12, 1: 12}

    def reset_board(self):
        self.board = copy.deepcopy(self.DEFAULT_BOARD)

    def get_board(self):
        return self.board

    def get_message(self):
        if self.read_message:
            self.read_message = False
            return self.message
        else:
            return ''

    def set_board(self, board):
        self.board = board

    def check_move(self, move_from, move_to, player_turn):
        diff = move_to -  move_from
        if not self.board[move_from]:
            return False
        elif self.board[move_from]['player'] != player_turn:
            self.message = 'You cannot move piece {}'.format(self.board_placement_converter[move_from])
            self.read_message = True
            return False
        mf = self.board[move_from]

        direction = 0
        if mf['king'] == True:
            direction = 2
        elif mf['player'] == 0:
            direction = 0
        else:
            direction = 1

        if diff < 0:
            self.last_dir = 1
        else:
            self.last_dir = 0

        if self.board[move_to]: # Check to see if there is a piece there already
            self.message = 'Cannot move to {} - there is a piece there'.format(self.board_placement_converter[move_to])
            self.read_message = True
            return False
        else:
            if move_to in self.adjacents[move_from]:
                if direction == 0 and diff <= 0: # Non-kinged white pieces can only travel upwards in number
                    self.message = 'Cannot move {} in that direction'.format(self.board_placement_converter[move_from])
                    self.read_message = True
                    return False
                elif direction == 1 and diff >= 0: # Non-kinged black piece can only travel downwards in number
                    self.message = 'Cannot move {} in that direction'.format(self.board_placement_converter[move_from])
                    self.read_message = True
                    return False
                else: # Kings can go anywhere
                    return True
            else:
                s1 = set(self.adjacents[move_from])
                s2 = set(self.adjacents[move_to])

                # Check if the move is legal -- i.e, can't jump 3 spaces
                common = list(s1 & s2)

                if common:
                    c = common[0]
                    # If there is a piece in that position
                    if self.board[c]:
                        # if the piece belongs to the other player
                        if self.board[c]['player'] != mf['player']:
                            self.piece_count[self.board[c]['player']] -= 1
                            self.board[c] = {}
                            print('Piece {} moved to {}, capturing {}'.format(move_from, move_to, c))
                            self.jumped = True
                            return True
                        else:
                            self.message = 'You cannot jump over your piece!'
                            self.read_message = True
                            return False
                    else:
                        self.message = 'You cannot move that many spaces without a valid jump!'
                        self.read_message = True
                        return False
                else:
                    self.message = 'Stop it! You cannot do that!'
                    self.read_message = True
                    return False

    def get_adjacent_in_direction(self, position):
        if (self.last_dir == 0):
            return [x for x in self.adjacents[position] if x > position]
        else:
            return [x for x in self.adjacents[position] if x < position]

    def find_jump(self, position, player_turn):
        if self.board[position]:
            if self.board[position]['player'] != player_turn:
                return []
        else:
            return []

        adj = self.get_adjacent_in_direction(position)
        hostiles = []
        moves = []
        for p in adj:
            if self.board[p]:
                if self.board[p]['player'] != player_turn:
                    if hostiles:
                        hostiles.append(p)
                    else:
                        hostiles = [p]

        for p in hostiles:
            h_adj = self.get_adjacent_in_direction(p)
            for pot_jump_spot in h_adj:
                if not self.board[pot_jump_spot]:
                    if moves:
                        moves.append(pot_jump_spot)
                    else:
                        moves = [pot_jump_spot]

        return moves

    def check_capture(self, player_turn):
        for key in list(self.board.keys()):
            x = self.find_jump(key, player_turn)
            if x:
                return True
        return False

    def move_piece(self, move_from, move_to, player_turn = 1):
        diff = move_to -  move_from
        # t = self.check_move(move_from, move_to)

        if self.check_move(move_from, move_to, player_turn):
            self.board[move_to] = self.board[move_from]
            self.board[move_from] = {}
            if move_to in [1, 2, 3, 4, 29, 30, 31, 32]:
                self.board[move_to]['king'] = True

            print('Moved: {} to {}'.format(self.board_placement_converter[move_from], self.board_placement_converter[move_to]))
            return True
            # for key in self.board.keys():
            #     print '{}: {}'.format(key, self.board[key])

            # print ' '
        else:
            self.message = 'Invalid move: From {} to {}'.format(self.board_placement_converter[move_from], self.board_placement_converter[move_to])
            self.read_message = True
            return False


if __name__ == '__main__':
    x = Board()
    x.move_piece(21, 17)
    x.move_piece(24, 20)
    x.move_piece(9, 13, 0)
    x.move_piece(22, 18),
    x.move_piece(27, 24)
    x.move_piece(31, 27)
    x.move_piece(25, 21)
    x.move_piece(29, 25)
    x.move_piece(13, 22, 0)
    # x.move_piece(21, 17)
    # x.move_piece(17, 14)
    # x.move_piece(22, 18)
    # x.move_piece(26, 22)
    # x.move_piece(10, 17, 0)
    # x.move_piece(23, 19)
    # x.move_piece(27, 23)
    # x.move_piece(31, 27)
    # x.move_piece(17, 26,  0)
    # x.move_piece(26, 31,  0)
    # x.move_piece(30, 26)
    # x.move_piece(31, 22,  0)

    # x.move_piece(9, 13)
    # x.move_piece(13, 17)
    # x.move_piece(22, 13)
    # x.move_piece(11, 16)
