import pytest


from zombies.alert import *

def test_has_humans_identifies_humans():
    human = Being(10)
    assert has_humans([human])

def test_has_humans_identifies_lack_of_humans():
    zombie = Being(10)
    zombie.zombify()
    assert not has_humans([zombie])

def test_humans_at_returns_humans_at_location():
    beings = []
    beings.append(Being(10))
    beings.append(Being(10))

    zombie = Being(10)
    zombie.zombify()
    beings.append(zombie)

    humans = humans_at(-1, -1, beings)
    assert len(humans) == 2

def test_get_zombies_returns_all_zombies():
    beings = []
    beings.append(Being(10))
    beings.append(Being(10))

    zombie = Being(10)
    zombie.zombify()
    zombie.locate()
    beings.append(zombie)

    zombies = get_zombies(beings)
    assert len(zombies) == 1
