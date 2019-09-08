from random import choice

from solver import boggle_solver


class Cube:

    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        
    def __str__(self):
        return "{}".format(self.letter)


class Word:

    def __init__(self, cube=None):
        self.cube = cube
        self.next = None

    def get_cube(self):
        return self.cube

    def get_next(self):
        return self.next

    def is_cube_in(self, cube):
        if self.cube == cube:
            return True
        if self.next:
            return self.next.is_cube_in(cube)
        return False

    def add(self, cube):
        if self.next:
            if self.cube == cube:
                return False
            return self.next.add(cube)
        self.next = Word(cube)
        return True


class Default:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPRSTUVWXYZ"

    def generate_board(self):
        return [[choice(self.letters) for i in range(4)] for j in range(4)]


class Boggle:

    def __init__(self, generator=Default):
        letters = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
        self.generator = generator()
        self.board = self.generator.generate_board()

    def __str__(self):
        ret = ""
        "\n".join([" ".join(letters) for letters in self.board])
        return ret

    def get_board_list(self):
        return [[self.board[i, j] for i in range(4)] for j in range(4)]

    def count_max_points(self, dictionary="slowa.txt"):
        return boggle_solver(dictionary, self.board)
