def is_nondecreasing(a):
    prev = a[0]
    ans = True
    for curr in a[1:]:
        if curr >= prev:
            prev = curr
        else:
            ans = False
            break
    return ans

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        m = min(a[i], a[i + 1])
        a[i] -= m
        a[i + 1] -= m
    if is_nondecreasing(a):
        print('YES')
    else:
        print('NO')
