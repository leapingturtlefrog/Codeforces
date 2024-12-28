output = ''
for _ in range(int(input())):
    length = int(input())
    arr = []
    for _ in range(length):
        arr += [[int(x) for x in input().split(' ')]]
    for i in range(length):
        for val in range(arr[i][0], arr[i][1] + 1):
            unique = True
            for m in range(i):
                if arr[m] == [val, val]:
                    unique = False
            for m in range(i+1, length):
                if arr[m] == [val, val]:
                    unique = False
            if unique:
                output += '1'
                break
        if not unique:
            output += '0'
    output += '\n'
print(output[:-1])