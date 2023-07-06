from fpl.squad import Squad
from fpl import BSPlayer, BootstrapStatic

def test_Squad():
    bs = BootstrapStatic(2023)
    s = Squad(
        BSPlayer(bs, name='Ramsdale'),
        BSPlayer(bs, name='Zinchenko'),
        BSPlayer(bs, name='White'),
        BSPlayer(bs, name='Tomiyasu'),
        BSPlayer(bs, name='Walker'),
        BSPlayer(bs, name='Xhaka'),
        BSPlayer(bs, name='Saka'),
        BSPlayer(bs, name='Martinelli'),
        BSPlayer(bs, name='Kane'),
        BSPlayer(bs, name='Haaland'),
        BSPlayer(bs, name='Jesus'),
        BSPlayer(bs, name='De Gea'),
        BSPlayer(bs, name='Maguire'),
        BSPlayer(bs, name='De Bruyne'),
        BSPlayer(bs, name='Enzo'),
    )
    [print(p.series['web_name']) for p in s.players]
    print(s.positions)
    assert s.check_number_of_players
    assert s.check_gkp
    assert s.check_def
    assert s.check_mid
    assert s.check_fwd
