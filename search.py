from typing import Iterable, TypeVar

T = TypeVar('T')


def linear_search(sequence: Iterable[T], target: T) -> T | None:
    for idx, value in enumerate(sequence):
        if value == target:
            return idx
    return None


def binary_search(sequence: Iterable[T], target: T) -> T | None:
    left = 0
    right = len(sequence)

    while left < right:
        mid = (left + right) // 2

        if target < sequence[mid]:
            right = mid
        elif target == sequence[mid]:
            return mid
        else:
            left = mid + 1

    return None
