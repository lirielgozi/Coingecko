from pycoingecko import CoinGeckoAPI
import datetime

cg = CoinGeckoAPI()

# setting time
nowUnix = datetime.datetime.now().strftime("%s")
weekAgo = datetime.datetime.now() - datetime.timedelta(days=7)
weekAgoUnix = weekAgo.strftime("%s")
fmt = "%Y-%m-%d %H:%M:%S"

# print("Today in epoch: ", nowUnix)
# print("Week ago in epoch: ", weekAgoUnix)


dataOfDaysEURO = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=weekAgoUnix,
                                                      to_timestamp=nowUnix, localization=False)
dataOfDaysUS = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp=weekAgoUnix,
                                                    to_timestamp=nowUnix, localization=False)


def printPriceUS():
    print(" ****** LAST 7 DAYS BTC PRICE IN USD ******")
    for i in dataOfDaysUS['prices']:
        date = (i[0])
        price = (i[1])
        ts = datetime.datetime.fromtimestamp(float(date) / 1000.)

        print(ts.strftime(fmt), ":", round(price, 2), "USD")


def printPriceEuro():
    print(" ****** LAST 7 DAYS BTC PRICE IN EURO ******")
    for i in dataOfDaysEURO['prices']:
        date = (i[0])
        price = (i[1])
        ts = datetime.datetime.fromtimestamp(float(date) / 1000.)

        print(ts.strftime(fmt), ":", round(price, 2), "EURO")


def usPriceAvarage():
    placeHolder = 0
    index = len(dataOfDaysUS['prices'])
    for i in dataOfDaysUS['prices']:
        price = (i[1])
        placeHolder += price

    avarage = float(placeHolder / index)
    print("average price of BTC\\USD for the last 7 days is:", avarage, "USD\n")


def euroPriceAvarage():
    placeHolder = 0
    index = len(dataOfDaysEURO['prices'])
    for i in dataOfDaysEURO['prices']:
        price = (i[1])
        placeHolder += price

    avarage = float(placeHolder / index)
    print("average price of BTC\\EUR for the last 7 days is:", avarage, "EURO\n")


def printPriceTotal():
    printPriceUS()
    printPriceEuro()
    usPriceAvarage()
    euroPriceAvarage()


printPriceTotal()
