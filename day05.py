def get_idx(is_right, input, l, size):
	if not input:
		return l
	size /= 2
	if is_right(input[0]):
		return get_idx(is_right, input[1:], l + size, size)
	else:
		return get_idx(is_right, input[1:], l, size)

def get_seat(line):
	row = get_idx(lambda v: v=='B', line[:7], 0, 128)
	col = get_idx(lambda v: v=='R', line[7:], 0, 8)
	return (row, col)

def get_seat_idx(seat):
	return int(seat[0]*8+seat[1])

with open('day05.txt', 'r') as f:
	print(max(get_seat_idx(get_seat(l)) for l in f.readlines()))

with open('day05.txt', 'r') as f:
	seats = (get_seat(l) for l in f.readlines())
	seats = [get_seat_idx(i) for i in seats if 0 < i[0] < 128]
	seats.sort()
	for i in range(1, len(seats)):
		if seats[i] - seats[i-1] > 1:
			print('seat:', seats[i] - 1)

