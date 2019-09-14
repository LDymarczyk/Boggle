from classes import *
from random import randint
import time, random, copy
from math import exp


class SimulatedAnnealing:

    def __init__(self, alfa=0.5):
        self.temperature = 600
        self.alfa = alfa
        self.n = 0.91
        self.random_generator = randint
        self.board = None
        self.new_board = None

    def set_random_generator(self, generator=randint):
        self.random_generator = generator
        print "Set new random generator"

    def get_started(self):
        self.board = Boggle()
        print "Created boggle board {}".format(str(self.board.board))

    def count_points(self, board):
        return boggle_solver("slowa.txt", board.board)
## https://pl.wikipedia.org/wiki/Symulowane_wy%C5%BCarzanie 4
    def change_board(self):
        number_of_slots = random.randint(1, 5)
        self.new_board = copy.copy(self.board)
        self.new_board.update_board(number_of_slots)

    def execute(self):
        self.get_started()
        i =1
        # while self.temperature>6:
            # points = self.count_points(self.board)
        print(self.board.board)
        self.change_board()
        print(self.board.board)
            # new_points = self.count_points(self.new_board)
            # print(points, new_points)
            # if new_points > points or exp((points - new_points)/self.temperature) > self.alfa:
            #     print("greatwder")
            #     self.board = self.new_board
            # print i
            # i += 1
            # self.temperature *= self.n



sa = SimulatedAnnealing()
start_time = time.time()
sa.execute()
elapsed_time = time.time() - start_time
print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

