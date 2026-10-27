import numpy as np


def simulate_monty_hall(switch: bool) -> bool:
    """Simulate one Monty Hall game and return whether the player wins."""

    rng = np.random.default_rng()

    doors = [0, 1, 2]

    car_door = rng.choice(doors)
    player_choice = rng.choice(doors)

    # The host can open only an unselected door with a goat.
    possible_doors = [
        door for door in doors
        if door != player_choice and door != car_door
    ]

    host_opens = rng.choice(possible_doors)

    # If switching, choose the only remaining unopened door.
    if switch:
        player_choice = next(
            door for door in doors
            if door != player_choice and door != host_opens
        )

    return car_door == player_choice
