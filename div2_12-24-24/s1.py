output = []
for _ in range(int(input())):
    val = int(input())
    counter = 1
    while val > 3:
        counter *= 2
        val //= 4
    output += [str(counter)]
print('\n'.join(output))