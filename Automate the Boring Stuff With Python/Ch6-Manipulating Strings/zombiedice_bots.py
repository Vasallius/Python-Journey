import zombiedice
import random

class RandomRoller:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        decision = random.randint(0,1)
        if decision == 0:
            diceRollResults = zombiedice.roll() # first roll


        # #brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #
        #     if brains < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break

class StopAfterTwoBrains(object):
    """After the first roll, this bot always has a fifty-fifty chance of deciding to roll again or stopping."""
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        results = zombiedice.roll() # first roll

        while results and random.randint(0, 1) == 0:
            results = zombiedice.roll()
class StopAfterTwoSG(object):

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        shotguncnt = 0
        while diceRollResults is not None:

            shotguncnt += diceRollResults['shotgun']

            if shotguncnt < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class Jhin(object):

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        x = random.randint(1,4)

        for y in range(x):
            diceRollResults = zombiedice.roll()

        shotguncnt = 0

        while diceRollResults is not None:

            shotguncnt += diceRollResults['shotgun']

            if shotguncnt < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class DUMBRIANE(object):

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        shotguncnt = 0
        braincnt = 0
        while diceRollResults is not None:

            shotguncnt += diceRollResults['shotgun']
            braincnt += diceRollResults['brains']

            print(shotguncnt,braincnt)

            if shotguncnt < braincnt:
                diceRollResults = zombiedice.roll()
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    RandomRoller(name='RandomRoller'),
    StopAfterTwoBrains(name='StopAfterTwoBrains'),
    StopAfterTwoSG(name='StopAfterTwoSG'),
    Jhin(name='Jhin'),
    DUMBRIANE(name='DUMBRIANE')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
