class Solutions:
    def solve1(self, s: str) -> str:
        """
        Use replace method

        Time complexity: O(N)
        Memory Space: O(1)
        """
        return s.replace(" ", "%20")

    def solve2(self, s: str) -> str:
        """
        Don't use replace method

        Time complexity: O(N)
        Memory Space: O(1)
        """
        s = list(s)
        for i, ss in enumerate(s):
            if ss == " ":
                s[i] = "%20"
        return "".join(s)


if __name__ == "__main__":
    """
    URLify: Write a method to replace all spaces in a string with'%20'You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string, (Note: if implementing in Java, please use a character array so that you can
    perform this operation in place.)

    EXAMPLE
    Input: "Mr John Smith
    Output: "Mr%20John%20Smith
    """
    S = input()
    sol = Solutions()
    print("solve1", sol.solve1(S))
    print("solve2", sol.solve2(S))
