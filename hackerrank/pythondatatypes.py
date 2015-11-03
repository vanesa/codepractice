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

def hr_tuples1(lines, nums):
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



if __name__ == '__main__':
    hr_tuples1(2, '1 2')