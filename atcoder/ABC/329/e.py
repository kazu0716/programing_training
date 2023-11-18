from collections import deque


def can_replace(s, t):
    if s == ["#"] * M:
        return False
    for ss, tt in zip(s, t):
        if ss != "#" and ss != tt:
            return False
    return True


N, M = map(int, input().split())
S = list(input())
T = list(input())
deq = deque([i for i in range(N - M + 1) if S[i:i + M] == T])
while deq:
    head = deq.popleft()
    S[head:head + M] = ["#"] * M
    for di in range(-M + 1, M + 1):
        if 0 > head + di or head + di > N - M:
            continue
        if can_replace(S[head + di:head + di + M], T):
            deq.appendleft(head + di)
print("Yes" if S == ["#"] * N else "No")
