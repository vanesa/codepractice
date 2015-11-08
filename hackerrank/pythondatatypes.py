"""
HACKERRANK CHALLENGES - PYTHON DATA TYPES
"""

#### Lists ######

"""

Task 
You have to initialize your list L = [] and follow the N commands given in N lines.

Commands will be 1 of the 8 commands as given above, other than extend, and each command will have its value separated by space.

Follow this example:

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

import sys

def hr_lists():
    lines = int(raw_input())
    result = []
    commands = ["insert", "remove", "append", "sort", "pop", "reverse"]
    for i in range(lines):
        command = raw_input().split(" ")
        if command[0] == "insert":
            result.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            result.remove(int(command[1]))
        elif command[0] == "append":
            result.append(int(command[1]))
        elif command[0] == "sort":
            result.sort()
        elif command[0] == "pop":
            result.pop()
        elif command[0] == "reverse":
            result.reverse()
        else:
            print result


##### Tuples ###

"""
Task 
You are given an integer N in one line. The next line contains N space-separated integers. Create a tuple of those N integers. Lets call it T. 
Compute hash(T) and print it.

Note hash() is one of the function in __builtins__ module.

Input Format 
The first line contains N. The next line contains N space-separated integer values.

Output Format 
Print the computed value.

Sample Input

2
1 2
Sample Output

3713081631934410656

"""

def hr_tuples1():
    if not lines:
        lines = raw_input()
        nums = raw_input()
    lines = int(lines)
    nums = nums.split(" ")
    tuples = [int(nums[i]) for i in range(lines)]
    t = tuple(tuples)
    print hash(t)

""" Or the short version:
def hr_tuples2(lines, nums):
    lines, nums = int(lines), nums.split(" ")
    print hash(tuple([int(nums[i]) for i in range(lines)]))
"""

#### Sets ####

"""
Problem Statement

Lets learn about a new datatype 'sets'! You are given two set of integers M and N and you have to print their symmetric difference in ascending order. The first line of input contains value of M followed by M integers, then value of N followed by N integers. Symmetric difference between M and N mean those values which either exist in M or in N but not in both.

Input Format

Value of M followed by M integers, then value of N followed by N integers.

Output Format

Integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
"""

def hr_sets():
    m = int(raw_input())
    list1 = map(int, raw_input().split())
    n = int(raw_input())
    list2 = map(int, raw_input().split())
    list1 = set(list1)
    list2 = set(list2)
    diff1 = list1.difference(list2)
    diff2 = list2.difference(list1)
    symmetric_diff = diff1.union(diff2)
    ordered = []
    for i in symmetric_diff:
        ordered.append(i)
    ordered.sort()
    for a in ordered:
        print a

### List Comprehension ####

"""
Problem Statement

Lets learn about list comprehensions!. You are given three integers X, Y and Z denoting the dimensions of a Cuboid. You have to print a list of all possible coordinates on the three dimensional grid, such that at any point the sum Xi + Yi + Zi is not equal to N. If X = 2, then possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

Input Format

Four integers X, Y, Z and N in four different lines.

Output Format

You have to print the list, in increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""

def hr_list_comprehension():
    a, b, c, N = [int(raw_input()) for x in range(4)]
    output = [[x,y,z] for x in range(a+1) for y in range(b+1) for z in range(c+1) if x+y+z!=N]
    print output

if __name__ == '__main__':

    