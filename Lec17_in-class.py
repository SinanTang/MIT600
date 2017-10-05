### Lec17: Computational Models: Random Walk Simulation ###

# Informal Problem Description -> Formal/Rigorous Problem Statement
# Inventing computational models

  # Dealing with & exploiting randomness
    # stochastic models

  # Making sense of data
    # e.g. visualise data

  # Evaluating the quality of answers


## the Problem: how far can a drunk student walk on a field after xx seconds?
    # start simple!
    # cartesian plane
    # assume only 4 possible directions (NSEW) to walk in
    # *Simulate* a *random walk*

      # design the structure of the problem
        # what data abstractions are needed?
            # Location
            # CompassPt (direction)
            # Field
            # Drunk


import math, pylab, random
# random module - pseudo random
# pylab - brings into Python a lot of features of Matlab

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
    # global variable
    def __init__(self, pt):
        if pt in self.possibles: self.pt = pt
        # we need self in self.possibles, b/c self here refers to
        # the class CompassPt, rather than an instance of the class.
        # Classes are objects
        else: raise ValueError('in CompassPt.__init__')
         # says where the error is coming from
    def move(self, dist):
        if self.pt == 'N': return (0, dist)
        elif self.pt == 'S': return (0, -dist)
        elif self.pt == 'E': return (dist, 0)
        elif self.pt == 'W': return (-dist, 0)
        else: raise ValueError('in CompassPt.move')

# What decisions are encapsulated in the first 2 classes?
    # it's a 2-dimensional space
    # only 4 directions to move towards


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
    # the move of one class is defined by the move of another class -> modularity
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk

# What decisions are encapsulated in class Field?
    # only one drunk in the field


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def move(self, field, time=1):
    # defualt values (time=1) for parameters
        if field.getDrunk() != self:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            # random.choice takes a sequence and picks one at random
            field.move(pt, 1)


def performTrial(time, f):
    start = f.getLoc()
    distances = [0.0]
    for t in range(1, time+1):
        f.getDrunk().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
    return distances


# drunk = Drunk('Homer Simpson')
# for i in range(3):
#     f = Field(drunk, Location(0,0))
#     distances = performTrial(500, f)
#     pylab.plot(distances)
#
# pylab.title('Homer\'s Random Walk')
# pylab.xlabel('Time')
# pylab.ylabel('Distance from Origin')
#
# pylab.show()
# assert False

# to be more organised...
def performSim(time, numTrials):
    distLists = []
    for trial in range(numTrials):
        d = Drunk('Drunk' + str(trial))
        f = Field(d, Location(0,0))
        distances = performTrial(time, f)
        distLists.append(distances)
    return distLists

def ansQuest(maxTime, numTrials):
    means = []
    distLists = performSim(maxTime, numTrials)
    for t in range(maxTime+1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distL)) # bug? tot/len(distLists)
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('Average Distance vs Time (' + str(len(distLists)) + ' trials)')

ansQuest(500, 300)
pylab.show()


