import unittest
# class frame:、class Score: ，為理想型。
class ThrowBallFrame:
    def __init__(self):
        self.score : int = 0
        self.currentFrame : int = 1
        self.isFirstThrow : bool = True
        self.Scorer = ThrowBallScorer()

    def GetScore(self): # 提取總得分
        return self.Scorer.ScoreForFrame(self.currentFrame)

    def GetCurrentFrame(self): # 提取當前局數
        return self.currentFrame

    def AddBallScore(self, pins : int): # 增加獲得分數
        self.Scorer.AddBallScore(pins)
        self.AdjustCurrentFrame(pins)
        self.score += pins

    def AdjustCurrentFrame(self, pins : int): # 計算當前局數
        if self.LastBallInFrame(pins):  # 判斷拋球 7種 方式。 
            self.AdvanceFrame()  # 下一局 + 重製
        else:
            self.isFirstThrow = False

    def AdvanceFrame(self):
        self.isFirstThrow = True 
        self.currentFrame += 1
        if self.currentFrame > 10:
            self.currentFrame = 10

    def AdjustFrameForStrike(self, pins : int):
        if (pins == 10):
            self.AdvanceFrame()
            return True

    def Strike(self, pins : int):  
        return self.isFirstThrow and (pins == 10 )

    def LastBallInFrame(self, pins : int):
        return (self.Strike(pins)) or ( False == self.isFirstThrow)

    def ScoreForFrame(self, theFrame : int):
        return self.Scorer.ScoreForFrame(theFrame)

class ThrowBallScorer:
    def __init__(self):
        self.ball : int
        self.ThrowsLattice : int = self.CreateThrowsLattice()
        self.currentThrow : int = 0

    def CreateThrowsLattice(self): #創建21個未計分格子。
        __nullThrows = []
        for _i in range(21):
            __nullThrows.append(0)
        throwList : int = __nullThrows
        return throwList

    def AddBallScore(self, pins : int): # 增加獲得分數
        self.ThrowsLattice[self.currentThrow] = pins
        self.currentThrow +=1
        
    def ScoreForFrame(self, theFrame : int): # 計算每局分數
        self.ball = 0
        _score : int = 0
        _currentFrame : int = 0

        for index in range(len(self.ThrowsLattice)) :
            if _currentFrame < theFrame : 
                _currentFrame += 1
                _theBallScore : int = self.theBallScore()
                firstThrow : int = _theBallScore['firstThrow']
                secondThrow : int = _theBallScore['secondThrow']
                _theFrameAllScore : int = firstThrow + secondThrow
                _nextFrameBall_1index : int = (_currentFrame * 2)

                if self.Strike(firstThrow, _currentFrame) :
                    _score += _theFrameAllScore + self.ThrowsLattice[_nextFrameBall_1index] + self.strikeTwoBallState(_nextFrameBall_1index, _currentFrame)
                    continue
                
                if self.Spare(_theFrameAllScore):
                    _score +=  self.ThrowsLattice[_nextFrameBall_1index]

                _score += _theFrameAllScore
        return _score

    def theBallScore(self):
        firstThrow : int = self.ThrowsLattice[self.ball]
        self.ball += 1
        secondThrow : int = self.ThrowsLattice[self.ball]
        self.ball += 1
        return{"firstThrow":firstThrow, "secondThrow":secondThrow}

    def strikeTwoBallState(self, nextFrameBall_1index : int, currentThrow : int):
        if currentThrow != 9:
            if self.ThrowsLattice[nextFrameBall_1index] == 10: # if next first ball == 10 score
                nextFrameBall_2index = nextFrameBall_1index +2
        else:
            nextFrameBall_2index = nextFrameBall_1index +1
        return  self.ThrowsLattice[nextFrameBall_2index]

    def Strike(self, firstThrow : int, currentThrow : int):
        return (self.ThrowsLattice[firstThrow] == 10) and (currentThrow != 10)

    def Spare(self, theFrameAllScore : int): 
        return theFrameAllScore == 10 or theFrameAllScore == 20

class TestClass(unittest.TestCase):
    def setUp(self):
        self.TB = ThrowBallFrame() 

    def testThrowBallAdd_0Function(self): #Spare補全倒 / 取得緊接執行局數
        self.TB.AddBallScore(5)  
        self.TB.AddBallScore(5)

        self.TB.AddBallScore(8)
        self.TB.AddBallScore(2)

        self.assertEqual(18, self.TB.ScoreForFrame(1) )
        self.assertEqual(28, self.TB.ScoreForFrame(2) )
        self.assertEqual(28, self.TB.ScoreForFrame(3) )
        self.assertEqual(3, self.TB.GetCurrentFrame() )

    def testThrowBallAdd_1Function(self): #Spare補全倒 / 取得執行局數
        self.TB.AddBallScore(5)  
        self.TB.AddBallScore(5)

        self.TB.AddBallScore(8)
        self.TB.AddBallScore(2) # 未清除 bool

        self.TB.AddBallScore(1)
        
        
        self.assertEqual(18, self.TB.ScoreForFrame(1) )
        self.assertEqual(29, self.TB.ScoreForFrame(2) )
        self.assertEqual(30, self.TB.GetScore())
        self.assertEqual(3, self.TB.GetCurrentFrame() )

    def testThrowBallAdd_2Function(self): # Perfect Game 完全比賽 300分

        for index in range(10):
            if index == 9:
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(10)
            else:
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(0)
    
        self.assertEqual(30, self.TB.ScoreForFrame(1) )
        self.assertEqual(60, self.TB.ScoreForFrame(2) )
        self.assertEqual(90, self.TB.ScoreForFrame(3) )
        self.assertEqual(120, self.TB.ScoreForFrame(4) )
        self.assertEqual(150, self.TB.ScoreForFrame(5) )
        self.assertEqual(180, self.TB.ScoreForFrame(6) )
        self.assertEqual(210, self.TB.ScoreForFrame(7) )
        self.assertEqual(240, self.TB.ScoreForFrame(8) )
        self.assertEqual(270, self.TB.ScoreForFrame(9) )
        self.assertEqual(300, self.TB.ScoreForFrame(10) )
        self.assertEqual(10, self.TB.GetCurrentFrame() )
        self.assertEqual(300, self.TB.GetScore() )

    def testThrowBallAdd_3Function(self): # 10 Frame not strike(全倒) and spare(補全倒)

        for index in range(10):
            if index == 9:
                self.TB.AddBallScore(5)
                self.TB.AddBallScore(1)
                # self.TB.AddBallScore(10) # 不會被記錄
            else:
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(0)
        self.assertEqual(235, self.TB.ScoreForFrame(8) )
        self.assertEqual(251, self.TB.ScoreForFrame(9) )
        self.assertEqual(257, self.TB.ScoreForFrame(10) )
        self.assertEqual(10, self.TB.GetCurrentFrame() )
        self.assertEqual(257, self.TB.GetScore() )

    def testThrowBallAdd_4Function(self): # 10 Frame spare(補全倒)

            for index in range(10):
                if index == 9:
                    self.TB.AddBallScore(9)
                    self.TB.AddBallScore(1)
                    self.TB.AddBallScore(1) # 補中
                else:
                    self.TB.AddBallScore(10)
                    self.TB.AddBallScore(0)
            self.assertEqual(239, self.TB.ScoreForFrame(8) )
            self.assertEqual(259, self.TB.ScoreForFrame(9) )
            self.assertEqual(270, self.TB.ScoreForFrame(10) )
            self.assertEqual(10, self.TB.GetCurrentFrame() )
            self.assertEqual(270, self.TB.GetScore() )

    def testThrowBallAdd_5Function(self): # 10 Frame strike、strike、9
        for index in range(10):
            if index == 9:
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(9) # 補中
            else:
                self.TB.AddBallScore(10)
                self.TB.AddBallScore(0)
        self.assertEqual(240, self.TB.ScoreForFrame(8) )
        self.assertEqual(270, self.TB.ScoreForFrame(9) )
        self.assertEqual(299, self.TB.ScoreForFrame(10) )
        self.assertEqual(10, self.TB.GetCurrentFrame() )
        self.assertEqual(299, self.TB.GetScore() )

    def testThrowBallAdd_6Function(self): # 10 Frame strike、strike、9
            for index in range(10):
                if index == 9:
                    self.TB.AddBallScore(10)
                    self.TB.AddBallScore(0)
                    self.TB.AddBallScore(9) # 補中
                else:
                    self.TB.AddBallScore(10)
                    self.TB.AddBallScore(0)
            self.assertEqual(240, self.TB.ScoreForFrame(8) )
            self.assertEqual(260, self.TB.ScoreForFrame(9) )
            self.assertEqual(279, self.TB.ScoreForFrame(10))
            self.assertEqual(10, self.TB.GetCurrentFrame() )
            self.assertEqual(279, self.TB.GetScore() )

suite = unittest.TestSuite()
suite.addTest(TestClass('testThrowBallAdd_0Function'))
suite.addTest(TestClass('testThrowBallAdd_1Function'))
suite.addTest(TestClass('testThrowBallAdd_2Function'))
suite.addTest(TestClass('testThrowBallAdd_3Function'))
suite.addTest(TestClass('testThrowBallAdd_4Function'))
suite.addTest(TestClass('testThrowBallAdd_5Function'))
suite.addTest(TestClass('testThrowBallAdd_6Function'))
unittest.TextTestRunner(verbosity=2).run(suite)