dial = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5, "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9}
print(sum((value+1) for s in input() for key,value in dial.items() if key.count(s)==1))
# string = input()
# result = 0
# for s in string:
#     for key, value in dial.items():
#         if key.count(s) == 1:
#             result += (value + 1)
#             break
# print(result)