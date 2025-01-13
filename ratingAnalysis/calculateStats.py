import ast
import sys

rating = int(sys.argv[2])
with open('data' + sys.argv[1] + '.txt') as f:
    data = ast.literal_eval(f.read())
minimum = min(data.keys())
maximum = max(data.keys())
arr = [0] * (maximum - minimum + 1)
totals = {
    'users at or below': 0,
    'users above': 0,
    'total users': 0
}
for pair in zip(data.keys(), data.values()):
    arr[pair[0]] = pair[1]
for i in range(len(arr)):
    totals['total users'] += arr[i]
    if i <= rating:
        totals['users at or below'] += arr[i]
    else:
        totals['users above'] += arr[i]
print(totals)