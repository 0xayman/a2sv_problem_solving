# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

t = int(input())

for _ in range(t):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(f"{s[0]}{len(s) - 2}{s[-1]}")