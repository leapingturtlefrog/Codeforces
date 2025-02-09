for m in range(int(input())):
    # rows, cols
    n, m = [int(x) for x in input().split(' ')]
    print(1 + max(n, m))