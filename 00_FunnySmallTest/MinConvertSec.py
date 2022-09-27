# 字串解法。
class MinConvert:
    def __init__(self):
        self.min = 0
        self.sec = 0
        self.convertUnit = 60
        self.start = True

    def clear(self):
        self.min = 0
        self.sec = 0
        
    def title(self):
        title : str
        title = "分轉秒換算"
        print(title)

    def UseInput(self):
        _UseMin : str
        _UseMin = input('輸入數字分鐘:')

        _intUseMin : int = int(_UseMin)
        return _intUseMin

    def parse(self, UseMin:int):
        _convertNumber : str
        _convertNumber = str(self.convertUnit * UseMin)

        _convertNumberLen : int 
        _convertNumberLen = len(_convertNumber)

        _convertDifference : int
        _convertDifference = _convertNumberLen - 2

        if _convertNumberLen <= 2 :
            self.sec = _convertNumber
        else:
            self.min = _convertNumber[0 : _convertDifference]
            self.sec = _convertNumber[_convertDifference: ]
        
        _correct = _convertNumberLen < 5
        self.start = _correct == True
        return _correct

    def resolve(self, state : bool):
        _resolve : str
        _resolve = ''
        _resolve += f'{self.min}分'
        _resolve += f'{self.sec}秒'

        print(_resolve)
        if state == False:
            print('好了~ 好了~ 別 Now了!，還有很多有意義的事可以做XDD。')   
        
    def execution(self):
        self.title()
        while self.start:
            self.resolve( self.parse( self.UseInput() ) )
            self.clear()

MCS = MinConvert()
MCS.execution()