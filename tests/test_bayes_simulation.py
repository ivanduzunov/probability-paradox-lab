
import numpy as np
import pytest

from src.bayes_simulation import (
    bayes_probability,
    simulate_bayes_probability,
)


def test_bayes_probability():
    result = bayes_probability(
        prevalence=0.01,
        sensitivity=0.99,
        false_positive_rate=0.05,
    )

    assert result == pytest.approx(0.1667, abs=0.0001)


def test_invalid_probabilities():
    with pytest.raises(ValueError):
        bayes_probability(-0.1, 0.99, 0.05)

    with pytest.raises(ValueError):
        bayes_probability(0.01, 1.1, 0.05)

    with pytest.raises(ValueError):
        bayes_probability(0.01, 0.99, -0.1)


def test_simulation_approximates_theoretical_probability():
    rng = np.random.default_rng(42)

    theoretical = bayes_probability(0.01, 0.99, 0.05)

    simulated = simulate_bayes_probability(
        population_size=1_000_000,
        prevalence=0.01,
        sensitivity=0.99,
        false_positive_rate=0.05,
        rng=rng,
    )

    assert simulated == pytest.approx(theoretical, abs=0.005)


def test_invalid_population_size():
    with pytest.raises(ValueError):
        simulate_bayes_probability(
            population_size=0,
            prevalence=0.01,
            sensitivity=0.99,
            false_positive_rate=0.05,
        )
