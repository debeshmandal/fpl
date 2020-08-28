from .data import _teams
from .players import Player

class Team:
    def __init__(self, index : int = None, name : str = None):
        if not (index or name) or (index and name):
            raise TypeError('Please give an index OR name')
        if index:
            row = _teams.loc[index]
        elif name:
            row = _teams[_teams['name']==name].reset_index(drop=True).loc[0]
        self.series = row[[
                'short_name',
                'strength_attack_home',
                'strength_attack_away',
                'strength_defence_home',
                'strength_defence_away',
                'strength_overall_home',
                'strength_overall_away'
            ]]

    def __repr__(self):
        return f'Team({self.name})'

    @property
    def name(self):
        return self.series['short_name']

    @property
    def home(self):
        return {
            'attack' :  self.series['strength_attack_home'],
            'defence' : self.series['strength_defence_home'],
            'overall' : self.series['strength_overall_home']
        }

    @property
    def away(self):
        return {
            'attack' :  self.series['strength_attack_away'],
            'defence' : self.series['strength_defence_away'],
            'overall' : self.series['strength_overall_away']
        }


