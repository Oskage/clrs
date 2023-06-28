from copy import deepcopy
from typing import Iterable, TypeVar

T = TypeVar('T')


def merge(
        sequence: Iterable[T],
        p: int,
        q: int,
        r: int,
        reverse: bool = False,
):
    left = list(sequence[p: q])
    right = list(sequence[q: r])

    left.append(float('inf') if not reverse else float('-inf'))
    right.append(float('inf') if not reverse else float('-inf'))

    left_idx = 0
    right_idx = 0
    for k in range(p, r):
        if (left[left_idx] < right[right_idx]
                if not reverse
                else left[left_idx] > right[right_idx]):
            sequence[k] = left[left_idx]
            left_idx += 1
        else:
            sequence[k] = right[right_idx]
            right_idx += 1


def inner_merge_sort(
        sequence: Iterable[T],
        p: int,
        r: int,
        reverse: bool = False,
):
    if p + 1 >= r:
        return

    q = (p + r) // 2
    inner_merge_sort(sequence, p, q, reverse)
    inner_merge_sort(sequence, q, r, reverse)

    merge(sequence, p, q, r, reverse)


def merge_sort(
        sequence: Iterable[T],
        reverse: bool = False,
) -> Iterable[T]:
    sequence = deepcopy(sequence)
    inner_merge_sort(sequence, p=0, r=len(sequence), reverse=reverse)
    return sequence
