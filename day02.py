import re

with open('day02.txt', 'r') as f:
	res = 0
	count = 0
	count2 = 0
	for l in f.readlines():
		l=l.strip()
		n, l, p = l.split()
		min_n, max_n = n.split('-')
		min_n = int(min_n)
		max_n = int(max_n)
		l = l[:-1]
		count = p.count(l)
		if count >= min_n and count <= max_n:
			res += 1

		correct = 0
		if p[min_n-1] == l:
			correct += 1
		if p[max_n-1] == l:
			correct += 1
		if correct == 1:
			count2 += 1
		count += 1
	print(res)
	print(count)
	print(count2)