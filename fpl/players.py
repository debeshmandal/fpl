from .data import _elements

class Player:
    def __init__(self, index : int = None, name : str = None):
        if not (index or name) or (index and name):
            raise TypeError('Please give an index OR name')
        if index:
            row = _teams.loc[index]
        elif name:
            row = _teams[_teams['web_name']==name].reset_index(drop=True).loc[0]
        self.series = row