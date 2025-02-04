# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
ar = list(map(int, input().split()))

res = [0] * n
for i in range(n):
    res[ar[i] - 1] = i + 1  
print(*res)