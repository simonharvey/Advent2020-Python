import functools
with open('day03.txt', 'r') as f:
	grid = [l.strip() for l in f.readlines()]
	
	def count_hits(tx, ty):
		x, y = 0, 0
		hits = 0
		while y < len(grid):
			if grid[y][x] == '#':
				hits += 1
			x = (x + tx) % len(grid[0])
			y += ty
		return hits
	
	print(count_hits(3, 1))
	slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
	print(functools.reduce(lambda a, b: a * b, (count_hits(*a) for a in slopes)))