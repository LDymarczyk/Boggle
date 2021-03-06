from random import choice, randint

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
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def generate_letters(self, nslots):
        slots = self.generate_slots(nslots)
        new_letters = {}
        for slot in slots:
            new_letters[slot] = choice(self.letters)
        return new_letters

    def generate_board(self):
        return [[choice(self.letters) for i in range(4)] for j in range(4)]

    @staticmethod
    def generate_slots(nslots):
        points = []
        while len(points) < nslots:
            point = (randint(0, 3), randint(0, 3))
            if point not in points:
                points.append(point)
        return points


class Boggle:

    def __init__(self, generator=Default):
        self.generator = generator()
        self.board = self.generator.generate_board()

    def __str__(self):
        ret = ""
        "\n".join([" ".join(letters) for letters in self.board])
        return ret

    def get_board_list(self):
        return [[self.board[i][j] for i in range(4)] for j in range(4)]

    def count_max_points(self, dictionary="slowa.txt"):
        return boggle_solver(dictionary, self.board)

    def update_board(self, nslots):
        letters = self.generator.generate_letters(nslots)
        for slot, letter in letters.iteritems():
            self.board[slot[0]][slot[1]] = letter
