from generators import LetterFrequencyGenerator, DiceGenerator, Default
from simulated_annealing import SimulatedAnnealing, Boggle
import datetime, os


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


# Runner().run(3)
Runner().collect_data_for_statistics(1, 50)
