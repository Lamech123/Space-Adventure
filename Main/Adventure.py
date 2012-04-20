
__author__="wyeth"
__date__ ="$Apr 18, 2012 10:58:50 PM$"

from engine.game import Game
from engine.place import Place
from engine.event import Event

class ShipGame(Game):
    def __init__(self):
        super(ShipGame, self).__init__()
        self.introduction = '''
Welcome to Ship Adventure. You are the captain of a star ship.
'''
        intruder = Event('Intruder', 0.8,'An intruder enters and attacks you', 1)
        
        bridge = Place('Bridge',"You are on the bridge of a spaceship, sitting in the captain's chair.", ())
        readyRoom = Place('Ready Room', "You are in the captain's ready room.", (intruder,))
        lift = Place('Lift', 'You have entered the turbolift.', ())
        lounge = Place('Lounge', 'Welcome to the lounge.', ())

        
        bridge.transitions = (readyRoom, lift)
        readyRoom.transitions = (bridge,)
        lift.transitions = (bridge,lounge)
        lounge.transitions = (lift,)

        self.location = bridge


game = ShipGame()
game.play()