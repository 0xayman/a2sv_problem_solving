# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())

base = "codeforces"
for _ in range(t):
    s = input().strip()
    count = 0
    for i in range(10):
        if s[i] != base[i]:
            count += 1

    print(count)