for t in range(int(input())):
    n, k = list(map(int, input().split()))
    m = sorted(list(map(int, input().split())))
    i, j = 0, len(m) - 1
    ans = 0
    while i < j:
        curr = m[j] + m[i]
        if curr > k:
            j -= 1
        elif curr < k:
            i += 1
        else:
            ans += 1
            i += 1
            j -= 1
    print(ans)
