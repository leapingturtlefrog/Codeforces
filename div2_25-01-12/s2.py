for t in range(int(input())):
    n = int(input())
    diffs = [ai - bi for ai, bi in zip(list(map(int, input().split())), list(map(int, input().split())))]
    smallest = float('inf')
    sec_smallest = float('inf')
    for num in diffs:
        if num < smallest:
            sec_smallest = smallest
            smallest = num
        elif num < sec_smallest:
            sec_smallest = num
    if smallest >= 0:
        print('YES')
    elif sec_smallest > 0:
        if sec_smallest + smallest >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    subtraction = 0
    smallest_dif = 10**10
    to_print = 'YES'
    for i in range(n):
        dif = a[i] - b[i]
        if dif < 0 and subtraction == 0:
            subtraction -= dif
        elif dif <= 0 and subtraction > 0:
            to_print = 'NO'
            break
        elif dif < smallest_dif:
            smallest_dif = dif
        if smallest_dif - subtraction < 0:
            to_print = 'NO'
            break
    print(to_print)