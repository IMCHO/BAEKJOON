import sys

num = int(sys.stdin.readline().rstrip())
# print(0 if num % 4 != 0 else 1 if (num % 100 != 0 or num % 400 == 0) else 0)
print(num % 4 != 0 and 0 or (num % 100 != 0 or num % 400 == 0) and 1 or 0)