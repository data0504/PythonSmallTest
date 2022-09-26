list = [-5, 5, 5, 700, 2200, 6, 28, 28, 280, 6, 3, 4, 10000, 20, 10000, 10000, 10000, 5, 5, 5, 5]

class smallSort():
    def __init__(self, list):
        self.list = list
        self.resolve = []
        self.mini = self.list[0]
        self.start = True
        self.repeat = 0

    def findMiniNumber(self):
        for i in range(len(self.list)):
            compare= self.list[i]
            if (compare not in self.resolve) and (compare < self.mini):
                self.mini= list[i]
        self.resolve.append(self.mini)

    def parseRepeatNumber(self):
        self.repeat = 0
        for i in range(len(self.list)):
            compare= self.list[i]
            if self.mini == compare:
                self.repeat+= 1
                if self.repeat > 1:
                    self.resolve.append(self.mini)
                    
    def nexToMini(self):
        for i in range(len(self.list)):
            compare= self.list[i]
            if self.mini < compare:
                self.mini = compare
                break

    def parseEnd(self):
        while self.start:
            if len(self.resolve) != len(self.list):
                self.findMiniNumber()
                self.parseRepeatNumber()
                self.nexToMini()
            else:
                self.start = False

        return self.resolve
        
sort= smallSort(list)
print(sort.parseEnd())