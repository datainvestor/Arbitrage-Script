import urllib.request, json 
from pushbullet.pushbullet import PushBullet


with urllib.request.urlopen("https://www.bitmarket.pl/json/BTCEUR/orderbook.json") as url:
    bitmarketdata = json.loads(url.read().decode())
    #print(bitmarketdata['bids'])
with urllib.request.urlopen("https://api.gdax.com/products/btc-eur/book/?level=2") as url:
    gdaxdata = json.loads(url.read().decode())
    #print(gdaxdata['bids'])
    
value=12000
k=0
pricelist=[]
weightlist=[]
while True:
    if value-bitmarketdata['asks'][k][0]*bitmarketdata['asks'][k][1]>0:
        value=value-bitmarketdata['asks'][k][0]*bitmarketdata['asks'][k][1]
        #print("remaining value", value)
        pricelist.append(bitmarketdata['asks'][k][0]*bitmarketdata['asks'][k][1])
        weightlist.append(bitmarketdata['asks'][k][1]*0.997) #0.997 zaklada 0,3% prowizje
        #print(pricelist)
        #print(weightlist)
        k=k+1
        continue
    else:
        remaining=value/bitmarketdata['asks'][k][0]
        pricelist.append(remaining*bitmarketdata['asks'][k][0])
        weightlist.append(remaining*0.997)
        #print("remaining value", value-remaining*bitmarketdata['asks'][k][0])
        #print(pricelist)
        #print(weightlist)
        break

bitmavg=sum(pricelist)/sum(weightlist)

print(sum(weightlist), 'of bitcoin will be bought for avg price of', bitmavg)
btcamount=sum(weightlist)-0.0009

value=btcamount
k=0
pricelist=[]
weightlist=[]
while True:
    if value-float(gdaxdata['bids'][k][1])>0:
        value=value-float(gdaxdata['bids'][k][1])
        #print("remaining value", value)
        pricelist.append(float(gdaxdata['bids'][k][0])*float(gdaxdata['bids'][k][1]))
        weightlist.append(float(gdaxdata['bids'][k][1]))
        #print(pricelist)
        #print(weightlist)
        k=k+1
        continue
    else:
        remaining=value
        pricelist.append(remaining*float(gdaxdata['bids'][k][0]))
        weightlist.append(remaining)
        #print("remaining value", value-remaining)
        #print(pricelist)
        #print(weightlist)
        break

gdaxavg=sum(pricelist)/sum(weightlist)

print(sum(weightlist), 'of bitcoin will be sold for avg price of', gdaxavg)

arbitrage=gdaxavg-bitmavg
#print(arbitrage)

string1=str(arbitrage)


apiKey = "o.nYrBuXGCAfYrQmvNCn2yahywKHw5s0c3"
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()
devices

p.pushNote(devices[0]["iden"], 'Buy at bitmarket/sell at gdax: ', string1)
