"""
HACKERRANK CHALLENGES - PYTHON STRINGS
"""

#### Strings ######

"""
Problem Statement

You are given a string S. Your task is to swap case, i.e., convert all lower case letters to upper case and vice versa.

Example :

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

Single line containing, String S.

Constraints 
0<len(S)⩽1000
Output Format

Print the modified string S.

Sample Input

HackerRank.com presents "Pythonist 2".
Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""
def swap_case('HackerRank.com presents "Pythonist 2".'):

	phrase = raw_input()
	swapped = ''
	for x in phrase:
	    if x == x.upper():
	        swapped = swapped + x.lower()
	    else:
	        swapped = swapped + x.upper()
	print swapped

	if __name__ == '__main__':