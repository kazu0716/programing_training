from collections import defaultdict
from enum import IntEnum


class PersonStatus(IntEnum):
    NOT_CALLED = 0
    CALLED = 1
    GONE = 2


N, Q = map(int, input().split())
status = defaultdict(lambda: PersonStatus.NOT_CALLED)
not_called_pos, called_pos = 1, 1
ans = []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        while status[not_called_pos] != PersonStatus.NOT_CALLED:
            not_called_pos += 1
        status[not_called_pos] = PersonStatus.CALLED
    elif query[0] == "2":
        status[int(query[1])] = PersonStatus.GONE
    else:
        while status[called_pos] != PersonStatus.CALLED:
            called_pos += 1
        ans.append(called_pos)
print(*ans, sep="\n")
