import unittest

# server 主導一切，的寫。

class Class1:
    def __init__(self, serverLenLimit, clientConnectLimit, clientContentLimit):
        self.content = []
        self.serverLenLimit = serverLenLimit
        
        self.clientPeople = []
        self.clientConnectLimit = clientConnectLimit
        self.clientContentLimit = clientContentLimit

    def AddCommunication(self, addContent:str):
        _content = self.contentBreakDown(addContent)
        _correct = self.idBreakDown(_content[0]) == True
        if _correct:
            self.content.append(_content[1])

    def contentBreakDown(self, addContent:str):
        _resolve = []
        for i in addContent:
            _resolve.append(i)
        _Content = _resolve[None:None]
        _UseId = _resolve[None:1]

        _SContent=''.join(_Content)
        _SUseId=''.join(_UseId)

        return _SUseId, _SContent
    
    def idBreakDown(self, ID:str):
        _ClientIndex = len(self.clientPeople)
        if (ID not in self.clientPeople) and (_ClientIndex < self.clientConnectLimit) :
            self.clientPeople.append(ID)
            return True

        if ID in self.clientPeople :
            return True
        else:
            return False
       
    def ParseServerCommunication(self): # 限制 server 儲存數量的方法。
        _len = len(self.content) - self.serverLenLimit
        if len(self.content) > self.serverLenLimit:
            for i in range(_len):
                self.content.pop(0) 

    def ParseClientCommunication(self): # 限制 clientGET 數量的方法。
        if len(self.clientPeople) < self.clientContentLimit:
            _start = len(self.content)-len(self.content)
            _stop = len(self.content)
            return _start,_stop

        if len(self.clientPeople) > self.clientContentLimit:
            _start = len(self.content)-self.clientContentLimit
            _stop = len(self.content)
            return _start,_stop

        if len(self.clientPeople) == self.clientContentLimit:
            _start = None
            _stop = len(self.content)
            return _start,_stop
        
    def GetCommunication(self):
        _Ss = self.ParseClientCommunication()
        return self.content[_Ss[0] : _Ss[1]]
        
class TestClass(unittest.TestCase):
    def setUp(self):
        self.manager = Class1(5,3,3) #參數左至右為 : server限制、client連線限制、client對話限制。

    def testWithoutAddFunction(self):
        self.manager.AddCommunication('A:1test')
        self.manager.ParseServerCommunication()
        self.assertEqual(['A:1test'], self.manager.GetCommunication() )

    def testAddOnce2Function(self):
        self.manager.AddCommunication('A:1test')
        self.manager.AddCommunication('B:2test')
        self.manager.ParseServerCommunication()
        self.assertEqual(['A:1test','B:2test'],self.manager.GetCommunication())

    def testAddOnce3Function(self):
        self.manager.AddCommunication('A:1test')
        self.manager.AddCommunication('A:2test')
        self.manager.AddCommunication('A:3test')
        self.manager.AddCommunication('A:4test')
        self.manager.AddCommunication('A:5test')
        self.manager.AddCommunication('A:6test')
        self.manager.ParseServerCommunication()
        self.assertEqual(['A:2test','A:3test','A:4test','A:5test','A:6test'],self.manager.GetCommunication())

    def testAddOnce4Function(self):
        self.manager.AddCommunication('A:1test')
        self.manager.AddCommunication('B:2test')
        self.manager.AddCommunication('A:3test')
        self.manager.AddCommunication('B:4test')
        self.manager.AddCommunication('A:5test')
        self.manager.AddCommunication('C:6test')
        self.manager.ParseServerCommunication()
        self.assertEqual(['B:2test','A:3test','B:4test','A:5test','C:6test'],self.manager.GetCommunication())

    def testAddOnce5Function(self):
        self.manager.AddCommunication('A:1test')
        self.manager.AddCommunication('B:2test')
        self.manager.AddCommunication('A:3test')
        self.manager.AddCommunication('B:4test')
        self.manager.AddCommunication('A:5test')
        self.manager.AddCommunication('C:6test')

        self.manager.AddCommunication('D:6test')
        self.manager.AddCommunication('E:6test')

        self.manager.ParseServerCommunication()
        self.assertEqual(['B:2test','A:3test','B:4test','A:5test','C:6test'],self.manager.GetCommunication())
    
    def testAddOnce6Function(self):
        self.manager.AddCommunication('A:1test')
        self.manager.AddCommunication('B:2test')
        self.manager.AddCommunication('A:3test')
        self.manager.AddCommunication('B:4test')
        self.manager.AddCommunication('A:5test')
        self.manager.AddCommunication('C:6test')

        self.manager.AddCommunication('D:6test')
        self.manager.AddCommunication('E:6test')

        self.manager.AddCommunication('B:4test')
        self.manager.AddCommunication('A:5test')
        self.manager.AddCommunication('C:6test')

        self.manager.ParseServerCommunication()
        self.assertEqual(['A:5test','C:6test','B:4test','A:5test','C:6test'],self.manager.GetCommunication())

suite = unittest.TestSuite()
suite.addTest(TestClass('testWithoutAddFunction'))
suite.addTest(TestClass('testAddOnce2Function'))
suite.addTest(TestClass('testAddOnce3Function'))
suite.addTest(TestClass('testAddOnce4Function'))
suite.addTest(TestClass('testAddOnce5Function'))
suite.addTest(TestClass('testAddOnce6Function'))

unittest.TextTestRunner(verbosity=2).run(suite)