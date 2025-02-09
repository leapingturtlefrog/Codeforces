import sys
from bisect import bisect_left

data = sys.stdin.read().split()
t = int(data[0])
idx = 1
ans = []

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    a = list(map(int, data[idx:idx + n]))
    idx += n
    b = sorted(map(int, data[idx:idx + m]))
    idx += m
    a[0] = min(a[0], b[0] - a[0])
    for i in range(1, n):
        spot = bisect_left(b, a[i - 1] + a[i])
        if spot == m:
            spot -= 1
        num = b[spot] - a[i]
        if num >= a[i - 1] and num < a[i]:
            a[i] = num
        elif a[i] < a[i - 1]:
            a[i] = num
        if a[i] < a[i - 1]:
            ans.append('NO')
            break
    else:
        ans.append('YES')
sys.stdout.write("\n".join(ans) + "\n")
