import pyupbit
import time
from datetime import datetime

while True:
    time.sleep(1)
    CurrentPrice = pyupbit.get_current_price("KRW-BTC")
    CurrentPrice2 = pyupbit.get_current_price("KRW-ETH")
    CurrentPrice3 = pyupbit.get_current_price("KRW-BTT")
    CurrentPrice4 = pyupbit.get_current_price("KRW-MLK")
    CurrentPrice5 = pyupbit.get_current_price("KRW-BORA")
    CurrentPrice6 = pyupbit.get_current_price("KRW-XRP")
    now = datetime.now()
    print(now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
    print("")
    print("비트코인 : "+ str(CurrentPrice))
    print("이더리움 : "+ str(CurrentPrice2))
    print("비트토렌트 : "+ str(CurrentPrice3))
    print("밀크 : "+ str(CurrentPrice4))
    print("보라 : "+ str(CurrentPrice5))
    print("리플 : "+ str(CurrentPrice6))
    print("===============================")

    f = open('C:\\xampp\\htdocs\\live_btc\\btc.json','w')
    text = {"BTC": CurrentPrice, "ETH": CurrentPrice2, "BTT": CurrentPrice3, "MLK": CurrentPrice4, "BORA": CurrentPrice5, "XRP": CurrentPrice6}
    f.write(str(text))
    f.close()