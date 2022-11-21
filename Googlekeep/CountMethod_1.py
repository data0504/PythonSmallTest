import json
import gkeepapi

TestAccount = r'D:\Todo\GoogleKeep\Account.txt' 
with open(TestAccount, 'r', encoding='utf-8') as f:
    account = json.load(f)

googleKeep = gkeepapi.Keep()

try:
    success = googleKeep.login(account['Account'], account['Password'])
except:
    print('Maybe you need to go to this website to enable permissions: https://accounts.google.com/b/0/DisplayUnlockCaptcha')
    raise


notes = googleKeep.all()  

for theNote in notes:
    calculate = False
    theNoteText : str = theNote.text

    start : int = 0
    stop : int = 0
    for i in range(len(theNoteText)-1):
        if theNoteText[i] =='$' and theNoteText[i+1] == '%' and (start == 0):
            start = i+2
            continue

        if theNoteText[i] =='$' and theNoteText[i+1] == '%' and (stop == 0):
            stop = i
            calculate = True
            break


    if calculate:
        formulaScope : str = theNoteText[start:stop]
        answer = eval(formulaScope)

        formulaSun : str = ''
        formulaSun += formulaScope
        formulaSun += '='
        formulaSun += str(answer)


        clearTheNoteText = theNoteText.replace('$%','').replace(formulaScope,formulaSun)
        theNote.text = clearTheNoteText
        googleKeep.sync()

        calculate = False