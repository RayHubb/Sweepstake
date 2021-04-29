import random


class Sweepstake:

    def __init__(self, name):
        self.contestant_list = {}
        self.name = name
        self.winner = name

    def register_contestant(self, contestant):
        key = len(self.contestant_list) + 1
        self.contestant_list[key] = contestant

    def pick_winner(self):
        # should return a contestant
        sweepstake_winner = random.randint(1, len(self.contestant_list))
        self.winner = self.contestant_list.get(sweepstake_winner)
        print(f'{self.winner.first_name} {self.winner.last_name} is the chosen winner!')

    def print_contestant_info(self, contestant):
        print(self.winner.first_name)
        print(self.winner.last_name)
        print(self.winner.email)
        print(self.winner.registration)

