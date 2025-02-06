# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

strength, n = map(int, input().split())
dragons = []
for i in range(n):
    dragons.append(list(map(int, input().split())))

dragons.sort(key=lambda x: x[0])

for i in range(n):
    if strength > dragons[i][0]:
        strength += dragons[i][1]
    else:
        print("NO")
        break
else:
    print("YES")