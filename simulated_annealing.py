from classes import *
import time, random, copy
from math import exp


class SimulatedAnnealing:

    def __init__(self):
        self.temperature = 600
        self.n = 0.91
        self.random_generator = Default
        self.board = None
        self.new_board = None
        self.results = []

    def set_random_generator(self, generator=Default):
        self.random_generator = generator
        print "Set new random generator"

    def get_started(self):
        self.board = Boggle(self.random_generator)
        print "Created boggle board {}".format(str(self.board.board))

    def count_points(self, board):
        return boggle_solver("slowa.txt", board.board)

    def change_board(self):
        number_of_slots = random.randint(1, 5)
        self.new_board = copy.copy(self.board)
        self.new_board.update_board(number_of_slots)

    def execute(self):
        self.get_started()
        i = 1
        points = self.count_points(self.board)
        self.results.append(str(points))
        print "result ", self.results
        while self.temperature > 599: #6
            self.change_board()
            new_points = self.count_points(self.new_board)
            self.results.append(str(new_points))
            if new_points > points or exp((points - new_points)/self.temperature) > random.random():
                self.board = self.new_board
                points = new_points
            i += 1
            print "result ", self.results
            self.temperature *= self.n
        print("done!")
        return self.results, self.board.board


if __name__ == "__main__":
    sa = SimulatedAnnealing()
    start_time = time.time()
    sa.execute()
    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
