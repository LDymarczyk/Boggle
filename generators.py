import copy, yaml, random
from random import choice, randint, shuffle
from classes import Default
from math import ceil


class DiceGenerator(Default):

    def __init__(self):
        Default.__init__(self)

        self.dices = {0:  "RIFOBX",
                      1:  "IFEHEY",
                      2:  "DENOWS",
                      3:  "UTOKND",
                      4:  "HMSRAO",
                      5:  "LUPETS",
                      6:  "ACITOA",
                      7:  "YLGKUE",
                      8:  "QBMJOA",
                      9:  "EHISPN",
                      10: "VETIGN",
                      11: "BALIYT",
                      12: "EZAVND",
                      13: "RALESC",
                      14: "UWILRG",
                      15: "PACEMD"}
        self.dice_order = range(16)
        shuffle(self.dice_order)

    def __str__(self):
        return "Dice Generator"

    def generate_letters(self, nslots):
        nslots = self.generate_slots(nslots)
        new_order = copy.deepcopy(nslots)
        while new_order == nslots:
            shuffle(new_order)
        ret = {}
        for i in range(len(nslots)):
            ret[nslots[i]] = choice(self.dices[4*new_order[i][0]+new_order[i][1]])
            self.dice_order[self.dice_order.index(4*nslots[i][0]+nslots[i][1])] = 4*new_order[i][0]+new_order[i][1]
        return ret

    def generate_board(self):
        return [[choice(self.dices[self.dice_order[4*j+i]]) for i in range(4)] for j in range(4)]


class FunnyGenerator(Default):

    def __init__(self):
        Default.__init__(self)
        self.generate_devide(self.letters)
        self.count_percent()


    def __str__(self):
        return "Funny Generator"

    def generate_devide(self, letters):
        keys = [0 for i in letters]
        values = [i for i in letters]
        count_letters = dict(zip(values, keys))
        with open("slowa.txt", 'r') as content:
            words = content.read().split('\n')
            for word in words:
                for letter in word:
                    count_letters[letter.upper()] += 1
        with open("letters.yml", "w") as yamlfile:
            yaml.dump(count_letters, yamlfile, default_flow_style=False)

    def count_percent(self):
        with open("letters.yml", "r") as yamlfile:
            letters_count = yaml.safe_load(yamlfile)
        all_letters = sum(letters_count.values())
        letters = ""
        for key, value in letters_count.iteritems():
            letters_count[key] = int(ceil(value * 200.0 / all_letters))
            letters += key * letters_count[key]
        self.letters = ''.join(random.sample(letters, len(letters)))


if __name__=="__main__":
        gen = DiceGenerator()
        print(gen.dice_order)
        print(gen.generate_letters(4))
