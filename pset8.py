# 6.00 Problem Set 8
#


import time

# SUBJECT_FILENAME = "subjects.txt"
SUBJECT_FILENAME = "subjects_small.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    subjects = {}
    with open(filename) as inputFile:
        for line in inputFile.readlines():
            line = line.strip()
            line = line.split(',')
            # print(line[0])
            subjects[line[0]] = (int(line[1]), int(line[2]))
    return subjects


subjects = loadSubjects(SUBJECT_FILENAME)
# print(subjects)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    # subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:  ' + str(totalVal) + '\n'
    res = res + 'Total Work:  ' + str(totalWork) + '\n'
    print(res)

# printSubjects(subjects)



#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # first sort the subject list according to preference (comparator)
    # then within the limit of max work hours, select subjects from top of preference list

    def sortAll(subjects, comparator):
        """
        returns a sorted list, with elements being the keys of subjects, according to the comparator rule
        algorithm: insertion sort
        order: from best to worst
        """
        subList = list(subjects.keys())

        for i in range(1, len(subList)):
            val = subList[i]
            index = i
            while index > 0 and comparator(subjects[val], subjects[subList[index - 1]]):
                subList[index] = subList[index - 1]
                index -= 1
            subList[index] = val
        return subList

    sortedSubjects = sortAll(subjects, comparator)
    # print(sortedSubjects)

    selected = {}
    countWork = 0

    for i in sortedSubjects:
        if (subjects[i][WORK] > maxWork) or (countWork + subjects[i][WORK] > maxWork):
            # print('continues to the next subject...')
            continue
        selected[i] = subjects[i]
        countWork += subjects[i][WORK]
        # print(i, countWork, selected)

    return selected


def greedyTest():
    print(greedyAdvisor(subjects, 15, cmpWork))
    print()
    print(greedyAdvisor(subjects, 40, cmpWork))
    print()
    print(greedyAdvisor(subjects, 15, cmpValue))
    print()
    print(greedyAdvisor(subjects, 40, cmpValue))
    print()
    print(greedyAdvisor(subjects, 15, cmpRatio))
    print()
    print(greedyAdvisor(subjects, 25, cmpRatio))

# greedyTest()
selected = greedyAdvisor(subjects, 15, cmpValue)
# printSubjects(selected)



#
# Problem 3: Subject Selection By Brute Force
#

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue


def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...


# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance



#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...



#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...



# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.