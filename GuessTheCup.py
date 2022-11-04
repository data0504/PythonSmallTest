import random
import time

def printTitle():
    _ues = input('是否開始遊戲 [Y] or [N]:')
    if _ues == 'Y':
        start = True
    else:
        start = False
        

    return start

def useAns():
     _uesAns = int(input('請猜球在哪個杯子，輸入:1為左杯、3為中杯、5為右杯'))
     return _uesAns

def offCup(row,column):
    _odd = [1,3,5]
    if row == 0:
        if column in _odd:
            return '  '
    if row == 1:
        if column in _odd:
            return ' _ '
    if row == 2:
        if column in _odd:
            return '[ ]'
    if row == 3:
        if column in _odd:
            return '[_]'
    return ''

def onCup(row,column):
    _odd = [1,3,5]

    if (column==cupAll[0]) and ball[0] == cupAll[0]:
        if row == 0:
            if column in _odd:
                return ' _ '
        if row == 1:
            if column in _odd:
                return '[ ]'
        if row == 2:
            if column in _odd:
                return '[_]'
        if row == 3:
            return ' 0 '
        return ''

    if (column==cupAll[1]) and ball[0] == cupAll[1]:
        if row == 0:
            if column in _odd:
                return '  _ '
        if row == 1:
            if column in _odd:
                return '[ ]'
        if row == 2:
            if column in _odd:
                return '[_]'
        if row == 3:
            return ' 0 '
        return ''

    if (column==cupAll[2]) and ball[0] == cupAll[2]:
        if row == 0:
            if column in _odd:
                return '   _ '
        if row == 1:
            if column in _odd:
                return '[ ]'
        if row == 2:
            if column in _odd:
                return '[_]'
        if row == 3:
            return ' 0 '
        return ''
    else:
        return offCup(row,column)

def moveCup(row,column):
    _odd = [1,3,5]
    if row == 0:
        if column in _odd:
            return '  '
    if row == 1:
        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 3:
            return '   _ '
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 5:
            return '   _ '
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 3:
            return ' _   '
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 1:
            return ' _   '

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 5:
            return '   _ '
        if (column==cupAll[2]) and ball[1] == 5 and ball[0] == 1:
            return ' _   '
        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 1:
            return '   _ '
        if (column==cupAll[2]) and ball[1] == 1 and ball[0] == 5:
            return ' _   '

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 1:
            return ' _ '
        if (column==cupAll[1]) and ball[0] == 1 and ball[1] == 1:
            return '   _ '
        if (column==cupAll[2]) and ball[0] == 1 and ball[1] == 1:
            return ' _  '

        if (column==cupAll[0]) and ball[0] == 3 and ball[1] == 3:
            return '   _ '
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 3:
            return ' _ '
        if (column==cupAll[2]) and ball[0] == 3 and ball[1] == 3:
            return ' _  '

        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 5:
            return '   _ '
        if (column==cupAll[1]) and ball[0] == 5 and ball[1] == 5:
            return ' _  '
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 5:
            return '  _ '


        if column in _odd:
            return ' _ '
    if row == 2:
        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 3:
            return '-=[ ]'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 5:
            return '-=[ ]'
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 3:
            return '[ ]=-'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 1:
            return '[ ]=-'

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 5:
            return '-=[ ]'
        if (column==cupAll[2]) and ball[1] == 5 and ball[0] == 1:
            return '[ ]=-'
        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 1:
            return '-=[ ]'
        if (column==cupAll[2]) and ball[1] == 1 and ball[0] == 5:
            return '[ ]=-'

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 1:
            return '[ ]'
        if (column==cupAll[1]) and ball[0] == 1 and ball[1] == 1:
            return '-=[ ]'
        if (column==cupAll[2]) and ball[0] == 1 and ball[1] == 1:
            return '[ ]=-'

        if (column==cupAll[0]) and ball[0] == 3 and ball[1] == 3:
            return '-=[ ]'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 3:
            return '[ ]'
        if (column==cupAll[2]) and ball[0] == 3 and ball[1] == 3:
            return '[ ]=-'

        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 5:
            return '-=[ ]'
        if (column==cupAll[1]) and ball[0] == 5 and ball[1] == 5:
            return '[ ]=-'
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 5:
            return '[ ]'

        if column in _odd:
            return '[ ]'
    if row == 3:
        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 3:
            return '-=[_]'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 5:
            return '-=[_]'
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 3:
            return '[_]=-'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 1:
            return '[_]=-'

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 5:
            return '-=[_]'
        if (column==cupAll[2]) and ball[1] == 5 and ball[0] == 1:
            return '[_]=-'
        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 1:
            return '-=[_]'
        if (column==cupAll[2]) and ball[1] == 1 and ball[0] == 5:
            return '[_]=-'

        if (column==cupAll[0]) and ball[0] == 1 and ball[1] == 1:
            return '[_]'
        if (column==cupAll[1]) and ball[0] == 1 and ball[1] == 1:
            return '-=[_]'
        if (column==cupAll[2]) and ball[0] == 1 and ball[1] == 1:
            return '[_]=-'

        if (column==cupAll[0]) and ball[0] == 3 and ball[1] == 3:
            return '-=[_]'
        if (column==cupAll[1]) and ball[0] == 3 and ball[1] == 3:
            return '[_]'
        if (column==cupAll[2]) and ball[0] == 3 and ball[1] == 3:
            return '[_]=-'

        if (column==cupAll[0]) and ball[0] == 5 and ball[1] == 5:
            return '-=[_]'
        if (column==cupAll[1]) and ball[0] == 5 and ball[1] == 5:
            return '[_]=-'
        if (column==cupAll[2]) and ball[0] == 5 and ball[1] == 5:
            return '[_]'

        if column in _odd:
            return '[_]'
    return ''

def createScreeMoveStart():
    for row in range(high):
        view = []
        for column in range(width):
            show = moveCup(row,column)
            view.append(show)
        print(' '.join(view))

def createScreeMoveStop():
    CreateScreenOff()
    ballMove = createMove()
    ball.append(ballMove)

def CreateScreenOff():
    for row in range(high):
        view = []
        for column in range(width):
            show = offCup(row,column)
            view.append(show)
        print(' '.join(view))

def CreateScreenOn():
    for row in range(high):
        view = []
        for column in range(width):
            show = onCup(row,column)
            view.append(show)
        print(' '.join(view))

def createMove():
    _move = cupAll[random.randint(0,2)]
    return _move

def TransitionsMove(lock,Transitions,gaming):

    if len(ball) == 0:
        CreateScreenOff()
        ball.append(3)
        lock = True
        return lock,Transitions,gaming

    if lock == True :
        CreateScreenOn()
        lock = False
        return lock,Transitions,gaming

    if len(ball) == 1:
        CreateScreenOff()
        ballMove = createMove()
        ball.append(ballMove)
        Transitions = False
        gaming = True
        lock = True
        return lock,Transitions,gaming

def onCupOnly(row,column,Ans):
    _odd = [1,3,5]
    if Ans == 1:
        if (column==cupAll[0]) and ball[0] != Ans:
            if row == 0:
                if column in _odd:
                    return ' _ '
            if row == 1:
                if column in _odd:
                    return '[ ]'
            if row == 2:
                if column in _odd:
                    return '[_]'
            if row == 3:
                return ' _ '
            return ''
        else:
            return offCup(row,column)
    if Ans == 3:
        if (column==cupAll[1]) and ball[0] != Ans:
            if row == 0:
                if column in _odd:
                    return '  _ '
            if row == 1:
                if column in _odd:
                    return '[ ]'
            if row == 2:
                if column in _odd:
                    return '[ ]'
            if row == 3:
                return ' _ '
            return ''
        else:
            return offCup(row,column)
    if Ans == 5:
        if (column==cupAll[2]) and ball[0] != Ans:
            if row == 0:
                if column in _odd:
                    return '   _ '
            if row == 1:
                if column in _odd:
                    return '[ ]'
            if row == 2:
                if column in _odd:
                    return '[ ]'
            if row == 3:
                return ' _ '
            return ''
        else:
            return offCup(row,column)

def CreateScreenOnlyOn(Ans):
    for row in range(high):
        view = []
        for column in range(width):
            show = onCupOnly(row,column,Ans)
            view.append(show)
        print(' '.join(view))
        

cupAll=[1,3,5]
cupAllLoop=[]
ball=[]
for i in range(len(cupAll)):
    cupAllLoop.append(cupAll[i])
    if len(cupAllLoop) == len(cupAll):
        cupAllLoop.append(cupAll[0])

width = 6
high = 4
FPS = 0.3
lock = False

start = True
Transitions = True
gaming = False
_pvrTime = time.time()
pvrTime = time.time()
second = 5


start = printTitle()

while start:
    currentTime = time.time()
    passTime = currentTime - pvrTime

    if passTime > FPS:
        pvrTime = currentTime

        if Transitions :
            lock,Transitions,gaming = TransitionsMove(lock,Transitions,gaming)
            continue
            
        if gaming :
            _currentTime = time.time()
            _passTime = _currentTime - _pvrTime

            if _passTime < second:

                if len(ball) == 1:
                    createScreeMoveStop()
                    continue

                if lock :
                    createScreeMoveStart()
                    ball[0],ball[1]=ball[1],ball[0]
                    ball.pop(1)
                    continue
            
            if _passTime > second:
                Ans = useAns()
                if Ans != ball[0]:
                    CreateScreenOnlyOn(Ans)
                    print(' ')
                    print('~猜錯啦~')
                    print('~正確答案是~')
                    print(' ')
                    CreateScreenOn()
                    break
                else:
                    CreateScreenOn()
                    print('恭喜答對了')
                    start = False
                    break