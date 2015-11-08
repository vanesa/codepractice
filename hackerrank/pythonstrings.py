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


##### String Split and Join #####

"""
Problem Statement

In Python a string can be split on a delimiter.

Example

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task 
You are given a string. Split the string on " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of words separated by space.

Output Format 
Print the formatted string as explained above.

Sample Input

this is a string   
Sample Output

this-is-a-string

"""

def split_join():
	phrase = raw_input("Type in a phrase: ")
	phrase = phrase.split()
	print "-".join(phrase)

	if __name__ == '__main__':
		split_join()