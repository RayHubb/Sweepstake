import random
from contestants import Contestant


class Sweepstake:

    def __init__(self, name):
        self.contestant_list = {}
        self.name = name

    def register_contestant(self, contestant):
        key = len(self.contestant_list) + 1
        self.contestant_list[key] = contestant

    def pick_winner(self):
        # should return a contestant
        sweepstake_winner = random.randint(1, len(self.contestant_list))
        winner = self.contestant_list.get(sweepstake_winner)
        print(f'Congrats to {winner}! You are the chosen WINNER!!')

    def print_contestant_info(self, contestant):
        pass


contestant1 = Contestant('John', 'Henry', 'crfw@gmail.com', 34124)
contestant2 = Contestant('Ray', 'Alexander', 'ray@gmail.com', 48646)
