# Zombie Dice Bots

import zombiedice
import random


class random_roller:
    ''' A bot that, after the first roll, randomly decides if it will continue or stop '''

    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        dice_roll_results = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        decision = random.randint(0, 1)
        # 0 to roll, 1 to stop
        while decision == 0:
            dice_roll_results = zombiedice.roll()
            decision = random.randint(0, 1)


class stop_after_two_brains(object):
    ''' A bot that stops rolling after it has rolled two brains '''

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        dice_roll_results = zombiedice.roll()  # first roll

        brain_count = 0
        while dice_roll_results is not None:
            # Add number of brains collected from roll
            brain_count += dice_roll_results['brains']

            if brain_count < 2:
                dice_roll_results = zombiedice.roll()  # roll again
            else:
                break


class stop_after_two_shotguns(object):

    ''' A bot that stops rolling after it has rolled two shotguns '''

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        shotgun_count = 0

        dice_roll_results = zombiedice.roll()  # first roll
        shotgun_count += dice_roll_results['shotgun']
        while shotgun_count < 2:
            dice_roll_results = zombiedice.roll()

            if dice_roll_results['shotgun'] is not None:
                shotgun_count += dice_roll_results['shotgun']


class roll_one_to_four(object):

    ''' A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns '''

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        number_of_rolls = random.randint(1, 4)
        shotgun_count = 0

        for roll in range(number_of_rolls):
            dice_roll_results = zombiedice.roll()

            try:
                shotgun_count += dice_roll_results['shotgun']
            except:
                pass

            if shotgun_count == 2:
                break
            else:
                pass


class shotgun_over_brain(object):
    ''' A bot that stops rolling after it has rolled more shotguns than brains '''

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun_count = 0
        brain_count = 0
        dice_roll_results = zombiedice.roll()

        if dice_roll_results['shotgun'] is not None:
            shotgun_count += dice_roll_results['shotgun']
        elif dice_roll_results['brain'] is not None:
            brain_count += dice_roll_results['brains']

        while shotgun_count < brain_count:
            dice_roll_results = zombiedice.roll()

            if dice_roll_results['shotgun'] is not None:
                shotgun_count += dice_roll_results['shotgun']
            elif dice_roll_results['brain'] is not None:
                brain_count += dice_roll_results['brains']


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 1 Shotgun', minShotguns=1),
    random_roller(name='RandomRoller'),
    stop_after_two_brains(name='StopAfterTwoBrains'),
    stop_after_two_shotguns(name='StopAfterTwoShotguns'),
    roll_one_to_four(name='RollsOneToFourTimes'),
    shotgun_over_brain(name='Shotgun>Brain')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
