import requests
import time
import keyboard
from enum import Enum

class ClientObj: # GET Client self Tittle 物件
    def __init__(self):
        self.LoginOption = '01遊戲登入 ; 02遊戲註冊 ; 00離開:' # add 帳號刪除
        self.signUpTitle = '遊戲註冊'
        self.signInTitle = '遊戲登入'
        self.signInUpAccountTitle = '輸入帳號:'
        self.signInUpPasswordTitle = '輸入密碼:'
        self.GameOptionTitle = "請輸入遊戲代碼:"
        self.inputWrong = "輸入錯誤"
        self.GameOptionsAccount = '99.玩家資訊'
        self.pending = "遊戲維修中"

        self.GameOptionsEnd = '00.遊戲登出'
        self.UploadStateTrue = '玩家資訊上傳成功'
        self.UploadStateFalse = '存檔玩家資訊上傳失敗'
        
class Options(Enum): # GET Client self Option 物件
    ZERO =  '00'
    ONE =   '01'
    TWO =   '02'
    THREE = '03'
    NINE =  '99'
    
class ClientAttest:  #  Get server OnlineGame 物件
    def __init__(self):
        self.GameOptions = []
        self.size = 0
        self.coin = 0

class ClientPay: # Todo Get server ClientData 物件
    def __init__(self):
        self.AccountState = False 
        self.PasswordState = False 
        self.AccountToken = None

        self.pay = 0
        self.getCoin = 0
        self.rebate = 0

    def setAccountJsonIN(self,  receiveJson): 
        self.pay = receiveJson ['pay']
        self.getCoin = receiveJson['getCoin']
        self.rebate = receiveJson['rebate']
    
    def setAccountJsonOUT(self,  receiveJson): 
        self.pay = receiveJson ['pay']
        self.getCoin += receiveJson['getCoin']
        self.rebate += receiveJson['rebate']
        
    def getJson(self):
        return {"pay":self.pay, "getCoin":self.getCoin, "rebate":self.rebate, "AccountToken": self.AccountToken}

    def viewClientPay(self):
        print(f' ')
        print(f'--玩家資訊--')
        print(f'錢包總額:{ self.pay}元。')
        print(f'中獎金額:{ self.getCoin}元')
        print(f'消費回饋:{ self.rebate}元')
        print(f' ')

class SlotMachineCombo(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class SlotMachine:
    def __init__(self):
        self.ClientPay = 0
        self.ClientGetCoin = 0
        self.ClientRebate = 0

        self.sizeCondition =  3
        self.coinCondition = 10
        self.coinCurrencyCondition = 10

        self.clientPaying = 0
        self.gameFrequency = 0
        self.CurrencyCondition  = False

        self.materialDesign = ['◐', '◑', '◒', '◓', '◔', '◕']
        self.materialAwardCondition = 3
        self.materialAward = 300
        self.materialRebateLimit = 1000
        self.materialRebateRate_one = 0.05
        self.materialRebateRate_two = 0.1

        self.rowRandomResult = []
        self.columnResult = []
        self.comboGrand = []
        self.bigCombo = 0
        self.materialBG = []

    def setJson(self, ClientPayJson):
        self.ClientPay = ClientPayJson['pay']

    def getJson(self):
            return {"pay":self.ClientPay, "getCoin":self.ClientGetCoin, "rebate":self.ClientRebate}
    
    def initGameCount(self):
        self.ClientPay = 0
        self.ClientGetCoin = 0
        self.ClientRebate = 0

        self.clientPaying = 0
        self.gameFrequency = 0
        self.CurrencyCondition  = False

    def InitGameCondition(self):
        self.rowRandomResult = []
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
        print(f'擁有 {self.ClientPay }元。')
        _wrong = True
        while _wrong:
            _clientPlayCoin = input(f"一霸 {self.coinCondition} 元，單次投入100元(含)以上，免拉霸:")
            _clientPlayCoinINT = int(_clientPlayCoin)
            _correct = (self.ClientPay >= self.coinCondition) or (self.ClientPay >= _clientPlayCoinINT)
            _wrong = _correct == False 

            if _correct:
                self.clientPaying += _clientPlayCoinINT
                self.ClientPay = (self.ClientPay - _clientPlayCoinINT)
                _recv = requests.post('http://127.0.0.1:5000/StartGameFrequencyProtocol',
                                        json = {'ClientPlayCoin':_clientPlayCoinINT, 
                                                'CoinCondition':self.coinCondition, 
                                                'CoinCurrencyCondition':self.coinCurrencyCondition})
                _decodeJsonData = _recv.json()
                _frequency = _decodeJsonData['GameFrequency']
                _currency = _decodeJsonData['GameCurrency']
                
                self.gameFrequency = _frequency
                self.CurrencyCondition = _currency
                print(f' ')
                print(f'共可拉霸 {self.gameFrequency }次。')
                _wrong = False
                return True

        print('沒錢滾。')
        return False
        
    def playing(self):
        print(f'單擊 空白鍵 啟動拉霸')
        _start = True
        while self.CurrencyCondition :
                _start = False
                self.gameFrequency -= 1
                return

        while _start :
            if keyboard.is_pressed('space') == True:
                self.gameFrequency -= 1
                _start = False
  
    def assign(self, single):
        for _i in range(len(self.materialDesign)):
            if single == _i :
                _Design = self.materialDesign[ _i ]
                return _Design

    def GetServerRandomResult(self):
        _recv = requests.get('http://127.0.0.1:5000/slotMachineRandomResultProtocol',
                                json={'SizeCondition': self.sizeCondition, 
                                        'IndexCondition': len(self.materialDesign),
                                        'AwardCondition': self.materialAwardCondition })
        _decodeJsonData = _recv.json()
        _randomResult = _decodeJsonData['RandomResult']
        _bigCombo = _decodeJsonData['BigCombo']
        _awardState = _decodeJsonData['AwardState']

        self.rowRandomResult = _randomResult
        self.bigCombo = _bigCombo

        if _awardState:
            self.ClientGetCoin += self.materialAward

    def graph(self):
        print(f' ')
        for _i in range(self.sizeCondition*self.sizeCondition):
            self.materialBG.append(' ')
        for _k in range(self.sizeCondition):
            _columnResult = []
            for _l in range(self.sizeCondition):
                single = self.assign(self.rowRandomResult[ _l + (self.sizeCondition * _k)])
                self.materialBG[_k + ( self.sizeCondition* _l)] = single
                for q in range( (_l * self.sizeCondition) , self.sizeCondition + (_l * self.sizeCondition)) :
                    _columnResult.append(self.materialBG[q])

                time.sleep(0.1)
                print(' '.join(_columnResult))
                _columnResult= []
            print(f'-{_k+1}Column-')

    def graphResult(self):
        print(f' ')
        print(f'-Combo[{self.bigCombo}]-')
        print(f'-剩餘[{self.gameFrequency}]次拉霸-')
        if self.bigCombo == SlotMachineCombo.ONE.value:
            print('贏要縮，輸要衝，再來！')
            
        if self.bigCombo == SlotMachineCombo.TWO.value:
            print('阿娘威，這種運氣，下回合豈不是中大獎。')

        if self.bigCombo == SlotMachineCombo.THREE.value:
            print(f'恭喜獲得{self.materialAward}')
            print('已涉及重大案件，請麻煩配合調查。')

    def rebateCount(self):
        print(f' ')
        if self.clientPaying <= self.materialRebateLimit:
            self.ClientRebate += self.clientPaying * self.materialRebateRate_one
            print(f'回饋金:消費:{self.clientPaying} X 回扣利率:{self.materialRebateRate_one} = 獲得{self.ClientRebate}元。')
        if self.clientPaying > self.materialRebateLimit: 
            self.ClientRebate += self.clientPaying * self.materialRebateRate_two
            print(f'回饋金:消費:{self.clientPaying} X 回扣利率:{self.materialRebateRate_two} = 獲得{self.ClientRebate}元。')
            
    def hint(self):
        print(f' ')
        if self.gameFrequency == 0:
            self.CurrencyCondition  = False
            if  self.clientPaying <= self.materialRebateLimit:
                _remain= (self.materialRebateLimit - self.clientPaying)
                _useAnswer = input(f'再投幣{_remain }元，便能獲得{self.materialRebateRate_two }回饋金。要再繼續致富? [Y/N]:')

            if  self.clientPaying > self.materialRebateLimit:
                _useAnswer = input(f'已擁有{self.materialRebateRate_two}回饋金，玩越多越致富。繼續嗎? [Y/N]:')

            if _useAnswer == 'Y':
                return True
            else:
                return False

    def information(self):
        print(f' ')
        print(f'--遊戲結算--')
        print(f'錢包剩餘:{ self.ClientPay}元。')
        print(f'中獎金額:{ self.ClientGetCoin}元')
        print(f'消費回饋:{ self.ClientRebate}元')
        print(f' ')

    def Execution(self):
        while (self.gameFrequency > 0) :
            self.InitGameCondition()
            self.playing()

            self.GetServerRandomResult() # Server 運算結果。

            self.graph() # Client 逐格表演。
            self.graphResult() # Client 總結現況。
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
            self.useCoin() # Server 計算遊玩次數。
            self.Execution()
    
    def GameStop(self):
        self.rebateCount()
        self.information()
        self.end()