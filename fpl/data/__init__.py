import os.path as path
import json
import pandas as pd

ROOT = '/'.join(path.abspath(__file__).split('/')[:-1])


with open(f'{ROOT}/2022.json', 'r') as f:
    static_2020 = json.load(f)

TOTAL_PLAYERS = static_2020['total_players']
_element_stats = pd.DataFrame(static_2020['element_stats'])
_element_types = pd.DataFrame(static_2020['element_types'])
_elements = pd.DataFrame(static_2020['elements']).sort_values(by=['team', 'element_type', 'now_cost']).reset_index(drop=True)
_events = static_2020['events']
_settings = static_2020['game_settings']
_phases = pd.DataFrame(static_2020['phases'])
_teams = pd.DataFrame(static_2020['teams'])
