import yfinance as yf

print("--------------------------------------------------------------")


def stockSymbol(): #starts here
    ticker = ["ATVI"] #can hold multiple stocks
    dataDownload(ticker)


def dataDownload(stocks): #called by stockSymbol() to download information from each listed stock
    print(stocks)
    for ticker in stocks:
        data = yf.download(ticker, start="2010-06-01", end="2020-06-01", interval="1d")
        data = data.dropna()
        dayAlignment(data, ticker, monStorage(), tuesStorage(), wednesStorage(), thursdayStorage(), fridayStorage(), totalmonStorage(), totaltueStorage(), totalwedStorage(), totalthurStorage(), totalfriStorage())


def totalmonStorage():
    totalmondayList = []
    return totalmondayList


def totaltueStorage():
    totaltuesdayList = []
    return totaltuesdayList


def totalwedStorage():
    totalwednesdayList = []
    return totalwednesdayList


def totalthurStorage():
    totalthursdayList = []
    return totalthursdayList


def totalfriStorage():
    totalfridayList = []
    return totalfridayList

def monStorage():
    mondayList = []
    return mondayList


def tuesStorage():
    tuesdayList = []
    return tuesdayList


def wednesStorage():
    wednesdayList = []
    return wednesdayList


def thursdayStorage():
    thursdayList = []
    return thursdayList


def fridayStorage():
    fridayList = []
    return fridayList


def dayAlignment(fianceData, ticker, mondayList, tuesdayList, wednesdayList, thursdayList, fridayList, totalmondayList, totaltuesdayList, totalwednesdayList, totalthursdayList, totalfridayList ): #called by dataDownload() to sort every index by day
    print("First Date of " + ticker + " series")
    print(fianceData.index[0])
    print("Last Date of " + ticker + " series")
    print(fianceData.index[-1])
    print("__________________________")

    for index, row in fianceData.iterrows(): #iterates through rows
        if index.isoweekday() == 1:
            open = row['Open']
            close = row['Close']

            flatgain = close - open
            totalmondayList.append(round(flatgain, 2))

            percentage = (close - open) / open * 100
            mondayList.append(round(percentage, 2))

        if index.isoweekday() == 2:
            open = row['Open']
            close = row['Close']

            flatgain = close - open
            totaltuesdayList.append(round(flatgain, 2))

            percentage = (close - open) / open * 100
            tuesdayList.append(round(percentage, 2))

        if index.isoweekday() == 3:
            open = row['Open']
            close = row['Close']

            flatgain = close - open
            totalwednesdayList.append(round(flatgain, 2))

            percentage = (close - open) / open * 100
            wednesdayList.append(round(percentage, 2))

        if index.isoweekday() == 4:
            open = row['Open']
            close = row['Close']

            flatgain = close - open
            totalthursdayList.append(round(flatgain, 2))

            percentage = (close - open) / open * 100
            thursdayList.append(round(percentage, 2))

        if index.isoweekday() == 5:
            open = row['Open']
            close = row['Close']

            flatgain = close - open
            totalfridayList.append(round(flatgain, 2))

            percentage = (close - open) / open * 100
            fridayList.append(round(percentage, 2))

    functionCallList(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList)
    print("__________________________")


def functionCallList(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList):
    listStorage(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList)
    highlowCalculator(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList)
    bestDay(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList)

def listStorage(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList):
    listConcat(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList)


def listConcat(mondayList, tuesdayList, wednesdayList, thursdayList, fridayList):
    totalResults = mondayList + tuesdayList + wednesdayList + thursdayList + fridayList
    valueCalculation(totalResults)


def bestDay(monday, tuesday, wednesday, thursday, friday):
    averagemon = sum(monday) / len(monday)
    averagetues = sum(tuesday) / len(tuesday)
    averagewed = sum(wednesday) / len(wednesday)
    averagethur = sum(thursday) / len(thursday)
    averagefri = sum(friday) / len(friday)

    daylist = {"monday": averagemon, "tuesday": averagetues, "wednesday": averagewed, "thursday": averagethur, "friday": averagefri}
    bestDay = max(daylist, key=daylist.get)
    print(" The best day on average is: " + bestDay)
    worstDay = min(daylist, key=daylist.get)
    print(" The worst day on average is: " + worstDay)


def valueCalculation(totalResults):
    maxium = max(totalResults)
    print(" Highest percentage gain in a day: " + str(maxium) + "%")

    lowest = min(totalResults)
    print(" Lowest percentage gain in a day: " + str(lowest) + "%")

    totalDays = len(totalResults)
    print(" Total number of days for stock " + str(totalDays) + " days ")


def highlowCalculator(monday, tuesday, wednesday, thursday, friday):
    highCalc(monday, tuesday, wednesday, thursday, friday)
    lowCalc(monday, tuesday, wednesday, thursday, friday)


def highCalc(monday, tuesday, wednesday, thursday, friday):
    high = [max(value) for value in zip(monday, tuesday, wednesday, thursday, friday)]
    if high[0] == monday[0]:
        print(" Highest Single day gain(%): Monday")
    if high[0] == tuesday[0]:
        print(" Highest Single day gain(%): Tuesday")
    if high[0] == wednesday[0]:
        print(" Highest Single day gain(%): Wednesday")
    if high[0] == thursday[0]:
        print(" Highest Single day gain(%): Thursday")
    if high[0] == friday[0]:
        print(" Highest Single day gain(%): Friday")


def lowCalc(monday, tuesday, wednesday, thursday, friday):
    low = [min(value) for value in zip(monday, tuesday, wednesday, thursday, friday)]
    if low[0] == monday[0]:
        print(" Highest single day loss(%): Monday")
    if low[0] == tuesday[0]:
        print(" Highest single day loss(%): Tuesday")
    if low[0] == wednesday[0]:
        print(" Highest single day loss(%): Wednesday")
    if low[0] == thursday[0]:
        print(" Highest single day loss(%): Thursday")
    if low[0] == friday[0]:
        print(" Highest single day loss(%): Friday")

stockSymbol()

