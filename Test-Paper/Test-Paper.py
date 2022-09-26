class testPaper():
    def __init__(self,path):
        self.path= path
        self.csvReader= None
        self.start= True
        self.useAnswer= None
        self.paperAnswer= None
        self.correct= 0
        self.wrong= 0
        self.nullAnswer= 0

    def Title(self):
        print('---簡易試卷---')

    def readCsv(self):
        _filePaper= open(self.path,'r',encoding='big5')
        self.csvReader= _filePaper.readlines()
        _filePaper.close()

    def topic(self,single,i):
        print(f'Q{i+1}.'+ single[0])
        print('(01).'+' '+ single[1], '(02).'+ ' '+ single[2])
        print('(03).'+' '+ single[3], '(04).'+ ' '+ single[4])
        self.paperAnswer= single[5]

    def unpick(self,i):
        self.start= True
        allTopic= self.csvReader[i]. replace('\n',''). split(',')
        self.topic(allTopic,i)

    def useInput(self):
        self.useAnswer= input('答:')

    def checkAnswer(self):
        _correct= self.useAnswer== '1' or self.useAnswer== '2' or \
                     self.useAnswer== '3' or self.useAnswer== '4'
        _wrong= _correct== False

        if _correct:
            if self.useAnswer == self.paperAnswer:
                print('正確答對。')
                self.correct+= 1
                self.start= False
            else:
                print('錯誤答案。')
                self.wrong+= 1
                self.start= False
        else:
            self.nullAnswer+= 1
            print('輸入錯誤。')

    def result(self):
        print(f'總{len(self.csvReader)}題; 對{self.correct}題; 錯{self.wrong}題; 無效{self.nullAnswer}次。')
        print('試卷結束。')
    
    def execution(self):
        self.Title()
        self.readCsv()
        
        for i in range(len(self.csvReader)):
            self.unpick(i)
            while self.start:
                self.useInput()
                self.checkAnswer()
        self.result()

testPaperPath= r'homeworks\6.TestPaper_SmallTest\testPaper.csv'
TP= testPaper(testPaperPath)
TP.execution()