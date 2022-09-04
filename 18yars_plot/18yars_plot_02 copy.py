import csv
import matplotlib.pyplot as plt

class DataAnalysis():
    def __init__(self,path):
        self.csv= path
        self.data= None

    def csvForPy(self):
        fp = open(self.csv, 'r', encoding='big5')
        csv_reader = csv.DictReader(fp.read().splitlines())
        self.data = list(csv_reader)
        fp.close()

    def unpick(self):
        buyGoodsTime = []
        buyGoodsPrice = []
        for d in self.data:
            purchaseTime = d['購買時間'][5:]
            purchasePrice = d['價錢']
            if purchaseTime == '' and purchasePrice == '':
                continue
            buyGoodsTime.append((purchaseTime))
            buyGoodsPrice.append(int(purchasePrice))

        return buyGoodsTime, buyGoodsPrice

    def clean(self,buyGoodsTime,buyGoodsPrice):
        finalGoodsTime= []
        finalGoodsPrice= []

        # 同日總消費金額。
        for i in range(len(buyGoodsTime)-1):
            reverseIndex= len(buyGoodsTime)-1-i
            if buyGoodsTime[reverseIndex]== buyGoodsTime[reverseIndex-1]:
                buyGoodsPrice[reverseIndex-1]= buyGoodsPrice[reverseIndex]+ buyGoodsPrice[reverseIndex-1]
        # 剔除重複月日。
        for i in range(len(buyGoodsTime)-1):
            if buyGoodsTime[i] not in finalGoodsTime:
                finalGoodsTime.append(buyGoodsTime[i])
                finalGoodsPrice.append(buyGoodsPrice[i])

        return finalGoodsTime, finalGoodsPrice

    def execution(self):
        self.csvForPy()
        _unpick= self.unpick()
        _result= self.clean(_unpick[0], _unpick[1])
        return _result[0], _result[1]
        
class DataTimePrice():
    def __init__(self):
        self.finalGoodsTime= []
        self.finalGoodsPrice= []

class pyPlot():
    def __init__(self):
        self.dateList=[]

    def createData(self):
        self.dateList.append(DataTimePrice())
        
    def addData(self):
        _DAresult= DA.execution()
        reversLen= len(self.dateList)-1
        self.dateList[reversLen].finalGoodsTime= _DAresult[0]
        self.dateList[reversLen].finalGoodsPrice= _DAresult[1]
        
    def pltData(self):
        plt.title("18years")
        reversLen= len(self.dateList)-1
        plt.plot(self.dateList[reversLen].finalGoodsTime, self.dateList[reversLen].finalGoodsPrice)
        
        plt.plot()
        plt.legend(['Money']) 
        plt.grid(True)
        plt.show()

    def execution(self):
        self.createData()
        self.addData()
        self.pltData()

DA= DataAnalysis(r'Pytohn-Small-Test\18yars_plot\18.csv')
# 創建以時間為基底的 條件。
pyPlot().execution()
