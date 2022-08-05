import random

def winOrLose(win,lose):
    for i in range(len(answerList)):
        for j in range(len(useAnswerList)):
            if (i==win and j==lose) or b==len(answerList) :
                return 0
        if len(answerList) == a:
            return 1

answer = random.randint(1000,9999)
answer = 1234

print('快來玩玩0A0B猜數字遊戲~')

start=True
while  start :
    useAnswer=input(f'請輸入{len(str(answer))}位數:')
    # str.isnumeric
    if len(str(answer)) != len(useAnswer):
        print('輸入長度不符唷')
        continue
    # useAnswer='4321'

    answerList=[]
    useAnswerList=[]

    a=0
    b=0

    for i in str(answer):
        answerList.append(i)
    for j in useAnswer:
        useAnswerList.append(j)

    for i in range(len(answerList)):
        # for j in range(len(useAnswerList)):
        if (answerList[i] == useAnswerList[i]):
            a+=1
            answerList[i]='-'

    for i in range(len(answerList)):
        if  (useAnswerList[i] in answerList) and (answerList[i] != useAnswerList[i]):
            b+=1
            answerList[i]='-'

    winOrLoseAns=winOrLose(a,b)
    if winOrLoseAns == 0:
        print(f'{a}A{b}B')
        print('不行要說欸，知道嗎?')

    if winOrLoseAns == 1:
        print(f'{a}A{b}B')
        print('還真有你的讚唷!')
        start=False