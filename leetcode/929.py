from typing import List, Set


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret: Set[str] = set()
        for email in emails:
            components = email.split("@")
            local = components[0].split("+")[0].replace(".", "")
            ret.add(local+"@"+components[1])
        return len(ret)


if __name__ == "__main__":
    sol = Solution()
    emails = list(list(input().replace("[", "").replace("]", "").replace("\"", "").split(",")))
    print(sol.numUniqueEmails(emails))
