from typing import Iterable, TypeVar

T = TypeVar('T')


def linear_search(sequence: Iterable[T], target: T) -> int | None:
    for idx, value in enumerate(sequence):
        if value == target:
            return idx
    return None
