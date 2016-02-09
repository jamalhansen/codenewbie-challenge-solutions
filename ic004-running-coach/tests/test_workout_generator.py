import pytest


from couch.workout_generator import WorkoutGenerator
from couch.activity import Walk, Jog

def test_workout_generator_knows_week():
    gen = WorkoutGenerator(1,2)
    assert gen.week == 1

def test_workout_generator_knows_workout():
    gen = WorkoutGenerator(1,2)
    assert gen.workout == 2

def validate_workout(expected, actual):
    assert expected.chain_length() == actual.chain_length()

    while actual.next_action:
        assert expected.name == actual.name
        assert expected.duration == actual.duration
        actual = actual.next_action
        expected = expected.next_action

def test_week_one_workout():
    gen = WorkoutGenerator(1,1)
    actual = gen.get_workout()

    expected = Walk(300)
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))
    expected.add_to_tail(Jog(60, Walk(90)))

    validate_workout(expected, actual)

def test_week_two_workout():
    gen = WorkoutGenerator(2,1)
    actual = gen.get_workout()

    expected = Walk(300, Jog(90, Walk(120)))
    expected.add_to_tail(Jog(90, Walk(120)))
    expected.add_to_tail(Jog(90, Walk(120)))
    expected.add_to_tail(Jog(90, Walk(120)))
    expected.add_to_tail(Jog(90, Walk(120)))
    expected.add_to_tail(Jog(90, Walk(60)))

    validate_workout(expected, actual)
