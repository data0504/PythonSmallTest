import json
import gkeepapi
import time

class googleKeepTool:
    def __init__(self):
        self.googleKeep = gkeepapi.Keep()

    def login(self):
        TestAccount = r'D:\Todo\GoogleKeep\Account.txt' 
        with open(TestAccount, 'r', encoding='utf-8') as f:
            account = json.load(f)


        try:
            self.googleKeep.login(account['Account'], account['Password'])
        except:
            print('Maybe you need to go to this website to enable permissions: https://accounts.google.com/b/0/DisplayUnlockCaptcha')
            raise

    def FormulaCalculation(self):

        notes = self.googleKeep.all()  
        for theNote in notes:
            calculate = False
            checkCalculate = False
            theNoteText : str = theNote.text

            theText = []
            start : int= 0
            stop : int= 0
            for i in range(len(theNoteText)):
                if theNoteText[i] == '\n':
                    stop = i
                    onePart = theNoteText[start : stop]

                    start = i + 1
                    theText.append(onePart)

                if i == (len(theNoteText)-1):
                    stop = i + 1
                    lostPart = theNoteText[start : stop]
                    theText.append(lostPart)

            for j in range(len(theText)):
                start : int = 0
                stop : int = 0
                calculate = False
                theNoteText = theText[j]
                for k in range(len(theNoteText)-1):
                    if theNoteText[k] =='$' and theNoteText[k+1] == '%' and (start == 0):
                        start = k+2
                        continue

                    if theNoteText[k] =='$' and theNoteText[k+1] == '%' and (stop == 0):
                        stop = k

                    if start!=0 and stop!=0:
                        calculate = True
                        break


                if calculate:
                        calculate = False
                        checkCalculate = True

                        formulaScope : str = theNoteText[ start : stop ]
                        answer = eval(formulaScope)

                        formulaSun : str = ''
                        formulaSun += formulaScope
                        formulaSun += ' = '
                        formulaSun += str(answer)

                        theText[j] = theText[j].replace('$%','').replace(formulaScope,formulaSun)


                if (j == (len(theText)-1)) and (checkCalculate == True):
                    nextRow = '\n'
                    theNote.text = nextRow.join(theText)
                    self.googleKeep.sync()



GKT = googleKeepTool()
GKT.login()
GKT.FormulaCalculation()