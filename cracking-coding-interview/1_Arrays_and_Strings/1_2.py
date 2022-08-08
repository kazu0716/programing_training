from collections import Counter


class Solutions():
    def solve1(self, s1: str, s2: str) -> bool:
        """
        Use Sort

        Time complexity: O(NlogN)
        Memory Space: O(N)
        """
        if len(s1) != len(s2):
            return False
        return sorted(list(s1)) == sorted(list(s2))

    def solve2(self, s1: str, s2: str) -> bool:
        """
        Use counter

        Time complexity: O(N)
        Memory Space: O(N)
        """
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)

    def solve3(self, s1: str, s2: str) -> bool:
        """
        Use counter, but optimized more solve2

        Time complexity: O(N)
        Memory Space: O(N)
        """
        if len(s1) != len(s2):
            return False
        counter = Counter(s1)
        for s in s2:
            counter[s] -= 1
            if counter[s] < 0:
                return False
        return True


if __name__ == "__main__":
    """
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
    """
    S1, S2 = input(), input()
    sol = Solutions()
    print("solve1", sol.solve1(S1, S2))
    print("solve2", sol.solve2(S1, S2))
    print("solve3", sol.solve2(S1, S2))
