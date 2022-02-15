class Solution:
    def isValid(self, s: str) -> bool:
        begin, end = ["[", "(", "{"], ["]", ")", "}"]
        stack = []
        for ss in s:
            if ss in begin:
                stack.append(ss)
            else:
                if stack and stack[-1] == begin[end.index(ss)]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    s = input()
    sol = Solution()
    print(sol.isValid(s))
