import random
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from typing import Callable, Iterable, TypeVar

from tqdm import tqdm

from search import linear_search, binary_search

T = TypeVar('T')

SEARCH_NAME_TO_FUNC: dict[str, Callable[[Iterable[T], T], int | None]] = {
    'linear_search': linear_search,
    'binary_search': binary_search,
}


def true_search(sequence: list[T], target: T) -> T | None:
    try:
        return sequence.index(target)
    except ValueError:
        return None


def make_random_sequence(
        min: int,
        max: int,
        length: int,
        unique: bool = False
) -> list[int]:
    sequence = [random.randrange(min, max) for _ in range(length)]
    if unique:
        sequence = list(set(sequence))
    return sequence


def main(args: Namespace):
    test_seqs = [
        make_random_sequence(args.min, args.max, args.seq_length)
        for _ in range(args.n_tests)
    ]
    test_seqs.extend([
        [],
        [1],
        [1, 2],
        [0] * args.seq_length,
        sorted(make_random_sequence(args.min, args.max, args.seq_length)),
        sorted(make_random_sequence(args.min, args.max, args.seq_length),
               reverse=True),
        [random.randrange(args.min, args.max)] * args.seq_length,
        [random.randrange(args.min, args.max)] * 10**6,
    ])

    for seq in tqdm(test_seqs):
        if args.search == 'binary_search':
            seq = sorted(list(set(seq)))

        if len(seq) == 0:
            target = None
        else:
            random_idx = random.randrange(len(seq))
            target = seq[random_idx]

        search_result = SEARCH_NAME_TO_FUNC[args.search](seq, target)
        true_search_result = true_search(seq, target)
        assert search_result == true_search_result, (f'Wrong result for: {seq}\n'
                                                     f'Expected: {true_search_result}\n'
                                                     f'But got: {search_result}\n'
                                                     f'Target: {target}')

        target = args.max + 0xDEAD
        search_result = SEARCH_NAME_TO_FUNC[args.search](seq, target)
        true_search_result = true_search(seq, target)
        assert search_result == true_search_result, (f'Wrong result for: {seq}\n'
                                                     f'Expected: {true_search_result}\n'
                                                     f'But got: {search_result}\n'
                                                     f'Target: {target}')
    print('Done! All tests passed!')


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('search', type=str,
                        choices=list(SEARCH_NAME_TO_FUNC.keys()))
    parser.add_argument('--seq-length', type=int, default=100,
                        help='length of sequence to test sort')
    parser.add_argument('--max', type=int, default=100,
                        help='max value of random numbers in sequences')
    parser.add_argument('--min', type=int, default=-100,
                        help='min value of random numbers in sequences')
    parser.add_argument('--n-tests', type=int, default=100,
                        help='number of auto tests')

    command_line_args = parser.parse_args()
    main(command_line_args)
