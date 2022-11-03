import requests
import time
import DataClass as DC

class ClientLogin:
    def __init__(self):
        self.ClientOption = DC.Options
        self.ClientObj = DC.ClientObj()
        self.ClientAttest = DC.ClientAttest()
        self.ClientPay = DC.ClientPay()
        self.ClientSlotMachine = DC.SlotMachine()
        
    def useSignInInput(self):
        _start = True
        while _start:
            print(self.ClientObj.signInTitle)
            _UseAccount = input(self.ClientObj.signInUpAccountTitle)
            _UsePassword = input(self.ClientObj.signInUpPasswordTitle)

            _recv = requests.post('http://127.0.0.1:5000/SignInAccountProtocol',
                                    json={'Account':f'{_UseAccount}','Password':f'{_UsePassword}'})
            _decodeJsonData = _recv.json()
            _signInACState = _decodeJsonData['AccountState']
            _signInPWState = _decodeJsonData['PasswordState']
            _signInToken = _decodeJsonData['AccountToken']
            
            if _signInACState:
                if _signInPWState:
                    self.ClientPay.AccountState = _signInACState 
                    self.ClientPay.PasswordState  = _signInPWState
                    self.ClientPay.AccountToken = _signInToken
                    _start = False
                    print(f'Account:{_signInACState}')
                    print(f'Password:{_signInPWState}')
                    
                else:
                    _start = False
                    print(f'Password:{_signInPWState}')
            else:
                _start = False
                print(f'Account:{_signInACState}')

    def useSignUpInput(self):
        _start = True
        while _start:
            print(self.ClientObj.signUpTitle)
            _UseAccount = input(self.ClientObj.signInUpAccountTitle)
            _UsePassword = input(self.ClientObj.signInUpPasswordTitle)
            _recv = requests.post('http://127.0.0.1:5000/SignUpAccountProtocol',
                                    json={'Account':f'{_UseAccount}','Password':f'{_UsePassword}'})
            _decodeJsonData = _recv.json()
            _signUpACState = _decodeJsonData['AccountState']
            _signUpPWState = _decodeJsonData['PasswordState']

            if _signUpACState:
                if _signUpPWState:
                    _start = False
                    print(f'Account:{_signUpACState}')
            else:
                _start = False
                print(f'Account:{_signUpACState}')

    def checkUseLoginSelect(self):
        _wrong = False
        while _wrong == False :
            _option = [self.ClientOption.ONE.value, self.ClientOption.TWO.value, self.ClientOption.ZERO.value]
            print(f' ')
            _useInput = input(self.ClientObj.LoginOption)
            _correct = _useInput in _option
            _wrong = _correct == True

            if _correct :
                    return _useInput
            print(self.ClientObj.inputWrong)

    def getMenu(self):
        _recv = requests.get('http://127.0.0.1:5000/GetOnlineGameMenuProtocol')
        _decodeJsonData = _recv.json()
        _TitleTxt = _decodeJsonData['TitleTxt']
        _Games= _decodeJsonData['Games']

        print(_TitleTxt)
        print(' ')
        for _i in range(len(_Games)):
            self.ClientAttest.GameOptions.append(f'0{_i+1}')
            print(f'{self.ClientAttest.GameOptions[_i]}:{_Games[_i]}')
        print(self.ClientObj.GameOptionsEnd)
        print(self.ClientObj.GameOptionsAccount)

    def checkGameOption(self):
        _wrong = False
        while _wrong == False :
            _useInput = input(self.ClientObj.GameOptionTitle)
            _correct = (_useInput in self.ClientAttest.GameOptions) or (_useInput == self.ClientOption.ZERO.value) or (_useInput == self.ClientOption.NINE.value)
            _wrong = _correct == True

            if _correct :
                    return _useInput
            print(self.ClientObj.inputWrong)

    def GameOption(self, useOption):
        if useOption == self.ClientOption.NINE.value :
            self.ClientPay.viewClientPay()
            return True

        if useOption == self.ClientOption.ONE.value:
            self.ClientSlotMachine.setJson(self.ClientPay.getJson())
            self.ClientSlotMachine.GameStart()
            self.ClientPay.setAccountJsonOUT(self.ClientSlotMachine.getJson())
            # self.ClientSlotMachine.__init__()
            self.ClientSlotMachine = None 
            self.ClientSlotMachine = DC.SlotMachine() # C++釋放記憶體的概念。

            return True
        if useOption == self.ClientOption.TWO.value :
            print(self.ClientObj.pending)
            return True
        if useOption == self.ClientOption.THREE.value :
            print(self.ClientObj.pending)
            return True

        if useOption == self.ClientOption.ZERO.value :
            if self.uploadClientPay(): # Todo POST Client Pay for Server
                self.ClientPay.__init__()
                return False
            return True
          
    def onlineLogin(self,useOption):
            if useOption == self.ClientOption.ZERO.value:
                return False

            if useOption == self.ClientOption.ONE.value :
                self.useSignInInput()
                return True

            if useOption == self.ClientOption.TWO.value :
                self.useSignUpInput()
                return True
     
    def uploadClientPay(self):
        _recv = requests.get('http://127.0.0.1:5000/UploadClientDataProtocol',
                                json={'ClientPayAll':self.ClientPay.getJson()})
        _decodeJsonData = _recv.json()
        if _decodeJsonData['UploadState']:
            print(self.ClientObj.UploadStateTrue)
            return True

        print(self.ClientObj.UploadStateFalse)
        return False
        
    def getClientData(self):
        _recv = requests.get('http://127.0.0.1:5000/GetClientDataProtocol',
                                json={'AccountToken': self.ClientPay.AccountToken})
        _decodeJsonData = _recv.json()
        self.ClientPay.setAccountJsonIN(_decodeJsonData['AccountPay'])

    def Execution(self):
        _start = True
        while _start:
            print(' ')
            self.getMenu()
            print(' ')
            if self.GameOption(self.checkGameOption()):
                pass
            else:
                _start = False
                self.OnlineGame()

    def OnlineGame(self):
        _start = True
        while _start:
            if self.onlineLogin( self.checkUseLoginSelect() ) :
                if (self.ClientPay.AccountState == True) and (self.ClientPay.PasswordState == True):
                    self.getClientData()
                    _start = False
                    self.Execution()
            else:
                _start = False

CS = ClientLogin()
CS.OnlineGame()