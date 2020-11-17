import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    string = sys.stdin.readline().strip()
    isVPS = True
    stack = []
    for c in string:
        if c == ")":
            if len(stack) == 0:
                isVPS = False
                break
            else:
                stack.pop()
        else:
            stack.append(c)

    if len(stack) != 0:
        isVPS = False

    if isVPS:
        print("YES")
    else:
        print("NO")
