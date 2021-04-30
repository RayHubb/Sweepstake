from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstake(self):
        sweepstake_4 = 'purplebanana'
        self.manager.insert_sweepstakes(Sweepstake(sweepstake_4))

