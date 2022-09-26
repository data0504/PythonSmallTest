import random
import time
import keyboard
from enum import Enum

class UsePay:
    def __init__(self):
        self.selfPay = 0
        self.getCoin = 0
        self.rebate = 0

class Combo(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class SlotMachine:
    def __init__(self):
        self.size =  None
        self.coin = None
        self.useInitPay = UsePay()

        self.usePay = 0
        self.gameNumber = 0
        self.GameCarry  = False

        self.materialDesign = ['◐', '◑', '◒', '◓', '◔', '◕']
        self.materialAward = 300
        self.materialRebateLimit = 500
        self.materialRebateRate_one = 0.05
        self.materialRebateRate_two = 0.1

        self.rowResult = []
        self.columnResult = []
        self.comboGrand = []
        self.bigCombo = 0
        self.materialBG = []
    
    def setGameCondition(self, json):
        self.size =  json['size']
        self.coin = json['coin']
    
    def setUsePay(self, json):
        self.useInitPay.selfPay = json['pay']

    def clearData(self):
        self.rowResult = []
        self.columnResult = []
        self.comboGrand = []
        self.bigCombo = 0
        self.materialBG = []

    def title(self):
        print(f"卍 Slot machine 卍")

    def end(self):
        print(f"卍 歡迎再來致富 卍")

    def YesNo(self):
        while True:
            _uesAnswer = input(f"是否致富[Y/N]:")
            _correct = _uesAnswer=='N' or _uesAnswer=='Y'
            if _correct:
                if _uesAnswer == 'N':
                    print(f'不玩就不玩，活該你單身。')
                    return False
                if _uesAnswer == 'Y':
                    return True
            print(f'請好好回覆。')

    def useCoin(self):
        print(f' ')
        print(f'擁有 {self.useInitPay.selfPay }元。')
        _uesAnswer = input(f"一霸 {self.coin} 元，單次投入100元(含)以上，免拉霸:")
        __uesAnswer = int(_uesAnswer)
        _correct = self.useInitPay.selfPay >= __uesAnswer
        _wrong = self.useInitPay.selfPay < self.coin == False or __uesAnswer < self.coin
        if _correct:
            self.usePay += __uesAnswer
            self.gameNumber = __uesAnswer / self.coin

            if self.gameNumber >= 10:
                self.GameCarry = True

            self.useInitPay.selfPay = (self.useInitPay.selfPay - __uesAnswer)
            print(f' ')
            print(f'共可拉霸 {self.gameNumber }次。')
            return True

        print('沒錢滾。')
        return False
        
    def playing(self):
        print(f'單擊 空白鍵 啟動拉霸')
        _start = True
        while self.GameCarry :
                _start = False
                self.gameNumber -= 1
                return

        while _start :
            if keyboard.is_pressed('space') == True:
                self.gameNumber -= 1
                _start = False
  
    def assign(self, single):
        for _i in range(len(self.materialDesign)):
            if single == _i :
                _Design = self.materialDesign[ _i ]
                return _Design

    def drawGameResult(self):
        for _i in range(self.size):
            for _j in range(self.size):
                _single = random.randint(0,len(self.materialDesign)-1)
                self.rowResult.append(_single)

    def parse(self):
        for m in range(self.size):
            _grandtotal = 1
            _comboStart = True
            for n in range(self.size-1):
                _singleRemainList = self.rowResult [self.size + (self.size * n) : self.size + self.size + (self.size * n)]
                if _comboStart:
                    if self.rowResult[m] in _singleRemainList :
                        _comboStart = True
                        _grandtotal += 1
                    else:
                        _comboStart = False
                        break
            self.comboGrand.append(_grandtotal)

    def parseResult(self):
        # 解析 單次拉霸，最大Combo。
        for _i in range(len(self.comboGrand)):
            self.bigCombo = self.comboGrand[0]
            if self.comboGrand[_i] > self.bigCombo :
                self.bigCombo = self.comboGrand[_i]

        # 解析 單次拉霸 是否中大獎。
        if self.bigCombo == Combo.THREE.value:
            self.useInitPay.getCoin += self.materialAward

    def graph(self):
        print(f' ')
        for _i in range(self.size*self.size):
            self.materialBG.append(' ')
        for _k in range(self.size):
            _columnResult = []
            for _l in range(self.size):
                single = self.assign(self.rowResult[ _l + (self.size * _k)])
                self.materialBG[_k + ( self.size* _l)] = single
                for q in range( (_l * self.size) , self.size + (_l * self.size)) :
                    _columnResult.append(self.materialBG[q])

                time.sleep(0.1)
                print(' '.join(_columnResult))
                _columnResult= []
            print(f'-{_k+1}Column-')

    def graphResult(self):
        print(f' ')
        print(f'-Combo[{self.bigCombo}]-')
        print(f'-剩餘[{self.gameNumber}]次拉霸-')
        if self.bigCombo == Combo.ONE.value:
            print('贏要縮，輸要衝，再來！')
            
        if self.bigCombo == Combo.TWO.value:
            print('阿娘威，這種運氣，下回合豈不是中大獎。')

        if self.bigCombo == Combo.THREE.value:
            print(f'恭喜獲得{self.materialAward}')
            print('已涉及重大案件，請麻煩配合調查。')

    def rebateCount(self):
        print(f' ')
        if self.usePay < self.materialRebateLimit:
            self.useInitPay.rebate += self.usePay * self.materialRebateRate_one
            print(f'回饋金:消費:{self.usePay} X 回扣利率:{self.materialRebateRate_one}% = 獲得{self.useInitPay.rebate}元。')
        if self.usePay >= self.materialRebateLimit: 
            self.useInitPay.rebate += self.usePay * self.materialRebateRate_two
            print(f'回饋金:消費:{self.usePay} X 回扣利率:{self.materialRebateRate_two}% = 獲得{self.useInitPay.rebate}元。')
            
    def hint(self):
        print(f' ')
        if self.gameNumber == 0:
            self.GameCarry  = False
            if  self.usePay < self.materialRebateLimit:
                _remain= (self.materialRebateLimit - self.usePay)
                _useAnswer = input(f'再投幣{_remain }元，便能獲得{self.materialRebateRate_two }%回饋金。要再繼續致富? [Y/N]:')

            if  self.usePay >= self.materialRebateLimit:
                _useAnswer = input(f'已擁有{self.materialRebateRate_two}%回饋金，玩越多越致富。繼續嗎? [Y/N]:')

            if _useAnswer == 'Y':
                return True
            else:
                return False

    def information(self):
        print(f' ')
        print(f'--本次遊玩資訊--')
        print(f'錢包:{ self.useInitPay.selfPay}元。')
        print(f'中獎:{ self.useInitPay.getCoin}元')
        print(f'消費回饋:{ self.useInitPay.rebate}元')
        print(f' ')

    def Execution(self):
        while (self.gameNumber > 0) :
            self.clearData()
            self.playing()

            self.drawGameResult()
            self.parse()
            self.parseResult()

            self.graph()
            self.graphResult()
        else:
            if self.hint():
                if self.useCoin():
                    self.Execution()
                else:
                    self.GameStop()
            else:        
                self.GameStop()

    def GameStart(self):
        self.title()
        if self.YesNo():
            self.useCoin()
            self.Execution()
    
    def GameStop(self):
        self.rebateCount()
        self.information()
        self.end()

SM = SlotMachine()

GameCondition = {"size" :3, "coin" :10}
SM.setGameCondition(GameCondition)

GameUserInitCondition = {"pay":500}
SM.setUsePay(GameUserInitCondition)

SM.GameStart()