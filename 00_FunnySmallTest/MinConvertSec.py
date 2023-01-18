import re

class MinConvert:
    """搞笑分鐘轉換"""
    def __init__(self) -> None:
        """初始化"""
        self.min: int = 0
        self.sec: int = 0
        self.convertUnit: int = 60
        self.start: bool = True
        self.check_input: bool = True

    def cleanTime(self) -> None:
        """分秒初始化"""
        self.check_input = True
        self.min = 0
        self.sec = 0
        
    def title(self) -> None:
        """程式標題"""
        title: str = '分轉秒換算'; print(title)

    def userInput(self) -> int:
        """使用者輸入,str 轉換 int"""
        while self.check_input:
            try:
                # 使用者鍵入值
                _userInput: str = input(
                                    '輸入數字分鐘:')
                # 正規表達,取得數字
                _parse_userValue: int = int(
                                    re.sub(r'[\D*?]','', _userInput))
                # 關閉迴圈
                self.check_input = False
            except Exception:
                print(f'請輸入數字 0 ~ 9。')
            else:
                return _parse_userValue

    def parse(self, UseMin:int) -> bool:
        """輸入值解析"""
        _convertNumber: str = str(self.convertUnit * UseMin)
        _convertNumberLen: int = len(_convertNumber)
        _convertDifference: int = _convertNumberLen - 2

        if _convertNumberLen <= 2 :
            self.min = self.min
            self.sec = _convertNumber
        else:
            self.min = _convertNumber[0:_convertDifference]
            self.sec = _convertNumber[_convertDifference:]
        
        _correct = _convertNumberLen > 5
        self.start = _correct == False
        return _correct

    def resolve(self, stuate: bool) -> None:
        """顯示換算成果"""
        _resolve: str = ''
        _resolve += f'{self.min}分'
        _resolve += f'{self.sec}秒'

        print(_resolve)
        if stuate:
            print('好了~ 好了~ 別 Now了!，還有很多有意義的事可以做XDD。')
            
    def execution(self) -> None:
        """執行流程"""
        self.title()
        while self.start:
            self.resolve(self.parse(self.userInput()))
            self.cleanTime()

MCS:object = MinConvert()
MCS.execution()