
import numpy as np

from src.monty_hall import simulate_monty_hall


def test_stay_probability():
    rng = np.random.default_rng()

    wins = sum(
        simulate_monty_hall(switch=False, rng=rng)
        for _ in range(10_000)
    )
    probability = wins / 10_000

    assert abs(probability - 1 / 3) < 0.03


def test_switch_probability():
    rng = np.random.default_rng()

    wins = sum(
        simulate_monty_hall(switch=True, rng=rng)
        for _ in range(10_000)
    )
    probability = wins / 10_000

    assert abs(probability - 2 / 3) < 0.03
