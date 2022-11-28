import requests, re, pandas, time
from bs4 import BeautifulSoup

# 各國家單一商品價格。
country_code1  = ['tw', 'us', 'uk', 'jp', 'kr']
commodityPrice = []
for country  in country_code1:
    res = requests.get(f'https://{country}.burberry.com/embroidered-oak-leaf-crest-cotton-pique-polo-shirt-p80651781')

    time.sleep(1)
    
    soup = BeautifulSoup(res.text, 'html.parser')
    priceText = soup.select_one('.product-info-panel__price').text
    text = float("".join(re.findall(r'\d+\.?\d*',priceText)))
    commodityPrice.append(text)
    
# 台灣 與 各國幣值匯率。
country_code2  = ['USD', 'GBP', 'JPY', 'KRW']
exchangeRate = []
defs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW", encoding='utf-8',header=0)
for i in defs:
    for j in range((len(i['幣別'])-1)):
        a = (i['幣別'][j+1])
        b = re.search('[a-zA-Z]+',str(a), flags=re.I).group(0)
        if b in country_code2:
            exchangeRate.append(i['現金匯率'][j+1])

# 台灣幣值 換 各國幣值匯率。
for i in range(len(commodityPrice)):
    if i != 0 :
        print(f'{country_code1[i]} {float(commodityPrice[i]) * float(exchangeRate[i-1])}')
    else:
        print(f'{country_code1[i]} {commodityPrice[i] * 1 }')

    print(" ")