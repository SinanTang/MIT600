# Problem Set 11: Simulating robots

import math, random
import matplotlib
matplotlib.use("TkAgg")
import pylab
import pset11_visualise

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)



# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleanTiles = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if pos not in self.cleanTiles:
            self.cleanTiles.append(pos)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if Position(m ,n) in self.cleanTiles:
            return True
        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height * self.width

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x, y = round(random.uniform(0, self.width),2), round(random.uniform(0, self.height),2)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if 0 <= pos.getX() <= self.width and 0 <= pos.getY() <= self.height:
            return True
        return False


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        initialPosition = self.room.getRandomPosition()
        initialDirection = random.randint(0,360)
        self.p = initialPosition
        self.d = initialDirection

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.p

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newPos = self.p.getNewPosition(self.d, self.speed)
        if self.room.isPositionInRoom(newPos):
            self.p = newPos
            self.room.cleanTileAtPosition(newPos)
        else:
            while True:
                tmp_direction = random.randint(0, 360)
                tmp_position = self.p.getNewPosition(tmp_direction, self.speed)
                if self.room.isPositionInRoom(tmp_position): break
            self.setRobotPosition(tmp_position)
            self.setRobotDirection(tmp_direction)
            self.room.cleanTileAtPosition(self.p)


def testRobot():
    # testing above classes
    room = RectangularRoom(5, 5)
    robot = Robot(room, 0.5)
    print('initial position & direction:')
    print(robot.getRobotPosition(), robot.getRobotDirection())
    print('\nstarts moving...')
    tiles = room.getNumTiles()
    c = 0
    while room.getNumCleanedTiles() / tiles < 1:
        robot.updatePositionAndClean()
        print(room.getNumCleanedTiles())
        c += 1
    print(c)
    # for i in range(10):
    #     robot.updatePositionAndClean()
    #     print(robot.getRobotPosition(), robot.getRobotDirection())
    #     print()

# testRobot()



# === Problem 3


def robotls(num_robots, room, speed, robot_type):
    robotls = []
    for i in range(num_robots):
        robot = robot_type(room, speed)
        # print(robot.getRobotDirection(), robot.getRobotPosition())
        robotls.append(robot)
    return robotls

# room = RectangularRoom(10, 10)
# robotls(3, room, 1, Robot)

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type=Robot, visualize=False):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)

    return: list of lists, timestep is the len of each list
    """

    all_trials = []
    # tiles = room.getNumTiles()
    anim = pset11_visualise.RobotVisualization(num_robots, width, height)
    for i in range(num_trials):

        room = RectangularRoom(width, height)
        tiles = room.getNumTiles()
        coverage_all_robots = []
        robotList = robotls(num_robots, room, speed, robot_type)

        while room.getNumCleanedTiles()/tiles < min_coverage:
            for robot in robotList:
                robot.updatePositionAndClean()
                anim.update(room, robotList)
            coverage = room.getNumCleanedTiles() / tiles
            coverage_all_robots.append(coverage)
            # print(coverage_all_robots)

        all_trials.append(coverage_all_robots)
    anim.done()

    # print('all trials: ', all_trials)
    # for i in all_trials:
    #     print('time-step needed:', len(i))

## TODO: speed is not affecting the result ??

runSimulation(1, 1, 5,5, 1, 1, Robot, True)



# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """



# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here