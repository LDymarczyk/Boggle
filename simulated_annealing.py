from classes import *
from random import randint
import time, random


class SimulatedAnnealing:

    def __init__(self):
        self.temperature = 100
        self.random_generator = randint
        self.board = None

    def set_random_generator(self, generator=randint):
        self.random_generator = generator
        print "Set new random generator"

    def get_started(self):
        self.board = Boggle()
        print "Created boggle board {}".format(str(self.board))

    def count_points(self):
        return boggle_solver("slowa.txt", self.board.board)
## https://pl.wikipedia.org/wiki/Symulowane_wy%C5%BCarzanie 3
    def change_board(self, number_of_slots): ##todo end this
        print number_of_slots

    def execute(self, times=100):
        self.get_started()
        # points = self.count_points()
        self.change_board(random.randint(1, 5))


sa = SimulatedAnnealing()
sa.get_started()
# import pdb; pdb.set_trace()
str(sa.board.board)
start_time = time.time()
sa.execute(1)
elapsed_time = time.time() - start_time
print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

