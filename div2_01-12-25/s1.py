for t in range(int(input())):
    n, a, b = [int(x) for x in input().split()]
    if (a - b) % 2 == 0:
        print('YES')
    else:
        print('NO')
