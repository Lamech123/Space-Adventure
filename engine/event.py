from random import random

class Event(object):
    '''A game event, including the probability of its happening.'''

    def __init__(self, title, probability, message, type, maxOccur=100000):
        self.title = title
        self.probability = probability
        self.message = message
        self.type = type
        self.remainingOccur = maxOccur

    def process(self):
        '''Process the event, and return the change in health, or 0.'''

        if self.remainingOccur and random() < self.probability:
            self.remainingOccur -= 1
            print(self.message)
        return 0