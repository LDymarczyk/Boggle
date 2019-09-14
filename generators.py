import copy
from random import choice, randint, shuffle
from .classes import Default


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
        self.dice_order = shuffle(range(16))

    def __str__(self):
        return "Dice Generator"

    def generate_letters(self, nslots):
        new_order = []
        old_order = copy.deepcopy(nslots)
        while old_order:
            old_order = shuffle(old_order)
            new_order.append(old_order.pop())
        Default.generate_letters(self, nslots)
        #todo change this

    def generate_board(self):
        return [[choice(self.dices[self.dice_order[4*j+i]]) for i in range(4)] for j in range(4)]


class FunnyGenerator(Default):

    def __init__(self):
        Default.__init__(self)
        self.letters = self.generate_devide(self.letters)

    def __str__(self):
        return "Funny Generator"

    def generate_devide(self, letters):
        count_letters = dict(zip([0 for i in letters], [i for i in letters]))
        with open("slowa.txt", 'r') as content:
            words = content.read().split('\n')
            for word in words:
                for letter in word:
                    count_letters[letter] += 1
        return self.letters
   