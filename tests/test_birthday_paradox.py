
import numpy as np
import pytest

from src.birthday_paradox import (
    birthday_match_probability,
    simulate_birthday_match,
)


def test_birthday_match_probability_for_two_people():
    assert birthday_match_probability(2) == pytest.approx(1 / 365)


def test_birthday_match_probability_for_23_people():
    assert birthday_match_probability(23) == pytest.approx(0.5073, abs=0.0001)


def test_birthday_probability_increases_with_group_size():
    assert birthday_match_probability(30) > birthday_match_probability(20)


def test_invalid_group_size():
    with pytest.raises(ValueError):
        birthday_match_probability(-1)

    with pytest.raises(ValueError):
        birthday_match_probability(366)


def test_simulate_birthday_match_returns_boolean():
    rng = np.random.default_rng(42)

    result = simulate_birthday_match(23, rng=rng)

    assert isinstance(result, (bool, np.bool_))
