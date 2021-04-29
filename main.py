from sweepstake import Sweepstake
from contestant import Contestant
from sweepstake_stack_manager import StackManager
from sweepstakes_queue_manager import QueueManager
from marketing_firm import MarketingFirm

# test objects and methods
sweepstake1 = Sweepstake('Some Sweepstake')
sweepstake2 = Sweepstake('Another Sweepstake')
sweepstake3 = Sweepstake('Yet Another Sweepstake')

contestant1 = Contestant('Roger', 'Rabbit', 'RRabbit@gmail.com', 1234)
contestant2 = Contestant('Jerry', 'Smith', 'Jsmith@loser.com', 5678)
contestant3 = Contestant('Peter', 'Griffin', 'petagriffin@yahoo.com', 9123)

sweepstake1.register_contestant(contestant1)
sweepstake1.register_contestant(contestant2)
sweepstake1.register_contestant(contestant3)

sweepstake1.pick_winner()

sweepstake1.print_contestant_info(sweepstake1.winner)

stack_manager = StackManager()
queue_manager = QueueManager()

stack_manager.insert_sweepstake(sweepstake1)
stack_manager.insert_sweepstake(sweepstake2)
stack_manager.insert_sweepstake(sweepstake3)

stack_manager.get_sweepstake()

queue_manager.inset_sweepstake(sweepstake1)
queue_manager.inset_sweepstake(sweepstake2)
queue_manager.inset_sweepstake(sweepstake3)

queue_manager.get_sweepstake()

firm1 = MarketingFirm(stack_manager)
firm1.create_sweepstake('You guessed it another sweepstake')






# just something to prevent myself from overstepping in the debugger to see end results
print('all done')
