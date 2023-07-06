from fpl import BootstrapStatic, BSPlayer

def test_players_index():
    bs = BootstrapStatic(2023)
    p = BSPlayer(bs, 1)
    assert p.series['element_type'] == 1

def test_players_name():
    bs = BootstrapStatic(2023)
    p = BSPlayer(bs, name='Turner')
    assert p.series['element_type'] == 1
