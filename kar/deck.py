import numpy as np


def decks(decks_count, no_tied_combinations):

    player_a = np.zeros(decks_count, dtype=int)
    player_b = np.zeros(decks_count, dtype=bool)

    for deck_a, deck_b, result in no_tied_combinations:
        if result == 1:
            player_a[deck_b-1] += 1
        else:
            player_b[deck_b-1] = True

    if max(player_a) == decks_count:
        return 1
    elif all(value for value in player_b):
        return -1
    return 0