def linear_search(sequence, target):
    for idx, value in enumerate(sequence):
        if value == target:
            return idx
    return None
