# You are given a function 'secret()' that accepts a single integer parameter and returns an integer. 
# In your favorite programming language, write a command-line program that takes one command-line argument (a number) 
# and determines if the secret() function is additive [secret(x+y) = secret(x) + secret(y)], for all combinations x and y, 
# where x and y are all prime numbers less than the number passed via the command-line argument.  

# Describe how to run your examples. Please generate the list of primes without using built-in functionality.

import time
import sys

idx = 0

def is_prime(n):

    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def get_primes_less_than(integer):
	# return a list of primes less than the integer
	prime_list = []

	# # no primes less than 2
	if integer <= 2:
		return prime_list

	for i in range(2,integer):
		# if prime then add to list
		if is_prime(i):
			prime_list.append(i)

	# print(prime_list)

	return prime_list

def secret(integer):
	return integer

# test not additive function

# def secret(integer):
# 	return integer**3

# progress animation for a large prime list 
def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('Processing [%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush() 


def is_secret_additive(integer):

	prime_list = get_primes_less_than(integer)

	# for progress animation
	count = 0
	length = len(prime_list)
	total = length * (length + 1)

	for i in prime_list:
		for j in prime_list:

			# ignore if both numbers are the same
			if i == j:
				continue

			count += 1
			progress(count,total)
			
			# https://en.wikipedia.org/wiki/Additive_function
			if secret(i + j) != secret(i) + secret(j):
				return False

	return True

def main():
	
	run = True

	while run:
		# get user input
		user_input = input("\nPlease input an integer (Enter Q to quit): ")

		# quit program
		if user_input.upper() == 'Q':
			run = False
			print("\nGoodbye!\n")
		else:

			# check if is a number
			try:
				# handle fractional
				number = int(user_input)

				additive = is_secret_additive(number)

				# overwrite progress bar
				print("                                                                                              ")

				if additive:
					print("\rFunction is additive!")
				else:
					print("\rFunction is NOT additive!")

			except ValueError:
				print("Please enter a number!")

	
main()