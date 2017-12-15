import pubcapi

# Fetch current buy order for GBP > BTC
def getbtcprice():
    global btcgbp
    # The Api Class cheats a bit and uses blockcain.info to get the GBP price
    jsondata = pcapi.getbtcprice()
    gbpdata = jsondata.get("GBP")
    btcgbp = gbpdata.get("buy")
    return btcgbp

btcgbp = 0
pcapi = pubcapi.PubCApi()
print(getbtcprice())
print(pcapi.getcurrencies())
print(pcapi.gettradepairs())