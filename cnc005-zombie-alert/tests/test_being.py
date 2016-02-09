import pytest


from zombies.being import *

def test_being_is_a_human():
    human = Being(10)
    assert human.reveal() == "H"

def test_being_can_be_zombified():
    human = Being(10)
    human.zombify()
    assert human.reveal() == "Z"

def test_being_has_max_location():
    human = Being(40)
    assert human.max_location == 40

def test_being_has_x_coordinate():
    human = Being(10)
    assert human.x <= 10

def test_being_has_y_coordinate():
    human = Being(10)
    assert human.y <= 10

def test_location_starts_negative():
    human = Being(10)
    assert human.x < 0
    assert human.y < 0

def test_locate_randomizes_location_less_than_limit():
    human = Being(10)
    human.locate()
    assert human.x >= 0
    assert human.x < 10
    assert human.y >= 0
    assert human.y < 10

def test_can_move():
    human = Being(10)
    human.locate()

    old_x = human.x
    old_y = human.y

    human.move()

    assert human.x != old_x or human.y != old_y

def test_change_loc_at_zero_moves_up():
    assert change_loc(0, 10) == 1

def test_change_loc_at_max_moves_down():
    assert change_loc(9, 10) == 8

def test_at():
    human = Being(10)
    human.locate()
    assert human.at(human.x, human.y)

def test_close_identifies_close_by_beings():
    human = Being(10)
    human.set_at(1,1)

    zomb_one = Being(10)
    zomb_one.zombify()
    zomb_one.set_at(1,2)

    zomb_two = Being(10)
    zomb_two.zombify()
    zomb_two.set_at(4,4)

    assert human.close([zomb_two, zomb_one]) == (1,2)

def test_is_next_to():
    assert is_next_to(1,0)
    assert is_next_to(7,8)
    assert is_next_to(4,4)

def test_is_not_next_to():
    assert not is_next_to(9,0)
    assert not is_next_to(7,9)
