# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        line = input().split()
        command = line[0]
        if command == "insert":
            ans.insert(int(line[1]), int(line[2]))
        elif command == "print":
            print(ans)
        elif command == "remove":
            ans.remove(int(line[1]))
        elif command == "append":
            ans.append(int(line[1]))
        elif command == "sort":
            ans.sort()
        elif command == "pop":
            ans.pop(-1)
        elif command == "reverse":
            ans.sort(reverse=True)
            
