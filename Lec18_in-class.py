### Lec18 Presenting Stimulation Results, Pylab, Plotting ###

# 1. inner loop that simulates 1 trial
# 2. 'enclose' inner loop in a loop that conducts *appropriate* number of trials
# 3. calculate & present relevant statistics

# Random walks have a wide applications:
  # Brownian motion
  # Stock market
  # Kinetics in Biology
  # Evolution

from pylab import *
# pylab is based on NumPy
# functionalities from Matlab in Python interface
import random

# plot([1,2,3,4])
# plot([5,6,7,8])
# # both plots showed on the same figure
# # use default x-values if not given
# # line chart
# plot([1,2,3,4], [1,4,9,16]) #([x], [y])

# starts a new blank figure
figure()
# dot chart
plot([1,2,3,4], [1,4,9,16], 'ro') # red-O
# axis([x0,x, y0,y])
axis([0,6,0,20])
title('Earnings')
xlabel('Days')
ylabel('Dollars')

figure()
# array (data type) in NumPy is a matrix
xAxis = array([1,2,3,4])
# print(xAxis)      # output: [1 2 3 4]
# arange() gives an array of ints
# test = arange(1,5)
# print(test)       # output: [1 2 3 4]
# print(test == xAxis)  # output: [ True True True True]
yAxis = xAxis**3
plot(xAxis, yAxis, 'ro')

figure()
vals = []
dieVals = [1,2,3,4,5,6]
# 10000 dies
for i in range(10000):
    vals.append(random.choice(dieVals)+random.choice(dieVals))
# a normal distribution
hist(vals, bins=11)

show()


