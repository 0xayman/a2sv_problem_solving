# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

for i in range(5):
    line = input().split()
    for j in range(5):
        if line[j] == "1":
            distance = abs(j - 2) + abs(i - 2)
print(distance)