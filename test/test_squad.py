from fpl.squad import Squad
from fpl import BSPlayer, BootstrapStatic

def test_Squad():
    bs = BootstrapStatic(2023)
    s = Squad(
        BSPlayer(bs, name='Lloris'),
        BSPlayer(bs, name='Zinchenko'),
        BSPlayer(bs, name='Burn'),
        BSPlayer(bs, name='Castagne'),
        BSPlayer(bs, name='Walker'),
        BSPlayer(bs, name='Rashford'),
        BSPlayer(bs, name='Saka'),
        BSPlayer(bs, name='Martinelli'),
        BSPlayer(bs, name='Kane'),
        BSPlayer(bs, name='Maupay'),
        BSPlayer(bs, name='Watkins'),
        BSPlayer(bs, name='De Gea'),
        BSPlayer(bs, name='Maguire'),
        BSPlayer(bs, name='De Bruyne'),
        BSPlayer(bs, name='Enzo'),
    )
    [print(p.series['web_name']) for p in s.players]
    print(s.players[0].series.index)
    print(s.positions)
    print(s.teams)
    print(s.price)
    assert s.check_number_of_players
    assert s.check_gkp
    assert s.check_def
    assert s.check_mid
    assert s.check_fwd
    assert s.check_teams
    assert s.check_price
