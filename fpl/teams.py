from .data import _teams
from .players import Player

class Team:
    def __init__(self, index: int = None, name: str = None):
        if isinstance(index, int):
            if name:
                raise TypeError('index AND name provided - please provide only one.')
            row = _teams.loc[index]
        elif name:
            row = _teams[_teams['name']==name].reset_index(drop=True).loc[0]
        else:
            raise TypeError('Neither index nor name provided - please provide one.')
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
