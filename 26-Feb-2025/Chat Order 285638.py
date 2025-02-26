# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())

res = []
for _ in range(n):
    res.append(input())

visited = set()
for name in reversed(res):
    if name in visited:
        continue
    print(name)
    visited.add(name)