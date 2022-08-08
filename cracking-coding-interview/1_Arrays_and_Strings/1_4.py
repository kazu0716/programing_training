from collections import defaultdict


class Solutions:
    def solve1(self, s: str) -> bool:
        """
        Use default dict

        Time complexity: O(N)
        Memory Space: O(N)
        """
        cnt = defaultdict(int)
        for ss in s:
            if ss == " ":
                continue
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
