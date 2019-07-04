import itertools
import sys


def primes():
	for possiblePrime in range(2, sys.maxsize**10):

		isPrime = True
		for num in range(2, int(possiblePrime ** 0.5) + 1):
			if possiblePrime % num == 0:
				isPrime = False
				break

		if isPrime:
			yield possiblePrime


print(list(itertools.takewhile(lambda x: x <= 61, primes())))
