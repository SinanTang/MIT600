### Lec20: Monte Carlo Simulations, Estimating pi ###

# Stochastic* vs Deterministic(always produces the same result)
# Static vs Dynamic*
# Discrete* vs Continuous

# Monte Carlo
  # inferential statistics
    # random sample tends to exhibit the same properties as the population
    # from which it is drawn


from pylab import *
import random, math
import locale, os

def flipTrial(numFlips):
    heads, tails = 0, 0
    for i in range(numFlips):
        coin = random.randint(0, 1)
        if coin == 0: heads += 1
        else: tails += 1
    return heads, tails

def simFlips(numFlips, numTrials):
    diffs = []
    for i in range(numTrials):
        heads, tails = flipTrial(numFlips)
        diffs.append(abs(heads - tails))
    diffs = array(diffs)
    # print(diffs)
    diffMean = sum(diffs) / len(diffs)
    diffPercent = (diffs / float(numFlips))*100
    # print(diffPercent)
    percentMean = sum(diffPercent) / len(diffPercent)

    hist(diffs)
    axvline(diffMean, color = 'r', label = 'Mean')
    legend()
    titleString = str(numFlips) + ' Flips, ' + str(numTrials) + ' Trials'
    title(titleString)
    xlabel('Difference between heads and tails')
    ylabel('Number of Trials')

    figure()
    plot(diffPercent)
    axhline(percentMean, color = 'r', label = 'Mean')
    legend()
    title(titleString)
    xlabel('Trial Number')
    ylabel('Percent Difference between heads and tails')


# simFlips(100,100)
# simFlips(1000,100)
 # the range is narrower for larger numFlips, percent-wise

# flip 3 coins and see the probability of 3-heads or 3-tails
# simFlips(3, 4000)  # diffMean: 1.5


# show()

## Guessing the value of a current state is no difference from predicting
## the value of a future state, when you don' have the information.

## Is past behaviour a good prediction of future?



## Estimating Pi ##

# Buffon & Laplace: needle-throwing stimulation

# computer simulation

# tell Python which local standard to use
if os.name in ['MAC', 'posix']:
    # name of operating system
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # MAC version
else:
    locale.setlocale(locale.LC_ALL, '') # PC version

# format ints according to local standard
def formatInt(i):
    return locale.format('%d', i, grouping=True)
                                # grouping -> thousand-seperater comma
# print(formatInt(2000000))


def throwDarts(numDarts, shouldPlot):
    inCircle = 0
    estimates = []
    for darts in range(1, numDarts+1, 1):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x + y*y) <= 1.0:
            inCircle += 1
        if shouldPlot:
            piGuess = 4*(inCircle/float(darts))
            estimates.append(piGuess)
        if darts%1000000 == 0: # so I know it's making progress
            piGuess = 4*(inCircle/float(darts))
            # dartsStr = locale.format('%d', darts, True)
            print('Estimate with', formatInt(darts), 'darts:', piGuess)
    if shouldPlot:
        xAxis = arange(1, len(estimates)+1)
        semilogx(xAxis, estimates)
        titleString = 'Estimates of pi, final estimate: ' + str(piGuess)
        title(titleString)
        xlabel('Number of Darts Thrown')
        ylabel('Estimate of pi')
        axhline(3.1415926)
    return 4*(inCircle/float(numDarts))

def findPi(numDarts, shouldPlot=False):
    piGuess = throwDarts(numDarts, shouldPlot)
    print('Estimated value of pi with', formatInt(numDarts), 'darts:', piGuess)


# findPi(10000, True)
findPi(100000000)
show()
