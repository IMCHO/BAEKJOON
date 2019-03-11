loc = int(input())
line = 1
while loc > line:
    loc -= line
    line += 1
if line % 2 == 0:
    print("{0}/{1}".format(loc, line + 1 - loc))
else:
    print("{0}/{1}".format(line + 1 - loc, loc))
