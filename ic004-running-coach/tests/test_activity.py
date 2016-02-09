import pytest


from couch.activity import Activity, Jog, Walk


def test_activity_has_name():
    sprint = Activity("run", 10)
    assert sprint.name == "run"

def test_activity_has_duration():
    walk = Activity("walk", 10)
    assert walk.duration == 10

def test_activity_accepts_a_third_optional_parameter_next_action():
    run = Activity("run", 10)
    walk = Activity("walk", 10, run)

    assert walk.next_action.name == "run"

def test_can_set_next_activity_manually():
    run = Activity("run", 10)
    walk = Activity("walk", 10)

    run.next_action = walk
    assert run.next_action.name == "walk"

def test_jog_is_syntactic_sugar():
    jog = Jog(10)
    assert jog.name == "jog"

def test_walk_is_syntactic_sugar():
    walk = Walk(10)
    assert walk.name == "walk"

def test_can_chain_activities():
    workout = Walk(600, Jog(60, Walk(60, Jog(60, Walk(60, Jog(60))))))

    assert workout.name == "walk"
    assert workout.next_action.name == "jog"
    last = workout.next_action.next_action.next_action.next_action.next_action
    assert last.next_action == None

def test_activity_outputs():
    swim = Activity("swim", 300)
    assert swim.output() == "swim for 300 seconds"

def test_can_add_to_tail():
    jogs = Jog(10, Jog(10, Jog(10)))
    jogs.add_to_tail(Walk(30))
    assert jogs.next_action.next_action.next_action.name == "walk"

def test_can_return_length():
    jogs = Jog(10)
    assert jogs.chain_length() == 1

    jogs.next_action = Walk(10)

    assert jogs.chain_length() == 2
