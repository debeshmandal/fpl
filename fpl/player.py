from .data import BootstrapStatic
import pandas as pd

class Player:
    def __init__(self, series: pd.Series):
        self.series = series

class BSPlayer(Player):
    def __init__(
            self,
            bs: BootstrapStatic,
            index : int = None,
            name : str = None
        ):
        super()
        if not (index or name) or (index and name):
            raise TypeError(
                'Please give an index OR name'
            )
        if index:
            row = bs.elements.loc[index]
        elif name:
            try:
                row = bs.elements[
                    bs.elements['web_name']==name
                ].reset_index(drop=True).loc[0]
            except KeyError:
                raise KeyError(f"{name} could not be found!")
        self.series = row