import requests
import random
URL = f"https://api.freeapi.app/api/v1/public/stocks"
req = requests.get(URL)
data = req.json()
i=random.randint(0,9)
data = data["data"]["data"]
y = 0
for i in data:
    x= "Symbol = " + i["Symbol"]+", Name = "+i["Name"] +", Market Cap. = "+i["MarketCap"] +", Price = "+i["CurrentPrice"] +", High/low = "+i["HighLow"] 
    y=y+1
    print(f"{y}--> {x}")
    