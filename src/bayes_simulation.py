
import numpy as np


def bayes_probability(
    prevalence: float,
    sensitivity: float,
    false_positive_rate: float,
) -> float:
    """Calculate the probability of a condition given a positive test."""

    if not 0 <= prevalence <= 1:
        raise ValueError("Prevalence must be between 0 and 1.")

    if not 0 <= sensitivity <= 1:
        raise ValueError("Sensitivity must be between 0 and 1.")

    if not 0 <= false_positive_rate <= 1:
        raise ValueError("False-positive rate must be between 0 and 1.")

    true_positive_probability = sensitivity * prevalence

    positive_test_probability = (
        true_positive_probability
        + false_positive_rate * (1 - prevalence)
    )

    if positive_test_probability == 0:
        raise ValueError("Positive test results have zero probability.")

    return true_positive_probability / positive_test_probability



def simulate_bayes_probability(
    population_size: int,
    prevalence: float,
    sensitivity: float,
    false_positive_rate: float,
    rng: np.random.Generator | None = None,
) -> float:
    """Estimate the probability of having a condition given a positive test."""

    if population_size <= 0:
        raise ValueError("Population size must be positive.")

    if not 0 <= prevalence <= 1:
        raise ValueError("Prevalence must be between 0 and 1.")

    if not 0 <= sensitivity <= 1:
        raise ValueError("Sensitivity must be between 0 and 1.")

    if not 0 <= false_positive_rate <= 1:
        raise ValueError("False-positive rate must be between 0 and 1.")

    if rng is None:
        rng = np.random.default_rng()

    has_condition = rng.random(population_size) < prevalence

    test_positive_probability = np.where(
        has_condition,
        sensitivity,
        false_positive_rate,
    )

    test_positive = rng.random(population_size) < test_positive_probability

    positive_count = np.count_nonzero(test_positive)

    if positive_count == 0:
        return float("nan")

    true_positive_count = np.count_nonzero(has_condition & test_positive)

    return true_positive_count / positive_count

