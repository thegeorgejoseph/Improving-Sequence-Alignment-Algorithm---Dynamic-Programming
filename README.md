# CSCI 570 Fall '21 : Final Project

Contributers: Amal, George, Srini
Task: Sequence Alignment problem

# Tasks left to do

@Srini:
- Complete Efficient algorithm and test it out (sample test cases in https://piazza.com/class/ksmlgkord5752e?cid=2701)

@Amal:
- Run plotter.py after Srini's code is ready

@Team:
- Finalise on the documentation


Basic Algorithm

The basic or naive implementation of the Sequence Alignment Problem involves the usage of Dynamic Programming. The basic approach involves usage of a matrix of dimension m * n where m and n are the lengths of the strings s1 and s2 respectively.  The runtime complexity of the algorithm is O(mn). The recurrance equation is framed with respective to the paramters like delta and penalty for the different mismatches.


Time Complexity - O(mn)
Space Complexity - O(mn)

Efficient Algorithm

The efficient algorithm makes use of Divide and Conquer Strategy for Sequence Alignment Problem.

We find the minimum cost for the operations to solve the alignment problem. We then make use of the cost to determine the split points for the strings to divide them. In this approach we become aware of the split points and divide the strings appropriately to get 2 subproblems which are repeatedly broken down to smaller subproblems and finally we make use of our basic algorithm to perform the computation.

Time Complexity - O(mn)
Space Complexity - O(2m)

This is one of the most efficient solutions with respective to the space complexity.