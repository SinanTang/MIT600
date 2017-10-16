### Lec23: Stock Market Simulation ###

""" simulation scenario

2 strategies to invest in the stock market
  - indexed portfolio (take everything on the market)
  -  managed portfolio (depend on an investor to pick a few stocks)

theory: Model of the stock market
    # Efficient Market Hypothesis
      - assert the market is informationally efficient
      - random walk

building a stimulation:
 1. class to have?
    - stock(comes first, easier to do unit test) & market
 2.

"""

import pylab, random

class Stock(object):
    def __init__(self, price, distribution):
        self.price = price
        self.history = [price]
        self.distribution = distribution
        self.lastChange = 0

    def setPrice(self, price):
        self.price = price
        self.history.append(price)

    def getPrice(self):
        return self.price

    def makeMove(self, mktBias, mo):
        """

        :param mktBias:
        :param mo: momentum, for momentum investors, those who believe the stock market
        is NOT memoryless (Poisson distribution) - today's change correlates to yesterday's change
        :return:
        """
        # if self.price == 0: return # a bug
        oldPrice = self.price
        baseMove = self.distribution() + mktBias
        # multiplicative vs additive factor
        self.price = self.price * (1.0 + baseMove)
        self.price += mo * random.gauss(.25, .25) * self.lastChange
        if self.price < 0.01:
            self.price = 0.0
        self.history.append(self.price)
        self.lastChange = self.price - oldPrice

    def showHistory(self, figNum):
        pylab.figure(figNum)
        pylab.plot(self.history)
        pylab.title('Closing Price, Test ' + str(figNum))
        pylab.xlabel('Day')
        pylab.ylabel('Price')


def unit_test_stock():
    def runSim(stks, fig, mo):
        mean = 0.0
        for s in stks:
            for d in range(numDays):
                s.makeMove(bias, mo)
            s.showHistory(fig)
            mean += s.getPrice()
        mean = mean / float(numStks)
        pylab.axhline(mean)

    numStks = 20
    numDays = 200
    stks1 = []
    stks2 = []
    bias = 0.001
    mo = True
    for i in range(numStks):
        # create volatility
        volatility = random.uniform(0, 0.2)
        # create distributions
        d1 = lambda: random.uniform(-volatility, volatility)
        # random.uniform() returns any value within the range
        d2 = lambda: random.gauss(0.0, volatility/2.0)
        # random.gauss(mean, volatility)
        # Gussian distribution may display more extreme values
        stks1.append(Stock(100.0, d1))
        stks2.append(Stock(100.0, d2))

    runSim(stks1, 1, mo)
    runSim(stks2, 2, mo)

unit_test_stock()
pylab.show()
assert False


