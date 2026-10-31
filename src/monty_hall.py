
import numpy as np


def simulate_monty_hall(
    switch: bool,
    rng: np.random.Generator | None = None
) -> bool:
    """Simulate one Monty Hall game and return whether the player wins."""

    if rng is None:
        rng = np.random.default_rng()

    doors = [0, 1, 2]

    car_door = rng.choice(doors)
    player_choice = rng.choice(doors)

    possible_doors = [
        door for door in doors
        if door != player_choice and door != car_door
    ]

    host_opens = rng.choice(possible_doors)

    if switch:
        player_choice = next(
            door for door in doors
            if door != player_choice and door != host_opens
        )

    return car_door == player_choice
