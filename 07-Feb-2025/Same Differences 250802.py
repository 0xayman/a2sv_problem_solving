# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t = int(input())


for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))

    count = 0
    freq = {}

    for i in range(n):
        key = ar[i] - i

        if key in freq:
            count += freq[key]

        freq[key] = freq.get(key, 0) + 1

    print(count)