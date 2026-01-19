import math


def min_block(tekst):
    if not tekst:
        return 0

    min_len = math.inf
    current_char = tekst[0]
    current_len = 1

    for character in tekst[1:]:
        if character == current_char:
            current_len += 1
        else:
            if current_len < min_len:
                min_len = current_len
            current_char = character
            current_len = 1

    if current_len < min_len:
        min_len = current_len

    return min_len  # type: ignore


def min_block2(s):
    if not s:
        return 0

    min_len = float("inf")
    current_len = 1

    # Iterate starting from the second character
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Same as previous char, extend the block
            current_len += 1
        else:
            # New character found, check if the previous block was the smallest
            if current_len < min_len:
                min_len = current_len
            # Reset counter for the new block
            current_len = 1

    # CRITICAL: Check the length of the very last block after the loop finishes
    if current_len < min_len:
        min_len = current_len

    return min_len


if __name__ == "__main__":
    assert min_block("aaabbbaaccc") == 2
    assert min_block("xxyyyyyz") == 1
    assert min_block("aaaaa") == 5
