from collections import defaultdict
from curses.ascii import isalpha


class Solutions:
    def solve1(self, s: str) -> bool:
        """
        Use default dict

        Time complexity: O(N)
        Memory Space: O(1)
        """
        cnt = defaultdict(int)
        for ss in s:
            if ss.isalpha():
                cnt[ss.lower()] += 1
        if len(s) % 2 == 0:
            for k in cnt:
                if cnt[k] % 2 != 0:
                    return False
            return True
        else:
            odds = 0
            for k in cnt:
                if cnt[k] % 2 != 0:
                    odds += 1
                if odds > 1:
                    return False
            return True

    def solve2(self, s: str) -> bool:
        """
        Use bits

        Time complexity: O(N)
        Memory Space: O(1)
        """
        # NOTE: input string only lower letter
        bits = [0]*26
        for ss in s:
            if ss.isalpha():
                idx = ord(ss.lower()) - 97
                bits[idx] = not bits[idx]
        n = 0
        for i in range(len(bits)):
            n += bits[i] * pow(2, len(bits) - 1 - i)
        return (len(s) % 2 == 0 and n == 0) or (len(s) % 2 == 1 and (n-1) & n == 0)


if __name__ == "__main__":
    """
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of
    a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, A
    permutation is a rearrangement of letters. The palindrome does not need to be limited to just
    dictionary words.

    EXAMPLE
    Input: Tac t Coa
    Output: True (permutations: "taco cat" "atc o eta" etc.)
    """
    S = input()
    sol = Solutions()
    print("solve1", sol.solve1(S))
    print("solve2", sol.solve2(S))
