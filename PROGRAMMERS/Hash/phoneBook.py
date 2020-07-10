def solution(phone_book):
    for index1, value1 in enumerate(phone_book):
        for index2, value2 in enumerate(phone_book):
            if index1 == index2: continue
            if value1.startswith(value2):
                return False
    return True
