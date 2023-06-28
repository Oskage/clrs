from copy import deepcopy
from typing import Iterable, TypeVar

T = TypeVar('T')


def selection_sort(
        sequence: Iterable[T],
        reverse: bool = False,
) -> Iterable[T]:
    sequence = deepcopy(sequence)
    for i in range(len(sequence) - 1):
        found_idx = i
        for j in range(i, len(sequence)):
            if (sequence[j] < sequence[found_idx]
                    if not reverse
                    else sequence[j] > sequence[found_idx]):
                found_idx = j
        sequence[i], sequence[found_idx] = sequence[found_idx], sequence[i]
    return sequence
