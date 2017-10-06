### Lec19 Biased Random Walks, Distributions ###

# Biased random walks (variants of random walks)

# using classes to structure the program

# understanding data

# good design: isolate decisions in different parts of the program

import math, random, pylab

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def getCoords(self):
        return self.x, self.y
    def getDist(self, other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)


class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles: self.pt = pt
        else: raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N': return (0, dist)
        elif self.pt == 'S': return (0, -dist)
        elif self.pt == 'E': return (dist, 0)
        elif self.pt == 'W': return (-dist, 0)
        else: raise ValueError('in CompassPt.move')


class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc
    def move(self, cp, dist):
        """
        cp: CompassPt
        """
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk


## Game: Chutes & Ladders
  # change class Field
class oddField(Field):
    def isChute(self):
        x, y = self.loc.getCoords()
        return abs(x) - abs(y) == 0
    def move(self, cp, dist):
        Field.move(self, cp, dist)
        if self.isChute():
            self.loc = Location(0, 0)


class Drunk(object):
    def __init__(self, name=''):
        self.name = name
    def move(self, field, cp, dist=1):
        if field.getDrunk().name != self.name:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(dist):
            field.move(cp,1)

# have 3 kinds of drunks with the minimal amount of change to the code
class UsualDrunk(Drunk):
    def move(self, field, dist=1):
        cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), dist)
        # note the notation of call

class ColdDrunk(Drunk):
    def move(self, field, dist=1):
        cp = random.choice(CompassPt.possibles)
        if cp == 'S':
            Drunk.move(self, field, CompassPt(cp), 2*dist)
        else:
            Drunk.move(self, field, CompassPt(cp), dist)

class EWDrunk(Drunk):
    def move(self, field, time=1):
        cp = random.choice(CompassPt.possibles)
        while cp != 'E' and cp != 'W':
            cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), time)



def performTrial(time, f):
    start = f.getLoc()
    distances = [0.0]
    for t in range(1, time+1):
        f.getDrunk().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
    return distances


def performSim(time, numTrials, drunkType):
    distLists = []
    locLists = []
    for trial in range(numTrials):
        d = drunkType('Drunk' + str(trial)) # pass the type
    ## Polymorphism - different types of Drunk
        f = oddField(d, Location(0, 0))
        distances = performTrial(time, f)
        distLists.append(distances)
        locLists.append(f.getLoc())
    return distLists, locLists


def ansQuest(maxTime, numTrials, drunkType, title):
    means = []
    distLists, locLists = performSim(maxTime, numTrials, drunkType)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('ave. distance')
    pylab.xlabel('steps')
    pylab.title(title)

numSteps = 500
numTrials = 400
# ansQuest(numSteps, numTrials, UsualDrunk, 'UsualDrunk '+str(numTrials)+' Trials')
# ansQuest(numSteps, numTrials, ColdDrunk, 'ColdDrunk '+str(numTrials)+' Trials')
# a small bias can lead to huge difference
# ansQuest(numSteps, numTrials, EWDrunk, 'EWDrunk '+str(numTrials)+' Trials')
# EWDrunk similar to UsualDrunk
## Once the drunk leaves the original location, the expected distance is not zero
## anymore, b/c the baseline changes.


def ansQuest2(maxTime, numTrials, drunkType, title):
    distLists, locLists = performSim(maxTime, numTrials, drunkType)
    means = []
    for t in range(maxTime +1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot / len(distLists))

    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title(title+' Ave. Distance')

    lastX = []
    lastY = []
    for locList in locLists:
        x, y = locList.getCoords()
        lastX.append(x)
        lastY.append(y)
    pylab.figure()
    pylab.scatter(lastX, lastY)
    pylab.xlabel('EW Distance')
    pylab.ylabel('NS Distance')
    pylab.title(title + ' Final Locations')

    # pylab.figure()
    # pylab.hist(lastX)
    # pylab.xlabel('EW Values')
    # pylab.ylabel('Number of Trials')
    # pylab.title(title + ' Distributions of final EW Values')

ansQuest2(numSteps, numTrials, UsualDrunk, 'UsualDrunk '+str(numTrials)+' Trials')
# ansQuest2(numSteps, numTrials, EWDrunk, 'EWDrunk '+str(numTrials)+' Trials')


pylab.show()


## Computer Simulation
    # Manhattan Project - nuclear detonation
      # Monte Carlo Simulation
  # attempts to generate a sample of representative scenarios
  # seen as experimental device
  # descriptive, not prescriptive
  # can use simulation to do optimization