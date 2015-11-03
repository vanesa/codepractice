from __future__ import division
import sys

"""
HACKERRANK CHALLENGES - PYTHON INTRODUCTION
"""


#####Arithmetic Operators#####

"""

Task 
Read two integers from STDIN and print three lines where: 
(1) the first line contains the sum of the two numbers, 
(2) the second line contains the difference of the two numbers (first - second), 
(3) the third line contains the product of the two numbers.

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Constraints 
1<=a<=1010 
1<=b<=1010

Output Format 
Print three lines as explained above.

Sample Input

3
2
Sample Output

5
1
6
Explanation 
3 plus 2=5 
3 minus 2=1 
3 times 2=6

"""

def hr_arithmetic():
	def calculations(a,b):
	    results = []
	    results.append(a + b)
	    results.append(a - b)
	    results.append(a * b)
	    return results
	    
	a = int(raw_input("Type one integer: "))
	b = int(raw_input("Type one integer: "))
	res = calculations(a,b)
	print res[0]
	print res[1]
	print res[2]


####DIVISION####

"""
Task 
Read two integers and print two lines, such that the first line contains integer division and the second line contains float division.

You don't need to perform any rounding or formatting operation.

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format 
Print two lines as described above.

Sample Input

4
3
sample Output

1
1.3333333333333333
"""

def hr_division():
	#from __future__ import division

	a = int(raw_input("Type one integer: "))
	b = int(raw_input("Type one integer: "))

	print a//b
	print a/b


####Mod Divmod####

"""
Task 
Read two integers, a and b, and print three lines. 
The first line is the integer division a//b (Remember to import division from __future__) 
The second line is the result of a mod b. (Modulo operator) 
In the third line print the divmod of a and b.

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format 
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)

"""

def hr_divmod():
	#from __future__ import division

	a = int(raw_input("Type one integer: "))
	b = int(raw_input("Type one integer: "))

	print a//b
	print a%b
	print divmod(a,b)

####Power - Mod Power####

"""
Task 
You are given three integers; print two lines. 
The first line should print pow(a,b), and the second line should print the result of pow(a,b,m).

Input Format 
The first line contains a, the second line contains b, and the third line contains m.

Constraints 
1=<a=<10 
1=<b=<10 
2=<m=<1000

Sample Input

3
4
5
Sample Output

81
1
"""

def hr_powermod():
	a = int(raw_input())
	b = int(raw_input())
	m = int(raw_input())

	print pow(a,b)
	print pow(a,b,m)


####Integers Come In All Sizes####

"""
Task 
Read four numbers, a, b, c, and d, and print the result of ab+cd.

Input Format 
Four numbers are given on four lines.

Constraints 
1=<a=<1000 
1=<b=<1000 
1=<c=<1000 
1=<d=<1000

Output Format 
Print the result in one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  
Note that this result is bigger than 263-1 and hence won't fit in long long int of C++ or a 64-bit integer.
"""
def hr_allsizes():
	a = int(raw_input())
	b = int(raw_input())
	c = int(raw_input())
	d = int(raw_input())

	print pow(a,b) + pow(c,d)


####LOOPS####
"""
Task 
Read an integer N. For all non-negative integers i<N, print i2. See the sample for details.

Input Format 
The first and only line contains N.

Constraints 
1<=N<=20

Output Format 
Print N lines, one corresponding to each i.

Sample Input

5
Sample Output

0
1
4
9
16
"""
def hr_loops():
	n = int(raw_input("Type one integer: "))
	i = 0
	while i < n:
	    print i**2
	    i += 1


####What's Your Name?####

"""
Problem Statement

Let's learn the basics of Python! You are given the first name and the last name of a person. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
It's that simple!

In Python you can read a line as a string using

s = raw_input()
#here s reads the whole line.  
Input Format The first line contains the first name, and the second line contains the last name.

Constraints 
The length of the first and last name <= 10.

Output Format Print the output as mentioned above.

Sample Input

Guido
Rossum
Sample Output

Hello Guido Rossum! You just delved into python.
Concept The input read by the program is stored as a string data type. A string is a collection of characters.

"""

def hr_name():
	firstname = raw_input("Type your firstname: ")
	lastname = raw_input("Type your lastname: ")

	print "Hello "+firstname, lastname+"! You just delved into python."

###Interchange two numbers###

"""
Problem Statement

You are given two integers. Store them into two variables and exchange them. Can it get any 
easier! Make sure to use a tuple to do the task, rather than using any fancy logic. Print the two numbers.

Input Format

Two integers

Output Format

Two integers

Sample Input

2
1
Sample Output

1
2
"""
def reversenums():
	a = raw_input("Type one integer: ")
	b = raw_input("Type a second integer: ")

	t = b,a

	print t[0]
	print t[1]

####Finding the percentage####

"""
Problem Statement

There is a record of 'n' students, each record having name of student, percent marks obtained in Maths, Physics and Chemistry. Marks can be floating values. The user enters an integer 'n' followed by names and marks for the 'n' students. You are required to save the record in a dictionary data type. The user then enters name of a student and you are required to print the average percentage marks obtained by that student, correct to two decimal places.

Input Format

Integer N followed by name and marks for N students, followed by the name of the particular student.

Output Format

Average percentage of marks obtained

Constraints 
2 <= N <= 10 
0 <= Marks <= 100

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output

56.00
"""

def average_grade():
	student_num = int(raw_input())
	students = {}
	for i in range(student_num):
	    data = raw_input()
	    student = data.split(" ")
	    average = (float(student[1]) + float(student[2]) + float(student[3]))/3
	    students[student[0]] = average
	sel_student = raw_input()
	if sel_student in students:
	    print format(students[sel_student], '.2f')
	else:
	    print sel_student + "is not in the database"


if __name__ == '__main__':
    print dir()