# 6.00 Problem Set 8
#


import time

SUBJECT_FILENAME = "subjects.txt"
# SUBJECT_FILENAME = "subjects_small.txt"
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
    subNames = list(subjects.keys())
    subNames.sort()
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
# selected = greedyAdvisor(subjects, 15, cmpValue)
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
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    """

    :param subjects:
    :param maxWork:
    :param i: index
    :param bestSubset: list of the index of selected subject
    :param bestSubsetValue:
    :param subset: [] or [n], n is an instance of i, not necessarily the same as i
    :param subsetValue:
    :param subsetWork:
    :return:
    """
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
            # print('after appending:', i, subset, bestSubset)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
            # print('after popping:', i, subset, bestSubset)
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

# printSubjects(bruteForceAdvisor(subjects, 25))


def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    def bruteForceTest(n):
        start = time.time()
        bruteForceAdvisor(subjects, n)
        end = time.time()
        compute_time = round(float(end - start), 3)
        print('Brute Force Algorithm: maxWork = {}, takes {}s to compute.'.format(n, compute_time))

    for i in range(5, 10):
        bruteForceTest(i)

    # bruteForceTest(5)  # 0.74379s
    # bruteForceTest(6)  # 2.44688s
    # bruteForceTest(7)  # 7.68925s
    # bruteForceTest(8)  # 22.42151s
    # bruteForceTest(9)  # 62.11813s

# bruteForceTime()


# Problem 3 Observations
# ======================
# your observations regarding bruteForceTime's performance

# Computation time grows exponentially. When maxWork equals 9, it already takes more than 1 minute to compute the optimal solution.
# recursive strategy



#
# Problem 4: Subject Selection By Dynamic Programming
#

def dp_decision_tree(w, v, i, aW, m):
    """
    Creates a course schedule that is optimized the maximum value.
    :param aW: work hour available
    :param m: memo = {(i,aW):(value,recSubjectNo), }
    """
    try: return m[(i, aW)]
    except KeyError:
        #  Leaf/Bottom of the tree case decision
        if i == 0:
            if w[i] < aW:
                m[(i, aW)] = v[i], [i]
                return v[i], [i]
            else:
                m[(i, aW)] = 0, []
                return 0, []

    # Calculate with and without i branches
    without_i, course_list = dp_decision_tree(w, v, i-1, aW, m)
    if w[i] > aW:
        m[(i, aW)] = without_i, course_list
        return without_i, course_list
    else:
        with_i, course_list_temp = dp_decision_tree(w, v, i-1, aW-w[i], m)
        with_i += v[i]

    # Take the branch with the higher value
    if with_i > without_i:
        i_value = with_i
        course_list = [i] + course_list_temp
    else:
        i_value = without_i

    # Add this value calculation to memo
    m[(i, aW)] = i_value, course_list
    return i_value, course_list


def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    memo = {}
    course_list = list(subjects.keys())
    v_w_list = list(subjects.values())
    value_list = []
    work_list = []
    for i in v_w_list:
        value_list.append(i[0])
        work_list.append(i[1])

    max_val, subject_id_list = dp_decision_tree(work_list, value_list, len(course_list)-1, maxWork, memo)

    outputSubjects = {}
    for i in subject_id_list:
        outputSubjects[course_list[i]] = v_w_list[i]
    return outputSubjects


# printSubjects(dpAdvisor(subjects, 25))
# printSubjects(bruteForceAdvisor(subjects, 25))


# not successful attempt
def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork, memo):
    # memo = {} {(i, subsetWork): subsetValue}
    try: return memo[(i, subsetWork)] #
    except KeyError:
        if i >= len(subjects):
            if bestSubset == None or subsetValue > bestSubsetValue:
                memo[(i, subsetWork)] = subsetValue, []
                # Found a new best.
                return subset[:], subsetValue
            else:
                memo[(i, subsetWork)] = bestSubsetValue, [] # this value?
                return bestSubset, bestSubsetValue
        else:
            s = subjects[i]
            # Try including subjects[i] in the current working subset.
            if subsetWork + s[WORK] <= maxWork:
                memo[(i, subsetWork+s[WORK])] = subsetValue + s[VALUE]
                subset.append(i)
                bestSubset, bestSubsetValue = dpAdvisorHelper(subjects, maxWork, i + 1, bestSubset, bestSubsetValue, subset, subsetValue + s[VALUE], subsetWork + s[WORK], memo)
                subset.pop()
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects, maxWork, i + 1, bestSubset, bestSubsetValue, subset, subsetValue, subsetWork, memo)
            memo[(i, subsetWork)] = subsetValue
            return bestSubset, bestSubsetValue

# print(dpAdvisor(subjects, 15))



#
# Problem 5: Performance Comparison
#

def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    def dpTest(n):
        start = time.time()
        dpAdvisor(subjects, n)
        end = time.time()
        compute_time = round(float(end - start), 3)
        print('Dynamic Programming Algorithm: maxWork = {}, takes {}s to compute.'.format(n, compute_time))

    for i in range(5, 26):
        dpTest(i)

dpTime()



# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

# Dynamic programmign algorithm performance:
  # maxWork = 5, 0.002s
  # maxWork = 25, 0.01s
# near O(N) linear performance

# Compared to the exponential complexity of brute force algorithm, dynamic programming is much more efficient.
# With dpAdvisor(), it's not likely that the program would fail when size of course catalogue or maxWork increases.