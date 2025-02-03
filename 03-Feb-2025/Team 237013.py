# Problem: Team - https://codeforces.com/contest/231/problem/A

problems = int(input())
solve = 0
for _ in range(problems):
    ar = list(map(int, input().split()))
    if sum(ar) >= 2:
        solve += 1
    
print(solve)