M, D = map(int, input().split())
y, m, d = map(int, input().split())
# NOTE: 0-indexed
# ex. 1/1 -> 0/0, 1/2 -> 0/1, 2/1 -> 1/0
total_days = y * M * D + (m - 1) * D + d
nxt_year = total_days // (M * D)
nxt_month = 1 + (total_days % (M * D)) // D
nxt_day = 1 + (total_days % (M * D)) % D
print(nxt_year, nxt_month, nxt_day)
