from copy import deepcopy
from typing import Iterable, TypeVar

T = TypeVar('T')


def insertion_sort(
        sequence: Iterable[T],
        reverse: bool = False,
) -> Iterable[T]:
    sequence = deepcopy(sequence)
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i >= 0 and (sequence[i] > key
                          if not reverse
                          else sequence[i] < key):
            sequence[i + 1] = sequence[i]
            i -= 1
        sequence[i + 1] = key
    return sequence
