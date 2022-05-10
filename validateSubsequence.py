def isValidSubsequence(array, sequence):
    sequence_index = 0
    for number in array:
        if number == sequence[sequence_index]:
            if sequence_index == len(sequence) - 1:
                return True
            sequence_index += 1
    return False
