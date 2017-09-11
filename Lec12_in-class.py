### Debugging, Knapsack Problem, Introduction to Dynamic programming

## 1. Optimization Problems
    # - a func to maximize/minimize
    # - a set of constraints

  # Classic Optimization Problems:
    # shortest path algorithm

    # Traveling sales person person (TSP)

    # bin packing

    # sequence alignment problems

    # knapsack problem *

  # problem reduction -> map new problems to old problems


## 2.1 Continuous knapsack problem
    # 4 lbs Au dust, 3 lbs Ag dust, 10 lbs Raisins
    # the problem - function:
        # - max()
        # constraint: 8 lbs in total
    # greedy algorithm: at each step, maximise your value
        # e.g. the word game
            # hand: d o g s l e t -> doges vs dogs + let
        # locally potimal decisions do not always lead to a global optimums
        # but easy to implement and fast to run

## 2.2 The zero-one (0/1) knapsack problem
    # n items, each has a weight and a value

    # the greedy thief: -> the greedy algorithm

    # a slow thief: try all possible combinations of objects then make a decision -> brute force exhaustive emuneration
        # max(Price-i * X-i), X: vector of 0/1
        # max(W-i * X-i) <= C

        # V1 = (0,0,0,0,0,0,0,0) ~ 2^n, exponential
        # exponential is not a good in general

    # the smart thief: Dynamic Programming
        # overlapping sub-problems, eg. recursive implementation of fibonacci numbers
        # optimal substructure

def fib(n):
    global numCalls
    numCalls += 1
    print('fib called with', n)
    # called fib() with the same arguments a few times -> overlapping sub-problems
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

numCalls = 0
# print(fib(5))

n = 10
# print('fib of', n, '=', fib(n), '. numCalls =', numCalls)

# exponential growth...

def fib1(n):
    global memo
    global numCalls
    numCalls += 1
    if not n in memo:
        memo[n] = fib1(n-1) + fib1(n-2)
    return memo[n]

memo = {0:0, 1:1}

print(fib1(10), '. numCalls =', numCalls)
# linear 