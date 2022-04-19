from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            w, d = 0, 1
            for i in range(len(weights)):
                if w + weights[i] > cap:
                    d += 1
                    if d > days or weights[i] > cap:
                        return False
                    w = weights[i]
                else:
                    w += weights[i]
            return True

        low, high = max(weights)-1, sum(weights)+1
        while high - low > 1:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid
        return high


if __name__ == "__main__":
    sol = Solution()
    weights = [1, 2, 3, 1, 1]
    days = 4
    print(sol.shipWithinDays(weights, days))
