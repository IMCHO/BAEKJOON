string = input().upper()
result = {}
for c in string:
    result[c] = result.get(c, 0) + 1
maxCount = max(result.values())
if list(result.values()).count(maxCount) > 1:
    print("?")
else:
    for key, value in result.items():
        if value == maxCount:
            print(key)
            break
# result2 = {}
# for key, value in result.items():
#     if result2.get(value, 0) == 0:
#         result2[value] = key
#     else:
#         result2[value] += key
#
# temp = max(result2.keys())
# if len(result2[temp]) > 1:
#     print("?")
# else:
#     print(result2[temp])
