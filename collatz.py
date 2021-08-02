# I wrote this program on my own

import sys

# calculate how many steps the Collatz conjecture needs to take to reach 1.
def collatz(n):
	count = 0
	while True:
		if n == 2:		return count + 1
		if (n % 2) == 0:	n = n / 2
		if (n % 2) == 1:	n = (3 * n) + 1
		count += 1
	return count

# find which input gives the greatest output
# we start at 4 because we could get problems if we go below
def collatz_best(n):
	max = n
	out = best = 0
	for i in range(4, max):
		out = collatz(i)
		if out > best:	best = out
	return best

# n is how many increases in the output of collatz_best()
def collatz_count(n):
	x = 4
	old_y = 0
	increases = 0
	while increases < n:
		y = collatz_best(x)
		if old_y != y:	increases += 1
		old_y = y
		x += 1
	return [x, y]


print(collatz_count(int(sys.argv[1])))
  
