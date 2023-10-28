from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def distinct_permutations(s):
    if len(s) == N and s not in pattern:
        pattern.add(s)
        return

    for c in set(strings):
        if c == "." and s.count(".") < 2:
            distinct_permutations(s + c)
        if c != "." and c not in s:
            distinct_permutations(s + c)


def dfs(rows: list[str], first_columns: list[str]):
    if len(rows) >= N:
        columns = [""] * N
        for i, r in enumerate(rows):
            for j, c in enumerate(r):
                columns[j] += c
        for c in columns:
            if "A" not in c or "B" not in c or "C" not in c:
                return
        if first_columns != list(C):
            return
        print("Yes")
        exit(print(*rows, sep="\n"))

    for row in all_rows[len(rows)]:
        is_ok = True
        cur_first_columns = first_columns.copy()
        for i, c in enumerate(row):
            if cur_first_columns[i] == "" and c != ".":
                if c != C[i]:
                    is_ok = False
                    break
                else:
                    cur_first_columns[i] = c
        if is_ok:
            dfs(rows + [row], cur_first_columns)


N = int(input())
R = input()
C = input()
strings = "ABC"
strings += "." * (N - len(strings))
pattern: set[str] = set()
distinct_permutations("")
all_rows: list[list[str]] = [[] for _ in range(N)]
for row in pattern:
    c = row.replace(".", "")[0]
    for i, r in enumerate(R):
        if r == c:
            all_rows[i].append(row)
dfs([], [""] * N)
print("No")
