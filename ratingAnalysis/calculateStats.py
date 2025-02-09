import ast
import sys
import matplotlib.pyplot as plt
import seaborn as sns

year = sys.argv[1]
rating = int(sys.argv[2])
with open('data' + year + '.txt') as f:
    data = ast.literal_eval(f.read())
minimum = min(data.keys())
maximum = max(data.keys())
total_users = sum(data.values())
arr, sums_proportion = [0] * (maximum - minimum + 1), [0] * (maximum - minimum + 1)

for pair in zip(data.keys(), data.values()):
    arr[pair[0]] = pair[1]

curr_total = 0
for i in range(len(arr)):
    curr_total += arr[i]
    sums_proportion[i] = curr_total / total_users
users_at_or_below = int(sums_proportion[rating - minimum - 1] * total_users)

print('year:', year)
print('rating:', rating, '\n')

print('total users:', total_users)
print('users at or below:', users_at_or_below)
print('users above:', total_users - users_at_or_below)
print('percentile:', users_at_or_below / total_users * 100)

plt.plot(
    [x for x in range(minimum, maximum + 1)],
    sums_proportion
)
plt.show()

sns.plot()