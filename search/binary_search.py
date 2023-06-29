from typing import Iterable, TypeVar

T = TypeVar('T')


def binary_search(sequence: Iterable[T], target: T) -> int | None:
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
