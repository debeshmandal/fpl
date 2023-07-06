from fpl import BootstrapStatic

def test_BootstrapStatic():
    [BootstrapStatic(i) for i in BootstrapStatic.YEARS]

def test_BootstrapStatic_properties():
    for i in BootstrapStatic.YEARS:
        bs = BootstrapStatic(i)
        assert not (bs.data is None)
        assert not (bs.element_stats is None)
        assert not (bs.elements is None)
        assert not (bs.element_types is None)
        assert not (bs.events is None)
        assert not (bs.phases is None)
        assert not (bs.teams is None)
        assert not (bs.total_players is None)
