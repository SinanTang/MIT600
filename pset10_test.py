import pset10
import importlib; importlib.reload(pset10)
from pset10 import *


def isClose(float1, float2):
    """
    Helper function - are two floating point values close?
    """
    return abs(float1 - float2) < .01

def testResult(boolean):
    """
    Helper function - print 'Test Failed' if boolean is false, 'Test
    Succeeded' otherwise.
    """
    if boolean:
        print('Test Succeeded')
    else:
        print('Test Failed')


def testHand():
    """
    Test the hand class. Add your own test cases
    """
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    h.update('bad')
    testResult(h.containsLetters('aabdd') and not h.isEmpty())
    h.update('dad')
    # print(h)
    testResult(h.containsLetters('ab') or not h.isEmpty())
    h.update('ab')
    # print(h.update('ab'), h)
    testResult(h.isEmpty())

    h2 = Hand(7, {'a': 2, 'c': 1, 'd': 2, 's':2})
    h2.update('as')
    testResult(h2.containsLetters('addcs') and not h2.isEmpty())
    h2.update('cs')
    testResult(h2.containsLetters('add') or not h2.isEmpty())
    testResult(h2.isEmpty())


def testPlayer():
    """
    Test the Player class. Add your own test cases.
    """
    p = Player(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))


def testComputerPlayer():
    """
    Test the ComputerPlayer class. Add your own test cases.
    """
    wordlist = Wordlist()
    p = ComputerPlayer(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(getWordScore(p.pickBestWord(wordlist)) == getWordScore('abode'))


def testAll():
    """
    Run all Tests
    """

    # print("Uncomment the tests in this file as you complete each problem.")

    # print('PROBLEM 2 -----------------------------------------')
    # testHand()

    # print('PROBLEM 3 -----------------------------------------')
    # testPlayer()

    # print('PROBLEM 4 -----------------------------------------')
    # testComputerPlayer()

testAll()