from generators import LetterFrequencyGenerator, DiceGenerator, Default, LetterFrequencyGenerator2
from simulated_annealing import SimulatedAnnealing, Boggle
import datetime, os, time


class Runner:

    def __init__(self):
        self.generators = {1: Default,
                           2: LetterFrequencyGenerator,
                           3: DiceGenerator}

    def run(self, generator_id=1):
        generator = self.generators[generator_id]
        simulator = SimulatedAnnealing()
        simulator.set_random_generator(generator)
        file_name = "test_data"
        folder = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S")
        current_folder = os.getcwd()
        os.mkdir(folder)
        os.chdir(folder)
        with open("{}--{}".format(file_name, str(generator)), 'w') as statistic_file:
            os.chdir(current_folder)
            data, board = simulator.execute()
            data = "\n".join(data)
            statistic_file.write(data)
        print(board)

    def collect_data_for_statistics(self, generator_id=1, n=50):
        folder = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S")
        os.mkdir(folder)
        file_name = "statistic_data"
        generator = self.generators[generator_id]
        for i in range(n):
            statistic_file = open(os.path.join(folder, "{}--{}".format(file_name, str(generator))), 'a+')
            game = Boggle(generator)
            game.get_board_list()
            points = game.count_max_points()
            print points
            statistic_file.write(str(points) + "\n")
            print(i)
            statistic_file.close()

    def time_counter(self, generator_id=1, n=50):
        generator = self.generators[generator_id]
        folder = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S_"+str(generator))
        os.mkdir(folder)
        file_name = "time_data"
        for i in range(n):
            statistic_file = open(os.path.join(folder, "{}--{}".format(file_name, str(generator))), 'a+')
            t_start = time.time()
            game = Boggle(generator)
            game.update_board(4)
            t_end = time.time()
            t = t_end - t_start
            print(t)
            statistic_file.write(str(t) + "\n")
            statistic_file.close()
        print("done!")

    def sec_time_counter(self, generator_id=1, n=100):
        self.generators[2] = LetterFrequencyGenerator2
        generator = self.generators[generator_id]
        folder = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S_" + str(generator))
        os.mkdir(folder)
        file_name = "time_data2"
        statistic_file = open(os.path.join(folder, "{}--{}".format(file_name, str(generator))), 'a+')
        t_start = time.time()
        for i in range(n):
            game = Boggle(generator)
        t_end = time.time()
        t = t_end - t_start
        t_start = time.time()
        statistic_file.write(str(t) + " ")
        for i in range(n):
            game.update_board(4)
        t_end = time.time()
        t = t_end - t_start
        statistic_file.write(str(t) + "\n")
        statistic_file.close()
        print("done!")



# Runner().run(3)
#Runner().collect_data_for_statistics(3, 50)

for i in xrange(3):
    Runner().sec_time_counter(i+1)
