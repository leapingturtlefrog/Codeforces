for t in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = int(input())
    if b - a[0] < a[0]:
        a[0] = b - a[0]
    for i in range(1, len(a)):
        num = b - a[i]
        if num >= a[i - 1] and num < a[i]:
            a[i] = num
        if not a[i] >= a[i - 1]:
            a[i] = num
        if not a[i] >= a[i - 1]:
            print('NO')
            break
    else:
        print('YES')
