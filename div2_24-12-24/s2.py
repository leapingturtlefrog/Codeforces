output = []
for _ in range(int(input())):
    n, d = [int(x) for x in input().split(' ')]
    curr_output = ['1']
    if n > 2 or d % 3 == 0:
        curr_output += '3'
    if d == 5:
        curr_output += '5'
    if n > 2 or d == 7:
        curr_output += '7'
    if n > 5 or d == 9 or (n > 2 and (d == 3 or d == 6)):
        curr_output += '9'
    output += [curr_output]
print('\n'.join([' '.join(line) for line in output]))