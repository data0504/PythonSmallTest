import json
from flask import Flask, request
import time
import random
from enum import Enum
import mysql.connector

class CreateAccountData:
    def __init__(self):
        self.accountNumber = ''
        self.passwordNumber = ''
        self.accountToken = int(0)

        self.SignUpTime = time.time()
        self.SignInTime = float(0)

        self.pay = 0
        self.getCoin = 0
        self.rebate = 0

    def getJson(self):
        return {"pay":self.pay, "getCoin":self.getCoin, "rebate":self.rebate, "accountToken": self.accountToken}

    def getDBJson(self):
        return {"AccountStr":self.accountNumber,
                 "PasswordStr":self.passwordNumber, 
                 "initToken":self.accountToken, 
                 "SignUpTime": self.SignUpTime,
                 "SignInTime": self.SignInTime,
                 "pay": self.pay,
                 "getCoin": self.getCoin,
                 "rebate": self.rebate,
                 }

    def getDBMySQL(self):
        return (self.accountNumber, 
                self.passwordNumber,
                self.accountToken,
                self.SignUpTime,
                self.SignInTime,
                self.pay,
                self.getCoin,
                self.rebate,
                self.accountToken
                )

    def getDBMySQLCreate(self):
        return (self.accountToken,
                self.accountNumber, 
                self.passwordNumber,
                self.accountToken,
                self.SignUpTime,
                self.SignInTime,
                self.pay,
                self.getCoin,
                self.rebate
                )

    def CreateSetJson(self, setValue):
        self.accountNumber = setValue['AccountStr']
        self.passwordNumber = setValue['PasswordStr'] 
        self.accountToken = setValue['initToken']
        self.pay = setValue['initCoin']

    def setDBTxt(self, setValue):
        self.accountNumber = setValue['AccountStr']
        self.passwordNumber = setValue['PasswordStr'] 
        self.accountToken = setValue['initToken']
        self.SignUpTime = setValue['SignUpTime']
        self.SignInTime = setValue['SignInTime']
        self.pay = setValue['pay']
        self.getCoin = setValue['getCoin']
        self.rebate = setValue['rebate']

    def setMySqlDB(self, setValue):
        self.accountNumber = setValue[1]
        self.passwordNumber = setValue[2] 
        self.accountToken = int(setValue[3])
        self.SignUpTime = float(setValue[4])
        self.SignInTime = float(setValue[5])
        self.pay = float(setValue[6])
        self.getCoin = float(setValue[7])
        self.rebate = float(setValue[8])

    def UpDataSetJson(self, UpSetValue): 
        self.pay = UpSetValue['pay'] 
        self.getCoin =  UpSetValue['getCoin']
        self.rebate =  UpSetValue['rebate']
    
class MySQLsyntax:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = '127.0.0.1',port = '3306',
            user = 'root',password = '0000',
            database = 'online_game',charset = 'utf8')

        self.cursor = self.con.cursor()

    def closeMySQL(self):
        self.con.close()
        self.cursor.close()

    def SelectTable(self):
        return "SELECT * FROM accounts;"

    def UpDate(self):
        return "UPDATE accounts SET\
            account = %s, password = %s,initToken = %s,\
            signUpTime = %s, signInTime = %s,\
            pay = %s, getCoin = %s, rebate = %s \
            WHERE accounts_id = %s;"

    def InsetData(self):
        return "INSERT INTO accounts\
            (accounts_id, account, password, initToken, signUpTime, signInTime, pay, getCoin, rebate) VALUES \
            (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

class AccountVerify:
    def __init__(self):
        self.AccountSave = [] 
        
        self.createCoin = 500
        self.AccountToken = None
        self.AccountState = False
        self.passwordState = False

        self.MySQLsyntax = MySQLsyntax()

    def clearState(self):
        self.AccountState = False
        self.passwordState = False
        self.AccountToken = None

    def closeMySQL(self):
        self.con.close()
        self.cursor.close()

    def SignUpParseAccount(self, accountNumber):
        for _i in range(len(self.AccountSave)):
            if accountNumber == self.AccountSave[_i].accountNumber:
                self.AccountToken = _i
                self.AccountState = False
                return False
            else:
                self.AccountState = True
        else:
            if len(self.AccountSave) != 0:
                self.AccountToken = (_i + 1)
            else:
                self.AccountToken = 0
            self.AccountState = True
            return True
        
    def SignUpAccount(self, accountNumber, passwordNumber):
        if passwordNumber != '' :
            _createSetValue = {"AccountStr":accountNumber, "PasswordStr":passwordNumber, "initCoin":self.createCoin, "initToken":self.AccountToken}
            self.createPay = CreateAccountData()
            self.createPay.CreateSetJson(_createSetValue)
            self.AccountSave.append(self.createPay)

            self.insetForMySQL(self.AccountSave[self.AccountToken]) # Server Inset MySQL
            self.setTomDBTxt(self.AccountSave[self.AccountToken], self.AccountToken) # Server Inset Txt

            self.passwordState = True

    def SignInParseAccount(self,accountNumber):
        for _i in range(len(self.AccountSave)):
            if accountNumber == self.AccountSave[_i].accountNumber:
                self.AccountToken = _i
                self.AccountState = True
                return True
            else:
                self.AccountState = False
        else:
            self.AccountState = False
            return False
        
    def SignInParsePassword(self,passwordNumber):
        if passwordNumber == self.AccountSave[self.AccountToken].passwordNumber:
                self.AccountSave[self.AccountToken].SignInTime = time.time()
                self.passwordState = True
                return True
        else:
            self.passwordState = False
            return False

    def GiveSingleAccountData(self, AccountVerify):
        if AccountVerify :
            return{
            "AccountState":self.AccountState,
            "PasswordState":self.passwordState,
            "AccountToken":AV.AccountToken
            }

        else:
            return{
            "AccountState":self.AccountState,
            "PasswordState":self.passwordState,
            "AccountToken":AV.AccountToken
            }

    def GetAccountData(self, ClientToken):
        return  {"AccountPay":AV.AccountSave[ClientToken].getJson() } # json 放 json

    def UploadAccount(self, ClientPayAll):
        _pass = True
        try:
            _index = ClientPayAll['AccountToken']
            self.AccountSave[_index].UpDataSetJson(ClientPayAll)
            self.setToDBMySQL(self.AccountSave[_index]) # Server Update MySQL
            self.setTomDBTxt(self.AccountSave[_index], _index) # Server Update Account.txt
            return {"UploadState":_pass}
        except:
            _pass = False
            return {"UploadState":_pass}

    def loadFromDBMySQL(self): # Todo : FetchallMySQLTableAccount append self.AccountSave.
        self.MySQLsyntax.cursor.execute(self.MySQLsyntax.SelectTable())
        records = self.MySQLsyntax.cursor.fetchall()
        print(f"TableAccountsAll : {self.MySQLsyntax.cursor.rowcount} 筆資料")
        for i in range(len(records)):
            _pendingList = []
            _pendingList += records[i]
            CAD = CreateAccountData()
            CAD.setMySqlDB(_pendingList)
            self.AccountSave.append(CAD)
            
        self.MySQLsyntax.closeMySQL()

    def setToDBMySQL(self, setValue): # Todo : self.AccountSet Update to MySQLTableAccount.
        self.MySQLsyntax.__init__()
        self.MySQLsyntax.cursor.execute(self.MySQLsyntax.UpDate(), setValue.getDBMySQL())
        self.MySQLsyntax.con.commit() # 確認資料有存入資料庫
        self.MySQLsyntax.closeMySQL()

    def insetForMySQL(self, setValue): # Todo : self.AccountInset signUp save MySQLTableAccount.
        self.MySQLsyntax.__init__()
        self.MySQLsyntax.cursor.execute(self.MySQLsyntax.InsetData(), setValue.getDBMySQLCreate())
        self.MySQLsyntax.con.commit() # 確認資料有存入資料庫
        self.MySQLsyntax.closeMySQL()

    def loadFromDBTxt(self): # Todo : FetchallAccount.txt append self.AccountSave.
        _txt = r'PythonSmallTest\DataOnlineGame\Account.txt'
        _filePaper = open(_txt,'r',encoding = 'big5')
        _DBreader = _filePaper.readlines()
        _filePaper.close()

        for i in range(len(_DBreader)):
            _jsonObj = json.loads(_DBreader[i])
            self.createPay = CreateAccountData()
            self.createPay.setDB(_jsonObj)
            self.AccountSave.append(self.createPay)

    def setTomDBTxt(self, setValue, index): # Todo : self.AccountSave Update DB 。
        _filePaper = open(r"PythonSmallTest\DataOnlineGame\Account.txt") # 導入舊DB 刷新 或 新增。
        
        _oldDB = []
        for i in _filePaper:
            _oldDB.append(i)
        _filePaper.close()

        _oldDBIndex = []
        for k in range(len(_oldDB)):
            _oldDBIndex.append(k)
        if index in _oldDBIndex: 
            _oldDB.pop(index)

        _json = setValue.getDBJson()
        j = json.dumps(_json) # 資料 Json 格式。
        _oldDB.insert(index, f'{j}\n')

        _filePaper = open(r"PythonSmallTest\DataOnlineGame\Account.txt",'w+') # 重新寫入檔案
        
        for j in range(len(_oldDB)):
            _filePaper.write(_oldDB[j])
            
        _filePaper.close()
        _oldDB = []

class OnlineGame:
    def __init__(self):
        self.Title = '澳門賭場上線瞜!'
        self.Games = ['SlotMachine', 'Baccarat', 'Big Two Deuces']

    def MainMenu(self):
        return {"TitleTxt":self.Title,
                "Games":self.Games}

    def GameFrequency(self, ClientPlayCoin, gameCoinCondition , gameCoinCurrencyCondition):
        _gameFrequency = ClientPlayCoin / gameCoinCondition
        _gameCurrency = False
        if _gameFrequency >= gameCoinCurrencyCondition:
            _gameCurrency = True

        return {"GameFrequency":_gameFrequency, "GameCurrency":_gameCurrency}

    def slotMachineRandomList(self, size, index):
        _rowRandomResult = []
        for _i in range(size):
            for _j in range(size):
                _single = random.randint( (size - size) , (index-1))
                _rowRandomResult.append(_single)
        return _rowRandomResult

    def slotMachineParseRandomList(self, size ,rowRandomList):
        _comboGrand = []
        for m in range(size):
            _grandtotal = 1
            _comboStart = True
            for n in range(size-1):
                _singleRemainList = rowRandomList [size + (size * n) : size + size + (size * n)]
                if _comboStart:
                    if rowRandomList[m] in _singleRemainList :
                        _comboStart = True
                        _grandtotal += 1
                    else:
                        _comboStart = False
                        break
            _comboGrand.append(_grandtotal)
        return _comboGrand

    def slotMachineParseBigCombo(self, comboGrand):
        _bigCombo = 0
        # 解析 單次拉霸，最大Combo。
        for _i in range(len(comboGrand)):
            _bigCombo = comboGrand[0]
            if comboGrand[_i] > _bigCombo :
                _bigCombo = comboGrand[_i]

        return _bigCombo

    def slotMachineParseAwardState(self, awardCondition, bigCombo):
        _awardState= False 
        # 解析 單次拉霸 是否中大獎。
        if bigCombo == awardCondition:
            _awardState = True

        return _awardState

server = Flask(__name__)
AV = AccountVerify()
OG = OnlineGame()

AV.loadFromDBTxt() # 開啟之後 先抓取 txt檔 帳號資料。
AV.loadFromDBMySQL() # 開啟之後 先抓取 MySQL 帳號資料。

@server.route('/SignUpAccountProtocol',methods=['POST'])
def SignUpAccount():
    clientSignUpAccount = request.json
    AV.clearState()
    if AV.SignUpParseAccount(clientSignUpAccount['Account']):
        AV.SignUpAccount(clientSignUpAccount['Account'], clientSignUpAccount['Password'])

    return {"AccountState": AV.AccountState, "PasswordState": AV.passwordState}
            
@server.route('/SignInAccountProtocol',methods=['POST']) # 登入就拿錢給Client
def SignInAccount():
    clientSignInAccount = request.json
    AV.clearState()
    if AV.SignInParseAccount(clientSignInAccount['Account']):
        return AV.GiveSingleAccountData((AV.SignInParsePassword(clientSignInAccount['Password'])))

    return {"AccountState": AV.AccountState, 
            "PasswordState": AV.passwordState, 
            "AccountToken":AV.AccountToken 
            }

@server.route('/GetOnlineGameMenuProtocol',methods=['GET'])
def GetOnlineGameMenu():
    return OG.MainMenu()

@server.route('/StartGameFrequencyProtocol',methods=['POST'])
def StartGameFrequency(): 
    _clientQuestion = request.json
    return OG.GameFrequency(_clientQuestion['ClientPlayCoin'], 
                        _clientQuestion['CoinCondition'], 
                        _clientQuestion['CoinCurrencyCondition'],)

@server.route('/slotMachineRandomResultProtocol',methods=['GET'])
def StartGameRandomResult():
    _clientQuestion = request.json

    _rowRandomResult = OG.slotMachineRandomList(_clientQuestion['SizeCondition'], _clientQuestion['IndexCondition'])

    _comGrand = OG.slotMachineParseRandomList(_clientQuestion['SizeCondition'], _rowRandomResult) 

    _bigCombo = OG.slotMachineParseBigCombo(_comGrand)
    _awardState = OG.slotMachineParseAwardState(_clientQuestion['SizeCondition'], _bigCombo)

    return {"RandomResult":_rowRandomResult, "BigCombo":_bigCombo, "AwardState":_awardState}

@server.route('/GetClientDataProtocol',methods=['GET'])
def GetClientData():
    _clientQuestion = request.json
    return AV.GetAccountData(_clientQuestion['AccountToken'])

@server.route('/UploadClientDataProtocol',methods=['GET'])
def UpDataClientData(): 
    _clientQuestion = request.json
    return AV.UploadAccount(_clientQuestion['ClientPayAll'])  # None 會出錯
    
server.run(host='127.0.0.1')