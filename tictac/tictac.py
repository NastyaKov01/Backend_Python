"""Tic-tac-toe game realisation"""

from enum import Enum


class Players(Enum):
    """Players ids"""
    Player1 = 1
    Player2 = 2


class WrongInp(Exception):
    """New exception class for invalid user input:
        invalid data format"""


class Occupied(Exception):
    """New exception class for invalid user input:
        position is occupied"""


class TicTacGame:
    """Simple tic-tac-toe game"""

    def __init__(self):
        """Initialization"""

        self.board = [['_' for i in range(3)] for k in range(3)]
        self.pos_coords = [0, 0]
        self.correct_inp = False
        self.occupied_num = 0

    def show_board(self):
        """Printing th game board"""

        print()
        for i in self.board:
            print(*i)
        print()

    def validate_input(self, pos):
        """Input validation"""

        cur_inp = pos.split(',')
        if len(cur_inp) != 2:
            raise WrongInp
        if cur_inp[0].isdigit() is False or cur_inp[1].isdigit() is False:
            raise WrongInp
        if int(cur_inp[0]) > 2 or int(cur_inp[1]) > 2:
            raise WrongInp
        if self.board[int(cur_inp[0])][int(cur_inp[1])] != '_':
            raise Occupied
        self.correct_inp = True
        self.pos_coords[0] = int(cur_inp[0])
        self.pos_coords[1] = int(cur_inp[1])

    def read_coords(self):
        """Coordinates input"""

        while self.correct_inp is False:
            pos = input()
            try:
                self.validate_input(pos)
            except WrongInp:
                print("Invalid input")
                print("The position coordinates should be integers without a space: i,j")
                print("(i = 0,1,2; j = 0,1,2)")
            except Occupied:
                print("Invalid input")
                print("This position is occupied")

    def play_game(self):
        """Main method: playing"""

        order = Players.Player1
        while self.check_winner(self.board) is False:
            if self.occupied_num == 9 and self.check_winner(self.board) is False:
                return "It is a draw!"
            self.read_coords()
            if order == Players.Player1:
                self.board[self.pos_coords[0]][self.pos_coords[1]] = 'x'
                order = Players.Player2
                self.occupied_num += 1
            elif order == Players.Player2:
                self.board[self.pos_coords[0]][self.pos_coords[1]] = 'o'
                order = Players.Player1
                self.occupied_num += 1
            self.show_board()
            self.correct_inp = False
        #It's Player1's move, but the game finished.
        #It means that Player2 made the previous move and he is the winner.
        if order == Players.Player1:
            return "Player 2 won the game!"
        return "Player 1 won the game!"

    def start_game(self):
        """Starting point"""

        print("Hello! Let's play!")
        self.show_board()
        print("Enter positions of your symbols one by one")
        print("The upper left corner is position (0,0)")
        print("The first Player plays with crosses")
        print(self.play_game())

    @staticmethod
    def check_winner(resboard):
        """Result is checked"""

        for i in range(3):
            #rows checked
            if resboard[i][0] == resboard[i][1] and resboard[i][1] == resboard[i][2]:
                if resboard[i][0] != '_':
                    return True
            #columns checked
            if resboard[0][i] == resboard[1][i] and resboard[1][i] == resboard[2][i]:
                if resboard[0][i] != '_':
                    return True
        #main diagonal checked
        if resboard[0][0] == resboard[1][1] and resboard[1][1] == resboard[2][2]:
            if resboard[0][0] != '_':
                return True
        #second diagonal checked
        if resboard[0][2] == resboard[1][1] and resboard[1][1] == resboard[2][0]:
            if resboard[0][2] != '_':
                return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
