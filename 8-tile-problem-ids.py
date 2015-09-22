# Assignment 1
# 9 tile problem using Iterative Depening Search.
# Online Compiler: www.codeskulptor.org. Uncomment line 6 & 7.

import random
# import codeskulptor
# codeskulptor.set_timeout(100)

# Checks if the state is solvable or not. It's not necessary for an state to be solvable.
# Returns True or False for solvable or non-solvable respectively.
def isSolvable(state):
    state.remove('B')
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                count += 1
    if count % 2 == 0:
        return True
    else:
        return False

# Generate a random initial state
# Returns the generated state
def generateInitialState():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 'B']
    random.shuffle(x)
    while isSolvable(list(x)) == False:
        random.shuffle(x)
    x = [x[i:i+3] for i in xrange(0, 9, 3)]
    x.append([])
    return x

# Compares current state and goal state. 'y' represents goal state.
# Returns True or False for equal or not equal.
def compareStates(x, y):
    if x[0:3] == y:
        return True
    else:
        return False

# Determines index of 'B' in the state
# Returns index in the [i, j] format
def posB(x):
    for p in x:
        if 'B' in p:
            j = p.index('B')
            i = x.index(p)
            return [i, j]

# Sum of indices in [i, j] format
# Returns sum in [i, j] format
def sumIndex(x, y):
    p = [-1, -1]
    p[0] = x[0] + y[0]
    p[1] = x[1] + y[1]
    return p

# Generate a child from the given state 'x' by moving the 'B' as per stated in 'step'
# Returns the child state
def generateChild(x, step):
    dictStep = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    addIndex = dictStep.get(step)
    posOld = posB(x)
    posNew = sumIndex(posOld, addIndex)
    y = [list(p) for p in x]
    temp = y[posNew[0]][posNew[1]]
    y[posNew[0]][posNew[1]] = y[posOld[0]][posOld[1]]
    y[posOld[0]][posOld[1]] = temp
    y[3].append(step)
    return y

# Checks if taking given 'step' is possible or not
# Returns True or False
def stepPossible(x, step):
    dictStep = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    addIndex = dictStep.get(step)
    posOld = posB(x)
    posNew = sumIndex(posOld, addIndex)
    if (posNew[0] > 2) or (posNew[0] < 0) or (posNew[1] > 2) or (posNew[1] < 0):
        return False
    else:
        return True

# Acts as main method which checks for the goal node within given 'depth'
# Returns True or False for the goal node found in 'depth' or not.
def findGoal(currentState, depth):
    global achievedGoalNode
    if depth == 0:
        if compareStates(currentState, goalState) == True:
            achievedGoalNode = currentState
            return True
        else:
            return False
    else:
        for step in STEPS:
            if stepPossible(currentState, step):
                childNode = generateChild(currentState, step)
                if findGoal(childNode, depth - 1) == True:
                    for i in range(len(currentState) - 1):
                        print currentState[i]
                    print
                    return True
        return False




goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]
STEPS = ['U', 'R', 'D', 'L']
achievedGoalNode = []
randomInitialState = [[1, 'B', 3], [4, 2, 5], [7, 8, 6], []]
# randomInitialState = [[8, 1, 4], [3, 6, 2], ['B', 5, 7], []]
# Uncomment below statement and comment the above one.
# randomInitialState = generateInitialState()
print 'Initial State:'
for i in range(len(randomInitialState) - 1):
    print randomInitialState[i]
print


found = False
depth = 0
while(not found):
    print 'Current Working Depth:', depth
    if findGoal(randomInitialState, depth) == True:
        found = True
        print '***** Goal Achieved at depth', depth
        print 'Path Taken:', achievedGoalNode[3]
    else:
        depth += 1
