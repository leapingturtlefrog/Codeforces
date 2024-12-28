def is_non_degenerate(arr):
    if min(arr) * 2 > max(arr):
        return True
    return False

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split(' ')]
    ans = 'NO'
    for i in range(len(arr) - 1):
        if is_non_degenerate(arr[i:i+2]):
            ans = 'YES'
            break
    print(ans)