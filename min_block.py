import math

def min_block(s: str) -> int:
    """Given a string, return the length of the smallest "block" in the string.
    A block is a run of adjacent chars that are the same.
    """
    if not s:
        return 0

    min_len = math.inf
    current_char = s[0]
    current_len = 1

    for c in s[1:]:
        if c == current_char:
            current_len += 1
        else:
            if current_len < min_len:
                min_len = current_len
            current_char = c
            current_len = 1

    if current_len < min_len:
        min_len = current_len

    return min_len # type: ignore

if __name__ == "__main__":
    assert min_block("aaabbbaaccc") == 2
    assert min_block("xxyyyyyz") == 1
    assert min_block("aaaaa") == 5
