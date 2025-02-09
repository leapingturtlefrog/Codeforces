for t in range(int(input())):
    s = input()
    last = s[0]
    for i in range(1, len(s)):
        if s[i] == last:
            print(1)
            break
        last = s[i]
    else:
        print(len(s))
