import os.path as path

ROOT = '/'.join(path.abspath(__file__).split('/')[:-1])

with open(f'{ROOT}/2020.json', 'r') as f:
    static_2020 = json.load(f)