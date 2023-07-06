from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).parent

class BootstrapStatic:
    YEARS = [2020, 2021, 2022, 2023]
    def __init__(self, year: int):
        # check year is correct
        assert year in self.YEARS
        self.year = year
        self.read()

    def read(self, year: int = None):
        """Read data from pre-loaded bootstrap-static files"""
        if not (year is None):
            self.year = year
        with open(ROOT / f"{self.year}.json", 'r') as f:
            self.data = json.load(f)
        return self.data

    @property
    def element_stats(self):
        return pd.DataFrame(self.data['element_stats'])

    @property
    def element_types(self):
        return pd.DataFrame(self.data['element_types'])

    @property
    def elements(self):
        return pd.DataFrame(
            self.data['elements']
        ).sort_values(
            by=['team', 'element_type', 'now_cost']
        ).reset_index(drop=True)

    @property
    def events(self):
        return self.data['events']

    @property
    def settings(self):
        return self.data['game_settings']

    @property
    def phases(self):
        return pd.DataFrame(self.data['phases'])

    @property
    def teams(self):
        return pd.DataFrame(self.data['teams'])

    @property
    def total_players(self):
        return self.data['total_players']
