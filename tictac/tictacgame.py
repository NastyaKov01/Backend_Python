class WrongInp(Exception):
    pass


class Occupied(Exception):
    pass


class TicTacGame:
    
    def __init__(self):
        self.board = [['_' for i in range(3)] for k in range(3)]
        self.pos_coords = [0,0]
        self.correct_inp = False

    def show_board(self):
        print()
        for i in self.board:
            print(*i)
        print()

    def validate_input(self, pos):
        cur_inp = pos.split(',')
        if len(cur_inp) != 2:
            raise WrongInp
        elif cur_inp[0].isdigit() == False or cur_inp[1].isdigit() == False:
            raise WrongInp
        elif int(cur_inp[0]) > 2 or int(cur_inp[1]) > 2:
            raise WrongInp
        elif self.board[int(cur_inp[0])][int(cur_inp[1])] != '_':
            raise Occupied
        else:
            self.correct_inp = True
            self.pos_coords[0] = int(cur_inp[0])
            self.pos_coords[1] = int(cur_inp[1])
        
    def read_coords(self):
        while(self.correct_inp == False):
            pos = input()
            try:
                self.validate_input(pos)
            except WrongInp:
                print("Invalid input")
                print("The position coordinates should look like i,j without a space")
                print("(i = 0,1,2; j = 0,1,2)")
            except Occupied:
                print("Invalid input")
                print("This position is occupied")

    def play_game(self):
        order = 1
        while self.check_winner() == False:
            self.read_coords()
            if order == 1:
                self.board[self.pos_coords[0]][self.pos_coords[1]] = 'x'
                order = 2
            elif order == 2:
                self.board[self.pos_coords[0]][self.pos_coords[1]] = 'o'
                order = 1
            self.show_board()
            self.correct_inp = False
            full =True
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        full = False
            if full == True and self.check_winner() == False:
                print("It is a draw!")
                return
        if order == 1:
            print("Player 2 won the game!")
        else:
            print("Player 1 won the game!")

    def start_game(self):
        print("Hello! Let's play!")
        self.show_board()
        print("Enter positions of your symbols one by one")
        print("The upper left corner is position (0,0)")
        print("The first Player plays with crosses")
        self.play_game()

    def check_winner(self):
        win = False
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != '_':
                    win = True
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                if self.board[0][i] != '_':
                    win = True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != '_':
                win = True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] != '_':
                win = True
        return win


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()    
