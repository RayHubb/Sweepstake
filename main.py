from sweepstake import Sweepstake
from contestant import Contestant

sweepstake1 = Sweepstake('Some Sweepstake')
contestant1 = Contestant('Roger', 'Rabbit', 'RRabbit@gmail.com', 1234)
contestant2 = Contestant('Jerry', 'Smith', 'Jsmith@loser.com', 5678)
contestant3 = Contestant('Peter', 'Griffin', 'petagriffin@yahoo.com', 9123)
sweepstake1.register_contestant(contestant1)
sweepstake1.register_contestant(contestant2)
sweepstake1.register_contestant(contestant3)
sweepstake1.pick_winner()
sweepstake1.print_contestant_info(sweepstake1.winner)
