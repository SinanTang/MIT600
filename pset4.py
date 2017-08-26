# Problem Set 4

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    retireFund_year = []
    fund = 0
    for i in range(0, years):
        fund = fund * (1 + 0.01 * growthRate)
        fund = fund + salary * save * 0.01
        retireFund_year.append(fund)

    return retireFund_year


def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

# testNestEggFixed()



#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRates: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    ## this doesnt work b/c it's calculating one growth rate for the given length of years
    # years = len(growthRates)
    # for rate in growthRates:
    #     print(nestEggFixed(salary, save, rate, years))

    years = len(growthRates)
    record = []
    fund = 0
    for i in range(0, years):
        fund = fund * (1 + 0.01 * growthRates[i])
        fund = fund + salary * save * 0.01
        record.append(fund)
    return record


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

# testNestEggVariable()



#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    record = []
    for i in range(0, len(growthRates)):
        savings = savings * (1 + 0.01 * growthRates[i]) - expenses
        record.append(savings)

    return record


def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

# testPostRetirement()



#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # 1. calculate total savings
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]

    # 2. binary search for ideal expenses
    low = 0
    high = savings + epsilon
    guess = (low + high) / 2.0
    count = 1
    while abs(high - low) > epsilon and count < 100:
        if postRetirement(savings, postRetireGrowthRates, guess)[-1] < - epsilon:
            high = guess
        else: low = guess

        guess = (low + high) / 2.0
        count += 1

        print(count, guess)

    assert count <= 100, "Iteration count exceeded"
    return guess


def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.

testFindMaxExpenses()