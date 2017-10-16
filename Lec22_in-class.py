### Lec22: Normal, Uniform and Exponential Distributions ###

# fitting old values != fitting new values

# notion of Distribution
  # Normal, Gaussian, Bell-curve
    # 2 factors needed for a stable distribution: mean, standard deviation(statistical dispersion)
      # stable distribution: the shape doesn't change with the scale
      # sigma = math.sqrt(E(xˆ2 - (E(x))ˆ2))
      # Empirical Rule for normal distribution: 68%(std1), 95%(std2), 99.7%(std3)

# symmetric / asymmetric distribution
# Uniform distribution: each value is equally likely
  # not very frequent to appear in nature
# Exponential distribution:
  # quite frequent to appear
  # e.g. the amount of traffic on website

# degree of predictability: uniform < normal < exponential

## Misuse/Sins of data ##
  # 0) beware of people who give you properties of data but not the data
  # 1) cum hoc ergo propter hoc -> correlation != causation (logical fallacy)
      # a *lurking variable* can exist...
  # 2) beware of non-response bias (non-representative samples)
  # 3) data enhancement - reading more into the data than it actually applies
        # we should put data in context
      # in particular, extrapolate data
  # 4) (most common) Texas sharp shooter fallacy - draw conclusion based on data without prior hypothesis



import random, pylab

fair = [1,2,3,4,5,6]

def throw_pair(vals1, vals2):
    d1 = random.choice(vals1)
    d2 = random.choice(vals2)
    return d1, d2


def conduct_trials(numThrows, die1, die2):
    throws = []
    for i in range(numThrows):
        d1, d2 = throw_pair(die1, die2)
        throws.append(d1+d2)
    return throws


numThrows = 100000

throws = conduct_trials(numThrows, fair, fair)
pylab.hist(throws, 11)
# pylab.xticks: where to put markers on x-axis & what they should be
pylab.xticks(range(2, 13), ['2','3','4','5','6','7','8','9','10','11','12'])
pylab.title('Distribution of Values')
pylab.xlabel('Sum of Two Die')
pylab.ylabel('Number of Throws')
## normal distribution


# Get probabilities for fair dice - another way to look at the same data
pylab.figure()
sums = pylab.array([0]*14)
for val in range(2, 13):
    sums[val] = throws.count(val)
probs = sums[2:13]/float(numThrows)
xVals = pylab.arange(2, 13)
pylab.plot(xVals, probs, label='Fair Dice')
pylab.xticks(range(2, 13), ['2','3','4','5','6','7','8','9','10','11','12'])
pylab.title('Probability of a Value')
pylab.xlabel('Sum of Two Die')
pylab.ylabel('Probability')



def craps(die1, die2):
    """
    return True if shooter wins at craps by betting pass line
    """
    d1, d2 = throw_pair(die1, die2)
    tot = d1 + d2
    if tot in [7, 11]: return True
    if tot in [2, 3, 12]: return False
    point = tot
    while True:
        d1, d2 = throw_pair(fair, fair)
        tot = d1 + d2
        if tot == point: return True
        if tot == 7: return False


def sim_craps(numBets, die1, die2):
    wins, losses = (0, 0)
    for i in range(numBets):
        if craps(die1, die2): wins += 1
        else: losses += 1
    print(wins, losses)
    houseWin = float(losses) / float(numBets)
    print(houseWin)
    print('House winning percentage: {}%'.format(100*houseWin))
    print('House profits per ${} bet: ${}'.format(numBets, losses-wins))


sim_craps(100000, fair, fair)

# try some unfair dice
# weighted = [1,1,2,3,4,5,6] # favors the house
weighted = [1,2,3,4,5,5,6] # favors the player
throws = conduct_trials(numThrows, fair, weighted)
sums = pylab.array([0]*14)
for val in range(2, 13):
    sums[val] = throws.count(val)
probs = sums[2:13]/float(numThrows)
xVals = pylab.arange(2, 13)
pylab.plot(xVals, probs, label = 'Weighted Dice')
pylab.legend()
sim_craps(100000, fair, weighted)

pylab.show()



