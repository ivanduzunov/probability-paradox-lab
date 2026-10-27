
import numpy as np

def birthday_match_probability(group_size: int) -> float:
    """Calculate the probability that at least two people share a birthday."""

    if group_size < 0 or group_size > 365:
        raise ValueError("Group size must be between 0 and 365.")

    probability_all_different = 1.0

    for person in range(group_size):
        probability_all_different *= (365 - person) / 365

    return 1 - probability_all_different


def simulate_birthday_match(
    group_size: int,
    rng: np.random.Generator | None = None
) -> bool:
    """Simulate a group and check whether any birthdays match."""

    if group_size < 0 or group_size > 365:
        raise ValueError("Group size must be between 0 and 365.")

    if rng is None:
        rng = np.random.default_rng()

    birthdays = rng.integers(0, 365, size=group_size)

    return len(np.unique(birthdays)) < group_size
