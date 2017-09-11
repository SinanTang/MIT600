( the ambiguity of problem statements )



### Lec11: Testing & debugging

- **Validation**: a process designed to <u>uncover problems</u> and <u>increase (warranted) confidence</u>.
  - a combination of 2 things: **testing** and **reasoning**



- **Debugging**: Process of ascertaining <u>why</u> the program is not working.
  - Function: 
  - Performance: why so slow? sometime takes more than half of the time



- **Defensive programming**: program so to facilitate validation and debugging
  - assert statement
  - write specifications to assist debugging
  - Modularize 



- **Testing vs debugging**
  - Testing: examine the input/output pair against the specifications
  - Debugging: study the events that led to an error



- **Unit Testing**:
  - Functions, classes
- **Integration testing**:
  - overall program 
  - dont just rush to this step



- **What is the <u>challenge</u> of testing?**
  - never feasible to do exhaustive testing
  - so we need to do a **Test suite**:
    - small enough
    - Large enough to boost confidence



- **Debugging**:
  - leared skill
  - the "epiphany"
  - transferable skill
  - Myth 1: bugs crawl into programs
  - Myth 2: bugs breed
  - **Goal**: Not to eliminate one bug, but to move towards a <u>bug-free program</u>
  - **2 best debugging tools**: 
    - print statement
    - <u>Reading</u> (your code)
  - Be **systematic** when debugging (the differentiator)
    - to reduce the search space
    - to localise source of problem



- **How to be systematic at debugging**
  - study the program text
  - Ask: how could it have produced <u>this</u> result? 
  - Ask: is it part of a family? -> is this a systematic mistake?
    - e.g. aliasing 
  - How to fix it? 



- **the Scientific method:**
  - study the available data
    - Test results
    - program text (you dont understand it as you still have bugs)
  - form hypothesis
  - design & run <u>repeatable</u> experiments 
    - potential to refute the hypothesis
    - have useful intemediate results
    - Expected result (what do you expect your program to do?)
    - find the simplest input 
    - find where the problem is -> binary search
      - e.g. print intermediate results



​	Code Example

```python
def silly():
	res = []
 	done = False
	while not done:
		elem = raw_input('Enter element. Return when done. ')
		if elem == '':
			done = True
		else:
			res.append(elem)
    
    # debugging step 1
    print "res should be [1, 'a', 2]:", res
    
	tmp = res # -> this is making an aliase of the list, 
    # tmp = res[:] # should be cloning, instead of aliasing
    
    # debugging step 3
    print "tmp", tmp, "res", res
    
	tmp.reverse()  # <- here is the bug!
    
    # debugging step 4
    print "tmp", tmp, "res", res
    
	isPal = (res == tmp)
    
    # debugging step 2, compare expectation vs result
    print "tmp", tmp, "res", res
    
	if isPal:
		print 'is a palindrome'
	else:
		print 'is NOT a palindrome' 
```

​	bug: list aliasing - tmp & res refer to the same object



...and **PATIENCE**



More from Lec12...

Where / How to look for **bugs**:
    1. reversed order of arguments (in function call)
    2. spelling
    3. initialisation
    4. object vs value quality, e.g. '=='
    5. aliasing (2 different ways to refer to the same object/value)
      - deep vs shallow copys, e.g. copying lists of lists (mutable)
    6. side effects, e.g. parameters changed during function call
    
    7. Keep a personal list of bugs you make...

    8. keep record of what you tried
    9. reconsidering your assumptions
    
    10. when debugging others code: debug code, not comments
    11. seek help - explain the program
    12. walk away

when find the bug, what to do:
    1. Haste makes waste..
    2. code should not always grow
    3. tidy up
    4. make sure that you can revert - save old versions
    
