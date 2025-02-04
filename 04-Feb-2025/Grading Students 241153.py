# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

t = int(input())
for _ in range(t):
    grade = int(input())
    difference = (10 - grade)  % 5
    if difference < 3 and grade >= 38:
        grade += difference
    
    print(grade)
        