from .solver import boggle_solver


class Cube:

    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        
    def __str__(self):
        return f"{self.letter}"


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


class Boggle:

    def __init__(self):
        letters = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
        self.board = [Cube(i//4, i % 4, letters[i]) for i in range(16)]

    def __str__(self):
        ret = ""
        for i in range(16):
            ret += str(self.board[i])
        return ret

    def get_board_list(self):
        return [[self.board[i+j].letter for i in range(4)] for j in range(4)]

    def count_max_points(self, dictionary="slowa.txt"):
        return boggle_solver(dictionary, self.board)
