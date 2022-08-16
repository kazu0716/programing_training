class Solutions:
    def solve1(self, s1: str, s2: str) -> bool:
        """
        Simple solution

        Time complexity: O(N)
        Memory Space: O(1)
        """
        if abs(len(s1) - len(s2)) >= 2:
            return False
        if len(s1) == len(s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                if cnt > 1:
                    return False
            return True
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i+cnt]:
                cnt += 1
            if cnt > 1:
                return False
        return True


if __name__ == "__main__":
    """
    One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bae -> false
    """
    sol = Solutions()
    s1, s2 = input(), input()
    print("solve1", sol.solve1(s1, s2))
