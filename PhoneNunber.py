from random import sample

class randomPhoneNumber():
    def __init__(self,rows, limit, country):
        self.rows= rows
        self.Limit= limit
        self.country= country
        self.destFile= rf'work\1.PhoneNumber_SmallTest\RandomPhoneNumber_{country}_{rows}rows.txt'

    def number(self):
        _list= [0,1,2,3,4,5,6,7,8,9]
        listRandom= sample(_list,self.Limit)
        return listRandom
    
    def write(self):
        with open(self.destFile, 'w') as f:
            for j in range(self.rows):
                resolve= ''
                resolve+= str(self.country)+ ' '+f'9'

                for i in self.number():
                    resolve+= f'{i}'
                print(resolve)
                f.write(''.join(resolve+ "\n"))
            f.close()

rows= 10
numberLimit= 8
countryCode= '+886'
randomN= randomPhoneNumber(rows, numberLimit, countryCode)
randomN.write()
