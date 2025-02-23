# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

from collections import Counter
 
t = int(input())
 
for _ in range(t):
    n, m = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    maxes = []
    curr_max = max(arr)
    for _ in range(m):
        symbols = input().split()
        op = symbols[0]
        l = int(symbols[1])
        r = int(symbols[2])
        if curr_max >= l and curr_max <= r:
            if op == "+":
                curr_max += 1
            else:
                curr_max -= 1
        maxes.append(curr_max)
    print(*maxes)