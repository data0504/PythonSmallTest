import random

class GuessTheNumber():
    def __init__(self):
        self.start= True
        self.answer= random.randint(1000,9999)
        self.useAnswer= None
        self.answerList= []
        self.uesAnswerList= []
        self.a= 0
        self.b= 0
        self.winOrLoseAns = None

    def winOrLose(self):
        for i in range(len(self.answerList)):
            for j in range(len( self.uesAnswerList)):
                if (i == self.a and j == self.b) or self.b==len(self.answerList) :
                    self.winOrLoseAns= 0
                    break

            if len(self.answerList) == self.a:
                self.winOrLoseAns= 1
                break

    def gameTitle(self):
        print('快來玩玩0A0B猜數字遊戲~')

    def useInput(self):
        self.useAnswer= input(f'請輸入{len(str(self.answer))}位數:')
        return self.checkInput()

    def checkInput(self):
        if len(str(self.answer)) != len(self.useAnswer):
            print('輸入長度不符唷。')
            return False

        for i in self.useAnswer:
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] :
                print('輸入不符規定唷。')
                return False

    def unpick(self):
        self.answerList= []
        for i in str(self.answer):
            self.answerList.append(i)

        self.uesAnswerList= []
        for j in self.useAnswer:
            self.uesAnswerList.append(j)

    def parse(self):
        self.a=0
        for i in range(len(self.answerList)):
            reveres= len(self.answerList)-i-1
            if (self.answerList[reveres] == self.uesAnswerList[reveres]):
                self.a+= 1
                self.answerList[reveres]='-'
                self.uesAnswerList.pop(reveres)
                
        self.b=0
        for i in range(len(self.uesAnswerList)):
            for j in range(len(self.answerList)):
                if  (self.uesAnswerList[i] in self.answerList) and (self.uesAnswerList[i] == self.answerList[j]):
                    self.b+= 1
                    self.answerList[j]= '-'

    def result(self,):
        if self.winOrLoseAns == 0:
            print(f'{self.a}A{self.b}B')
            print('不行要說欸，知道嗎?')

        if self.winOrLoseAns == 1:
            print(f'{self.a}A{self.b}B')
            print('還真有你的讚唷!')
            self.start= False

    def execution(self):
        self.gameTitle()
        while  self.start :
            if self.useInput() == False:
                continue
            self.unpick()
            self.parse()
            self.winOrLose()
            self.result()
            
GTN= GuessTheNumber()
GTN.execution()          