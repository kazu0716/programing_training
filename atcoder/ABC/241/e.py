N, K = map(int, input().split())
A = list(map(int, input().split()))
x, x_set = 0, set()
while x % N not in x_set:
    x_set.add(x % N)
    x += A[x % N]
x_list = list(x_set)
since = x_list.index(x % N)
loop = len(x_list) - since
loop_num = (K - since) // loop

i, ans = 0, 0
while K > 0 and i < since:
    ans += A[x_list[i]]
    i += 1
    K -= 1
while K > 0 and i < len(x_list):
    ans += A[x_list[i]] * loop_num
    i += 1
    K -= loop_num
i = since
while K > 0:
    ans += A[x_list[i]]
    i += 1
    K -= 1
print(ans)
