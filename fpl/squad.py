#!/usr/bin/env python
"""squad.py - auto-generated by softnanotools"""
from .player import Player
from softnanotools.logger import Logger
logger = Logger(__name__)

class Squad:
    def __init__(self, *players: Player):
        self.players = players

    @property
    def positions(self):
        """Returns histogram of positions"""
        keys = [None, 'gkp', 'def', 'mid', 'fwd']
        result = {
            'gkp': 0,
            'def': 0,
            'mid': 0,
            'fwd': 0,
        }
        for p in self.players:
            result[keys[p.series['element_type']]] += 1
        return result

    def checks(self, *opt: str):
        status = True
        status = self.check_number_of_players
        status = self.check_gkp
        status = self.check_def
        status = self.check_mid
        status = self.check_fwd
        return status

    @property
    def check_number_of_players(self):
        if len(self.players) != 15:
            return False
        return True

    @property
    def check_gkp(self):
        """Check number of goalkeepers is equal to 2"""
        if len(self.players) < 2: return False
        pos = self.positions
        return pos['gkp'] == 2

    @property
    def check_def(self):
        """Check number of goalkeepers is equal to 2"""
        if len(self.players) < 5: return False
        pos = self.positions
        return pos['def'] == 5

    @property
    def check_mid(self):
        """Check number of goalkeepers is equal to 2"""
        if len(self.players) < 5: return False
        pos = self.positions
        return pos['mid'] == 5

    @property
    def check_fwd(self):
        """Check number of goalkeepers is equal to 2"""
        if len(self.players) < 3: return False
        pos = self.positions
        return pos['fwd'] == 3

if __name__ == '__main__':
    import doctest
    doctest.testmod()