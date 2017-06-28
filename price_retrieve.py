import requests
import time
from collections import deque


currentBid = 0.0
currentAsk = 0.0
previousBid = 0.0
previousAsk = 0.0

firstRun = 1;
queueItemsCount = 0
maxItemsList = 100



while True:
    r = requests.get('https://www.therocktrading.com/api/ticker/ETHEUR')
    data = r.json()
    currentBid = data['result'][0]['bid'];
    currentAsk = data['result'][0]['ask'];



    if (firstRun == 1):
        firstRun = 0
        askHistory = deque([currentAsk])
    else:
        if (abs(currentAsk - previousAsk) > 0.01):
            print ("--- Ask Variation 1 Trans: " + str(currentAsk - previousAsk))

        queueItemsCount = queueItemsCount + 1
        if (queueItemsCount >= maxItemsList):
            askHistory.popleft()
            queueItemsCount = queueItemsCount - 1
            if(abs(currentAsk - askHistory[0]) > 0.01):
                print ("--- Ask Variation 100 Trans: " + str(currentAsk - askHistory[0]))

        print "Number of transactions in memory: " + str(queueItemsCount) + " of " + str(maxItemsList)

        askHistory.append(currentAsk)
        #print (askHistory)


    print ("Last Read. Bid: " + str(data['result'][0]['bid']) + "  -  Ask: " + str(data['result'][0]['ask']))
    previousBid = currentBid
    previousAsk = currentAsk





    time.sleep (10)




