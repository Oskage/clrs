from typing import Iterable, TypeVar

from tqdm import tqdm

from search import binary_search

T = TypeVar('T')


def find_two_sum(sequence: Iterable[T], target: T) -> tuple[int, int] | None:
    sequence = sorted(sequence)

    for idx, value in enumerate(sequence[:-1]):
        residual = target - value
        second_idx = binary_search(sequence[idx + 1:], residual)
        if second_idx is not None:
            return idx, (idx + 1) + second_idx

    return None


def main():
    tests = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[2, 3, 4], 7, [1, 2]],
        [[3, 3], 6, [0, 1]],
    ]

    for (seq, target, answer) in tqdm(tests):
        result = find_two_sum(seq, target)

        assert set(result) == set(answer), (f'Wrong result for {seq}\n'
                                            f'Expected: {answer}\n',
                                            f'But got: {result}\n',
                                            f'Target: {target}')
    print('Done! All tests passed!')


if __name__ == '__main__':
    main()
