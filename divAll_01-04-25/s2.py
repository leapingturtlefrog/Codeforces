for _ in range(int(input())):
    # max number of changes
    k = int(input().split(' ')[1])
    # array a
    a = [int(x) for x in input().split(' ')]
    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1
    lst = sorted(counts.values())
    min_idx, max_idx = 0, len(lst) - 1
    while k > 0 and min_idx < max_idx:
        min_count = lst[min_idx]
        if min_count <= k:
            k -= min_count
            min_idx += 1
        else:
            break
    print(max_idx - min_idx + 1)