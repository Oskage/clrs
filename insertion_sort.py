from copy import deepcopy
import random

from tqdm import tqdm

MAX_VALUE = 100
SEQ_LEN = 100
N_TESTS = 100


def insertion_sort(sequence):
    sequence = deepcopy(sequence)
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i >= 0 and sequence[i] > key:
            sequence[i + 1] = sequence[i]
            i -= 1
        sequence[i + 1] = key
    return sequence


def reversed_insertion_sort(sequence):
    sequence = deepcopy(sequence)
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i >= 0 and sequence[i] < key:
            sequence[i + 1] = sequence[i]
            i -= 1
        sequence[i + 1] = key
    return sequence


def main():
    for _ in tqdm(range(N_TESTS)):
        sequence = [random.randrange(100) for _ in range(SEQ_LEN)]
        sorted_sequence = insertion_sort(sequence)
        assert sorted_sequence == sorted(sequence), 'Wrong sort'
        reversed_sorted_sequence = reversed_insertion_sort(sequence)
        assert reversed_sorted_sequence == sorted(sequence, reverse=True), 'Wrong reverse sort'
        
    print('Done! All tests passed!')


if __name__ == '__main__':
    main()