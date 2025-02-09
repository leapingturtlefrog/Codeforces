def add_to(i, *args):
    for idx in args:
        sol[idx] |= 1 << i

def find_two_smallest():
    if sol[0] < sol[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0
    if sol[2] < sol[min1]:
        min1, min2 = 2, min1
    elif sol[2] < sol[min2]:
        min2 = 2
    return min1, min2

for m in range(int(input())):
    l, r = [int(x) for x in input().split(' ')]
    length = len(bin(r)) - 2
    ones_found = 0
    to_add = 0
    for i in range(length - 1, -1, -1):
        left_bit = (l >> i) & 1
        right_bit = (r >> i) & 1
        if left_bit == right_bit == 1:
            to_add |= 1 << i
        else:
            ones_found = length - i - 1
            break
    sol = [to_add] * 3
    for i in range(length - ones_found - 1, -1, -1):
        left_bit = (l >> i) & 1
        right_bit = (r >> i) & 1
        min1, min2 = find_two_smallest()
        if (sol[min2] | (1 << i)) <= r:
            if sol[min2] == sol[min1]:
                add_to(i, min1)
            else:
                add_to(i, min1, min2)
        elif (sol[min1] | (1 << i)) <= r:
            add_to(i, min1)
    print(sol[0], sol[1], sol[2])