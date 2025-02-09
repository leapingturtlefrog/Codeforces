def test(a):
    num = 0
    for i in range(2, 5):
        if a[i] == a[i-1] + a[i-2]:
            num += 1
    return num

for m in range(int(input())):
    a = list(map(int, input().split()))
    print(max(
        test(a[:2] + [a[0]+a[1]] + a[2:]),
        test(a[:2] + [a[2]-a[1]] + a[2:]),
        test(a[:2] + [a[3]-a[2]] + a[2:])
    ))
