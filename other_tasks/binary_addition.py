import random
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace

from tqdm import tqdm


def binary_add(first: list[int], second: list[int]) -> list[int]:
    result = [0] * (len(first) + 1)
    is_overflow = False
    for bit_idx in range(len(first) - 1, -1, -1):
        if first[bit_idx] and second[bit_idx]:
            if is_overflow:
                result[bit_idx + 1] = 1
            else:
                result[bit_idx + 1] = 0
            is_overflow = True
        elif first[bit_idx] or second[bit_idx]:
            if is_overflow:
                result[bit_idx + 1] = 0
                is_overflow = True
            else:
                result[bit_idx + 1] = 1
        else:
            if is_overflow:
                result[bit_idx + 1] = 1
                is_overflow = False
            else:
                result[bit_idx + 1] = 0
    result[0] = int(is_overflow)
    return result


def number_to_binary_list(number: int, num_bits: int) -> list[int]:
    return [int(bit) for bit in bin(number)[2:].zfill(num_bits)]


def binary_list_to_number(binary_list: list[int]) -> int:
    return int(''.join([str(bit) for bit in binary_list]), base=2)


def main(args: Namespace):
    test_numbers = [
        [random.randrange(args.max), random.randrange(args.max)]
        for _ in range(args.n_tests)
    ]

    num_bits = len(f'{args.max:b}')

    for (first, second) in tqdm(test_numbers):
        true_result = first + second
        result = binary_list_to_number(
            binary_add(
                number_to_binary_list(first, num_bits),
                number_to_binary_list(second, num_bits)
            )
        )

        assert result == true_result, (f'Wrong result for {first} + {second}\n'
                                       f'Expected: {true_result}\n',
                                       f'But got: {result}')
    print('Done! All tests passed!')


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--max', type=int, default=100,
                        help='max value of random numbers in sequences')
    parser.add_argument('--n-tests', type=int, default=100,
                        help='number of auto tests')

    command_line_args = parser.parse_args()
    main(command_line_args)
