from typing import Set


def solve1(string: str) -> bool:
    """
    Use set pattern

    Time complexity: O(N)
    Memory Space: O(1)
    """
    string_set: Set[str] = set()
    for s in string:
        if s in string_set:
            return True
        string_set.add(s)
    return False


def solve2(string: str) -> bool:
    """
    Brute Force 

    Time complexity: O(N^2)
    Memory Space: O(1)
    """
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return True
    return False


def solve3(string: str) -> bool:
    """
    Use sort 

    Time complexity: O(N^2)
    Memory Space: O(N)
    """
    string_list = sorted(string)
    for i in range(len(string_list)-1):
        if string[i] == string[i+1]:
            return True
    return False


if __name__ == "__main__":
    S = input()
    print(solve1(S))
    print(solve2(S))
    print(solve3(S))
