with open('day06.txt', 'r') as f:
	groups = [l.splitlines() for l in f.read().split('\n\n')]
	print('step 1:', sum(len({answer for line in group for answer in line}) for group in groups))
	print('step 2:', sum(len(set.intersection(*[{answer for answer in line} for line in group])) for group in groups))