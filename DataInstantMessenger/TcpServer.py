import socket               # 匯入 socket 模組

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # 建立 socket 物件
addr = ('127.0.0.1', 9999)
s.bind((addr))        # 繫結埠

user = {}  # 存放字典{addr:name}

while True:

    data, addr = s.recvfrom(1024)  # 等待接收客戶端訊息存放在2個變數data和addr裡
    if addr not in user:  # 如果addr不在user字典裡則執行以下程式碼
        user[addr] = data.decode('utf-8')  # 接收的訊息解碼成utf-8並存在字典user裡,鍵名定義為addr
        # print(f'{user}')
        continue  # 如果addr在user字典裡，跳過本次迴圈

       
    print((data.decode('utf-8')))  
    for address in user:    #從user遍歷出address
        if address != addr:  #address不等於addr時間執行下面的程式碼
            s.sendto(data, address)     #傳送data和address到客戶端