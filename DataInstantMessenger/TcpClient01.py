import tkinter as tk                       # 視窗圖形化標準模組
from tkinter import scrolledtext as tkSt   # 視窗圖形化標準模組 (帶有滾動條的視窗)
from tkinter import messagebox as tkMs     # 視窗圖形化標準模組 (提示對話視窗)
import socket                              # 連線標準模組
import threading

def APISend(sock, addr, _selfStr,):
    while True:
        string = str(_selfStr)
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        return
        
def selfTextSend():
    _selfStr = inputText.get('1.0','end-1c')    # 獲取 input 的內容。
    inputText.delete(1.0,'end')                 # 刪除 input 的內容。

    if _selfStr != "" :                         # str 不是 空字串 的狀況下...建立編輯個人視窗。

        textEdit.config(state='normal')             # 開啟聊天室編輯的功能

        title = ('客戶端1:')+'\n'                    # 建立用戶title
        textEdit.insert(tk.INSERT,title,'guest')   # 顯示title，並賦予藍色。
        textEdit.insert(tk.INSERT,_selfStr+'\n')  # 顯示輸入值，並換行。
        textEdit.see('end')                        # 設定 滾動條拉 移至最新消息。

        textEdit.config(state='disabled')           # 停止聊天室編輯的功能

        ts = threading.Thread(target=APISend, args=(sC, host, _selfStr)) # 傳送發送訊息 至 另一端口
        ts.start()
        return                                
    else:
        tkMs.showerror('警告',"不能發送空白訊息！")

def getInfo(sock, addr):
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024).decode('utf8')+'\n'
        
        while True:
            textEdit.config(state='normal')             # 開啟聊天室編輯的功能

            textEdit.insert(tk.END,data,'server')   # 顯示輸入值，並換行。
            textEdit.see('end')                        # 設定 滾動條拉 移至最新消息。

            textEdit.config(state='disabled')           # 停止聊天室編輯的功能
            break
            
# 建立 socket 物件
sC = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     
host = ('127.0.0.1', 9999)      # 獲取本地主機名

# 建立 tkinter 物件
root = tk.Tk()          
uesName = '客戶端1'
root.title(uesName)     # 建立 視窗title Name

#顯示聊天窗口
textEdit = tkSt.ScrolledText(root,width = 40 , height = 20 )  # 建立 聊天室顯示窗口
textEdit.grid (pady = 5 , padx = 5 )                          # 設定 聊天室顯示窗口內縮 (好看而已)
textEdit.tag_config('guest',foreground='blue')                # 設定 客戶端輸入顯示的顏色為藍
textEdit.tag_config('server',foreground='red')                # 設定 客戶端輸入顯示的顏色為藍
textEdit.config (state='disabled')                            # 執行 停止聊天室編輯的功能

#編輯窗口
inputText = tkSt.ScrolledText(root,width = 40 , height = 3 ) # 建立 聊天室輸入窗口
inputText.grid (pady = 5 , padx = 5 )                        # 設定 聊天室輸入窗口 (好看而已)

#發送按鈕
btnSend = tk.Button(text='發送', width = 5, height = 2, command = selfTextSend) # 建立 發送按鈕
btnSend.grid(row=2,column=0)                                                    # 設定 按鈕位置

print("-----歡迎來到聊天室-----")
name = uesName
print('-----------------%s------------------' % name)

#接收線程
tkt=threading.Thread(target=getInfo, args=(sC, host), daemon=True)
tkt.start()

root.mainloop()