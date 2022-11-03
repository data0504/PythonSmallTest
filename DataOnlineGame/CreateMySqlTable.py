import mysql.connector

class MySQLTidy:
    def __init__(self): # 連結 MySQL 規格。
        self.con = mysql.connector.connect(
            host = '127.0.0.1',
            port = '3306',
            user = 'root',
            password = '0000',
            database = 'online_game',
            charset = 'utf8')

        self.cursor = self.con.cursor()

    def closeMySQL(self):
        self.con.close()
        self.cursor.close()

    def createTable(self): # 創建 空Table.
        createTableAccounts = "CREATE TABLE `Accounts`\
            (`accounts_id` INT NOT NULL,\
            `account` VARCHAR(10) NOT NULL,\
            `password` VARCHAR(10) NOT NULL,\
            `initToken` int NOT NULL,\
            `signUpTime` DECIMAL(17,7) NOT NULL,\
            `signInTime` DECIMAL(17,7) NOT NULL,\
            `pay` DECIMAL(9,2) NOT NULL,\
            `getCoin` DECIMAL(9,2) NOT NULL,\
            `rebate` DECIMAL(9,2) NOT NULL,\
            PRIMARY KEY(`accounts_id`));"

        self.cursor.execute(createTableAccounts)

MST = MySQLTidy()
MST.createTable()
MST.closeMySQL()