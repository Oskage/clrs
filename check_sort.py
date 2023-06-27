import random
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from tqdm import tqdm

from sort import insertion_sort

SORT_NAME_TO_FUNC = {
    'insertion_sort': insertion_sort,
}


def main(args):
    test_seqs = [
        [random.randrange(args.min, args.max) for _ in range(args.seq_length)] 
        for _ in range(args.n_tests)
    ]
    test_seqs.extend([
        [], 
        [1], 
        [1, 2], 
        [0] * args.seq_length,
        sorted([random.randrange(args.min, args.max) for _ in range(args.seq_length)]),
        sorted([random.randrange(args.min, args.max) for _ in range(args.seq_length)], 
               reverse=True),
        [random.randrange(args.min, args.max)] * args.seq_length,
        [random.randrange(args.min, args.max)] * 10**6,
    ])
    
    for seq in tqdm(test_seqs):
        sorted_seq = SORT_NAME_TO_FUNC[args.sort](seq)
        true_sorted_seq = sorted(seq)
        assert sorted_seq == true_sorted_seq, (f'Wrong result for: {seq}\n'
                                               f'Expected: {true_sorted_seq}\n'
                                               f'But got: {sorted_seq}')
        
        sorted_seq = SORT_NAME_TO_FUNC[args.sort](seq, reverse=True)
        true_sorted_seq = sorted(seq, reverse=True)
        assert sorted_seq == true_sorted_seq, (f'Wrong result for: {seq}\n'
                                               f'Expected: {true_sorted_seq}\n'
                                               f'But got: {sorted_seq}')
    print('Done! All tests passed!')


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('sort', type=str, choices=['insertion_sort'])
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
