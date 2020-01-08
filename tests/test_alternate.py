from pytools.alternate import is_alternate

def test_alternate():
    s = 'ababab'
    assert is_alternate(s) is True
