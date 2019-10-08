from generators import LetterFrequencyGenerator, DiceGenerator, Default
from simulated_annealing import SimulatedAnnealing
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


Runner().run(3)
