import random

def TryDraw():
    _list = []
    for _i in range(100):
        _list.append(_i + 1 )
    random.shuffle(_list) # 打亂 list index 順序 。

    startFind = 1 # 開始尋找次數累計
    findLimit = 50 # 最大連續的次數。
    _cycle = [] # 通過循環。

    for _j in range(len(_list)):
        _start = True
        _Parse = [] 

        if _list[_j] not in _cycle:
            _self = _list[_j]             # 持有數。
            _positSelf = _list[_self-1]   # 持有數，對應 index 數。
            _cycle.append(_self)          # 持有數，加入循環

            _Parse.append(_self)          # 持有數，加入比對 index[0]。 
            _Parse.append(_positSelf)     # 持有數，對應 index 數 加入比對 index[1]

            while _start:
                if startFind > findLimit:
                    print(f'一人違規，全員死亡')
                    return False

                if _Parse[0] == _Parse[1] :
                    startFind = 1
                    _start = False
                    continue

                if _Parse[0] != _Parse[1] :
                    if _Parse[1] not in _cycle:
                        _cycle.append(_Parse[1])

                    _newSelf = _Parse.pop(1)
                    _positSelf = _list[_newSelf - 1]
                    _Parse.append(_positSelf)
    
                    startFind += 1

    print(f'全員{len(_cycle)}名逃出')      
    return True

totalRunTimes = 0
successTimes = 0

while True:
    try:
        loopTimes = int(input('輸入增加次數:'))

        for i in range(loopTimes):
            thisTimeSuccess = TryDraw()
            if thisTimeSuccess:
                successTimes += 1
            totalRunTimes += 1

        successRate = round(float(successTimes) / float(totalRunTimes) * 100,1)
        print(f'一共逃出{totalRunTimes} 成功逃出次數{successTimes} 逃出機率{successRate}%')

    except Exception as e:
        print(e)