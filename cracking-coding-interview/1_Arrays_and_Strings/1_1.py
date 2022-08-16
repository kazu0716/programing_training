from typing import Set


class Solutions:
    def solve1(self, string: str) -> bool:
        """
        Use set pattern

        Time complexity: O(N)
        Memory Space: O(N)
        """
        string_set: Set[str] = set()
        for s in string:
            if s in string_set:
                return True
            string_set.add(s)
        return False

    def solve2(self, string: str) -> bool:
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

    def solve3(self, string: str) -> bool:
        """
        Use sort 

        Time complexity: O(NlogN)
        Memory Space: O(N)
        """
        string_list = sorted(string)
        for i in range(len(string_list)-1):
            if string[i] == string[i+1]:
                return True
        return False


if __name__ == "__main__":
    """
    Is Unique: Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """
    S = input()
    sol = Solutions()
    print("solve1", sol.solve1(S))
    print("solve2", sol.solve2(S))
    print("solve3", sol.solve3(S))
