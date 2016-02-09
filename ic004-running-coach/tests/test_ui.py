import pytest


from couch.user_interfaces import split_times

def test_split_times_splits_times_into_list():
    times = split_times(200)
    assert len(times) > 1

def test_splits_times_into_twenty_second_chunks():
    times = split_times(200)
    assert len(times) == 10

def test_splits_times_adds_odd_time_to_first_portion():
    times = split_times(206)
    assert times[0] == 26
