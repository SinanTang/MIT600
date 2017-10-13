### Lec21: Validating Simulation Results, Curve Fitting, Linear Regression ###

# 2 related questions #
# How many samples?
# How accurate do I believe my results?

# the issue: it's never possible to achieve perfect accuracy through sampling
# Biased sample

# but with some assumptions, we can predict how *likely* the results are accurate

# statistical validity != correctness

# -> check results against physical reality

## The interplay of 3 things:
    # data
    # model which claims to explain the data
    # consequences of the models (plusible? true?)


# Example
# Spring constant (stiffness)
# Hooke's Law: F = -k*x

import pylab
import random

def getSpringData(fname):
    springData = open(fname, 'r')
    distances = []
    forces = []
    for line in springData:
        if line[0] == '#': continue
        line = line[:-1]
        elems = line.rsplit(':')
        distances.append(float(elems[0]))
        forces.append(float(elems[1]))
    return pylab.array(distances), pylab.array(forces)

# distances, forces = getSpringData('springData.txt')
# pylab.scatter(distances, forces)
# pylab.xlabel('Distance (Meters)')
# pylab.ylabel('|Force| (Newtons)')
# pylab.title('Force vs. Distance for Spring')


# not a straight line, b/c of experiment & measurement errors
# real data almost never match the theory precisely

# we need to find a line (linear function) that best fits the data
  # objective function -> trying to find a line to optimise this function
    # least squares fit: SUM(obsecuation, -prediction)ˆ2
  # using PyLab, polyfit

# k, b = pylab.polyfit(distances, forces, 1)
# yVals = k * distances + b
# pylab.plot(distances, yVals, c='r', linewidth=2)
# pylab.title('Force vs. Distance, k= ' + str(k))

# always look at the real data

def getData(fname):
    pass

# times, speeds = getData('speedData.txt')
#
# pylab.scatter(times, speeds)
# pylab.xlabel('Time (secs.)')
# pylab.ylabel('Speed (Meters/sec.)')
# a, b = pylab.polyfit(times, speeds, 1)
# yVals = a*times + b
# pylab.plot(times, yVals, c='r', linewidth=2)
# pylab.title('Speed vs. Time')
#
# print('R Squared Error, linear fit =', rSquare(speeds, yVals))
#
# ## modeling a quadratic function - parabola
# a, b, c = pylab.polyfit(times, speeds, 2)
# yVals = a*(times**2) + b*times + c
# pylab.plot(times, yVals, c='y', linewidth=4)
#
# print('R Squared Error, quadratic fit =', rSquare(speeds, yVals))



## Linear Regression
  # not just for lines

## compare different models
  # Rˆ2 - coefficient of determination
  # Rˆ2 = 1 - EE/DV
    # EE: errors in estimation, computed by comparing estimates to measured data
    # DV: variance in data, computed by mean of measured data to measured data

    # Rˆ2 = 0.9 -> 90% of variation in the variables can be explained by the model
      # lurking variable: something affecting the result but not in the model
      # need to worry when Rˆ2 is below 0.9
    # Rˆ2 = 1 -> perfect

def rSquare(measured, estimated):
    """
    computes Rˆ2
    :param measured: array
    :param estimated: array
    :return: Rˆ2, float
    """
    diffs = (estimated - measured) ** 2
    mMean = measured.sum() / float(len(measured))
    var = (mMean - measured) ** 2
    return 1 - diffs.sum()/var.sum()

# Quadratic fit can never be worse than linear fit

# but it's not always better to use a higher order polynomial model

numPts = 7
points = []
xVals = pylab.arange(numPts)
for x in xVals: points.append(x + random.random())
points = pylab.array(points)
pylab.scatter(xVals, points)

a1, b1 = pylab.polyfit(xVals, points, 1)
estVals1 = a1*xVals + b1
print('linear fit to points:', rSquare(points, estVals1))
pylab.plot(xVals, estVals1, c='r')

a,b,c,d,e,f = pylab.polyfit(xVals, points, 5)
estVals5 = a*(xVals**5) + b*(xVals**4) + c*(xVals**3) + d*(xVals**2) + e*xVals + f
print('5th order fit to same points:', rSquare(points, estVals5))
pylab.plot(xVals, estVals5, c='y')

# 5th order fit is a closer/tighter model
  # but not very predictive..
# but Closer/Tighter != Better

# Generate more points using same algorithm
pylab.figure()
xVals = pylab.arange(2*numPts)
points = list(points)
for x in range(numPts, 2*numPts): points.append(x + random.random())
points = pylab.array(points)
pylab.scatter(xVals, points)

# predict more data using 2 old models
estVals5 = a*(xVals**5) + b*(xVals**4) + c*(xVals**3) + d*(xVals**2) + e*xVals + f
pylab.plot(xVals, estVals5, c = 'r')
estVals1 = a1*xVals + b1
pylab.plot(xVals, estVals1, c='b')

# the quadratic fit is *overfitting*
# very complex model has high chance of being overfitting
# be aware of stats without any real theory

pylab.show()
