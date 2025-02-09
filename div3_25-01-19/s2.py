for t in range(int(input())):
    n, m = list(map(int, input().split()))
    c = []
    for cowNum in range(n):
        for val in list(map(int, input().split())):
            c += [(val, cowNum)]
    c = sorted(c)
    p = [x[1] for x in c[:n]]
    correct = True
    if len(set(p)) != n:
        print(-1)
    else:
        for i in range(n, n*m):
            if c[i][1] != p[i % n]:
                correct = False
                break
        if correct:
            for i in range(n):
                print(p[i] + 1, end=' ' if i != n - 1 else '')
        else:
            print(-1, end='')
    print()