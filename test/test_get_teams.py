from fpl.teams import BSTeam, Team
from fpl import BootstrapStatic

def test_Team():
    Team(None)

def test_BSTeam():
    for i in BootstrapStatic.YEARS:
        bs = BootstrapStatic(i)
        for j in range(20):
            BSTeam(bs, j)