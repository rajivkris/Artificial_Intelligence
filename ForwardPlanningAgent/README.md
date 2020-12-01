
## Introduction
Planning is an important topic in AI because intelligent agents are expected to automatically plan their own actions in uncertain domains. Planning and scheduling systems are commonly used in automation and logistics operations, robotics and self-driving cars, and for aerospace applications like the Hubble telescope and NASA Mars rovers.

This project is split between implementation and analysis. First you will combine symbolic logic and classical search to implement an agent that performs progression search to solve planning problems. Then you will experiment with different search algorithms and heuristics, and use the results to answer questions about designing planning systems.

Read all of the instructions below and the project rubric [here](https://review.udacity.com/#!/rubrics/1800/view) carefully before starting the project so that you understand the requirements for successfully completing the project. Understanding the project requirements will help you avoid repeating parts of the experiment, some of which can have long runtimes.

**NOTE:** You should read "Artificial Intelligence: A Modern Approach" 3rd edition chapter 10 *or* 2nd edition Chapter 11 on Planning, available [on the AIMA book site](http://aima.cs.berkeley.edu/2nd-ed/newchap11.pdf) before starting this project.

See the [Project Enhancements](#optional-project-enhancements) section at the end for additional notes about limitations of the code in this exercise.

![Progression air cargo search](images/Progression.PNG)

## Getting Started (Local Environment)
If you would prefer to complete the exercise in your own local environment, then follow the steps below:

**NOTE:** You are _strongly_ encouraged to install pypy 3.5 (download [here](http://pypy.org/download.html)) for this project. Pypy is an alternative to the standard cPython runtime that tries to optimize and selectively compile your code for improved speed, and it can run 2-10x faster for this project. There are binaries available for Linux, Windows, and OS X. Simply download and run the appropriate pypy binary installer (make sure you get version 3.5) or use the package manager for your OS. When properly installed, any `python` commands can be run with `pypy` instead. (You may need to specify `pypy3` on some OSes.)

## Instructions

1. Start by running the example problem (this example implements the "have cake" problem from Fig 10.7 of AIMA 3rd edition). The script will print information about the problem domain and solve it with several different search algorithms, however these algorithms cannot solve larger, more complex problems so next you'll have to implement a few more sophisticated heuristics.
```
$ python example_have_cake.py
```

2. Open `my_planning_graph.py` 

Building a Forward-Planning Agent
Part of Udacity's Artificial Intelligence Nanodegree.

Planning is an important topic in AI because intelligent agents are expected to automatically plan their own actions in uncertain domains. Planning and scheduling systems are commonly used in automation and logistics operations, robotics and self-driving cars, and for aerospace applications like the Hubble telescope and NASA Mars rovers.

This project is split between implementation and analysis. First I combined symbolic logic and classical search to implement an agent that performs progression search to solve planning problems. Then I experimented with different search algorithms and heuristics, and used the results to answer questions about designing planning systems.

Inconsistent Effects
Return True if an effect of one action negates an effect of the other

def _inconsistent_effects(self, actionA, actionB):

    for effectA in actionA.effects:
        
        for effectB in actionB.effects:
            
            if effectA == ~effectB:
                return True
Interference
Return True if the effects of either action negate the preconditions of the other

def _interference(self, actionA, actionB):
    
    for effect in actionA.effects:
        
        for precondition in actionB.preconditions:
            
            if precondition == ~effect:
                return True
Competing Needs
Return True if the preconditions of the actions are all pairwise mutex in the parent layer

def _competing_needs(self, actionA, actionB):
    
    for preconditionA in actionA.preconditions:

        for preconditionB in actionB.preconditions:

            if self.parent_layer.is_mutex(preconditionA, preconditionB):
                return True
Inconsistent Support
Return True if all ways to achieve both literals are pairwise mutex in the parent layer

def _inconsistent_support(self, literalA, literalB):
    
    for actionA in self.parents[literalA]:

        for actionB in self.parents[literalB]:

            if not self.parent_layer.is_mutex(actionA, actionB):
                return False

    return True
Negation
Return True if two literals are negations of each other.

def _negation(self, literalA, literalB):
    
    if literalA == ~literalB and literalB == ~literalA:
        return True
Heuristics
Level Sum
Calculate the level sum heuristic for the planning graph

The level sum is the sum of the level costs of all the goal literals combined. The "level cost" to achieve any single goal literal is the level at which the literal first appears in the planning graph. Note that the level cost is NOT the minimum number of actions to achieve a single goal literal.

For example, if Goal1 first appears in level 0 of the graph (i.e., it is satisfied at the root of the planning graph) and Goal2 first appears in level 3, then the levelsum is 0 + 3 = 3.

def h_levelsum(self):

    graph = self.fill()

    levelsum = 0

    for goal in self.goal:
        levelsum = levelsum + self.levelcost(graph, goal)

    return levelsum
Max Level
Calculate the max level heuristic for the planning graph

The max level is the largest level cost of any single goal fluent. The "level cost" to achieve any single goal literal is the level at which the literal first appears in the planning graph. Note that the level cost is NOT the minimum number of actions to achieve a single goal literal.

For example, if Goal1 first appears in level 1 of the graph and Goal2 first appears in level 3, then the levelsum is max(1, 3) = 3.

def h_maxlevel(self):

    graph = self.fill()

    costs = []

    for goal in self.goal:
        costs.append(self.levelcost(graph, goal))

    return max(costs)
Set Level
Calculate the set level heuristic for the planning graph

The set level of a planning graph is the first level where all goals appear such that no pair of goal literals are mutex in the last layer of the planning graph.

def h_setlevel(self):

    while not self._is_leveled:
        
        layer = self.literal_layers[-1]

        if self.goal.issubset(layer):
            
            no_pairmutex = True

            for goal1 in self.goal:
                for goal2 in self.goal:
                    if layer.is_mutex(goal1, goal2):
                        no_pairmutex = False
                        break

            if no_pairmutex:
                return len(self.literal_layers) - 1

        self._extend()

    return len(self.literal_layers) - 1  
