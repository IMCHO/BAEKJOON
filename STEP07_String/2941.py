# def checkCro(string, result):
#     checkFlag = False
#     for c in cro:
#         if string.find(c) != -1:
#             checkFlag = True
#             string = string.replace(c," ",1)
#             result += 1
#     return (checkFlag, string, result)
#

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string =input()
for c in cro:
    string=string.replace(c,"!")
print(len(string))
# result = 0
# tuple = checkCro(input(), result)
#
# while True:
#     result = tuple[2]
#     string = tuple[1]
#     if tuple[0] == True:
#         tuple = checkCro(string, result)
#     else:
#         break
# print(len(list(s for s in string if s != " ")) + result)
