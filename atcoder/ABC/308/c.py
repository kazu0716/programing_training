class CoinToss(object):
    def __init__(self, idx, success, failure):
        self.idx = idx
        self.success = success
        self.failure = failure

    def __lt__(self, other):
        x1 = self.success * (self.failure + other.failure)
        x2 = self.failure * (self.success + other.success)
        if x1 == x2:
            return self.idx > other.idx
        return x1 < x2


N = int(input())
people = []
for i in range(N):
    A, B = map(int, input().split())
    coin_toss = CoinToss(i + 1, A, B)
    people.append(coin_toss)
print(*[p.idx for p in sorted(people, reverse=True)])
