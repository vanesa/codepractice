
import random

def is_palindrome(word):
	"""
	Find if the word is a palindrome!

	>>> is_palindrome("a")
	True

	>>> is_palindrome("ete")
	True

	>>> is_palindrome("marvel")
	False

	>>> is_palindrome("racecar")
	True
	"""
	for i in range(len(word)/2):
		if word[i] != word[len(word)-i-1]:
			return False
	return True


def lucky_numbers(num):
	"""
	Check if random number output is unique:
	>>> lucky_numbers(2)
	True

	>>> lucky_numbers(6)
	True

	>>> lucky_numbers(10)
	True

	>>> lucky_numbers(0)
	True
	"""
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	selection = []

	for i in range(num):
		lucky = random.randrange(0,len(nums))
		selection.append(nums.pop(lucky))

	if len(selection) == num and len(nums) + num == 10:
		return True
	else:
		return False


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "All tests passed!"