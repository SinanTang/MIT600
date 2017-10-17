### Lec24. Course Overview; What do Computer Scientist do? ###

"""
Think Computationally

Computaional Thinking: the process
  - identify or invent useful abstractions
  - formulate solution to a problem as a computational experiment
  - design and construct a sufficiently efficient implementation of experiment
  - validate experimental setup
  - run experiment
  - evaluate results of experiment
  - repeat as needed

The two A's of Computational Thinking
 - Abstraction
   - choosing the right abstractions
   - operating in terms of multiple layers of abstraction simultaneously
   - defining the relationships between layers
 - Automation
   - think in terms of mechanizing our abstractions
   - mechanization is possible
     - b/c we have precise and exacting notations and models
     - there is some 'machine' below (human or computer, virtual or physical)

Examples of computational thinking
  - How difficult is this problem and how best can I solve it?
     - theoretical computer science gives precise meaning to these and related questions and their answers
  - Thinking recursively
    - reformulating a seemingly difficult problem into one which we know how to solve
    - reduction, embedding, transformation, simulation
  - choosing an appropriate representation or modelling the relevant aspects of a problem
    to make it tractable
  - precention, detection and recovery from worst-case scenarioa through redundancy,
    damage containment. and error correction
  - Using the difficulty of solving hard problems to foil would be evil doers


5 major topics:
1. Writing, Testing and Debugging Programs
  - Take it a step at time
    - understand the problem
    - think about overall structure and algorithms independently of expression in programming language
    - break into small parts
    - identify useful abstractions (data and functional)
    - code and unit test a part at a time
    - first functionality, then efficiency
    - start with pseudo code
  - Be systematic
    - when debugging, think scientific method
    - ask yourself why program did what it did, not why it didn't fo what you wanted it to do

2. From Problem Statement to Computation
  - break the problem into a series of smaller problems
  - try and relate problem to a problem you or somebpdy else have already solved
  - think about what kind of output you might like to see, e.g. what plots
  - formulate as an optimization problem
    - find the min/max vales satisfying some set of constriants
  - think about how to approximate solutions
    - solve a simpler problem
    - find a series of solutions that approaches (but may never reach) a perfect answer

3. algorithms
  - Big O notation
    - orders of growth: exponential, polynomial, linear, log
    - amortised analysis
  - Kinds of algorithms
    - exhaustive enumeration, guess and check, successive approximation, greedy algorithms
      divide and conquer, decision tree, dynamic programming
  - Specific algorithms
    - e.g. binary search, merge sort
  - optimization problems
    - knapsack problems

4. Simulations
  - an excuse (and framework) to learn about probability and statistics
  - an excuse to build interesting programs
  - the power of random choice
    - much of the world is or appears to be stochastic
    - can be used to solve problems that are not inherently random, e.g. calculating pi
  - assessing the quality of an answer
    - not always obvious
  - building models of parts of the world

5. Pervasive themes:
  - Power of abstraction
  - systematic problem solving

"""