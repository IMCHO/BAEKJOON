num = int(input())
cases = []
for i in range(num):
    cases.append(input())

for case in cases:
    quiz = dict()
    score = 0
    for result in case:
        if 'O' in result:
            quiz["O"] = quiz.get("O", 0) + 1
            score+=quiz['O']
        else:
            quiz["O"] = 0
    
    print(score)
