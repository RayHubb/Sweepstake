from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstake(self, name):
        sweepstake4 = Sweepstake(name)
        print(sweepstake4.name)