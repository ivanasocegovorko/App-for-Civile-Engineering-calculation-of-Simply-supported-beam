from project import shear_force, bending_moment, support_reactions, max_deflection

def test_shear_force():
    assert shear_force(10, 10) == 50
    assert shear_force(10, -10) == -50


def test_bending_moment():
    assert bending_moment(10, 10) == 125
    assert bending_moment(10, -10) == -125


def test_support_reactions():
    assert support_reactions(1, 2) == 1
    assert support_reactions(100, -2000) == -100000

def test_max_deflection():
    assert max_deflection(1, 20, 21000, 630) == 0.1968


