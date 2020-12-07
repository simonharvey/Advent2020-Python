import re

def height_validator(val):
	if len(val) < 3: return False
	units = val[-2:]
	val = int(val[:-2])
	if units == 'in': return 59 <= val <= 76
	elif units == 'cm': return 150 <= val <= 193
	return False

fields = {
	'byr':lambda v: 1920 <= int(v) <= 2002,
	'iyr':lambda v: 2010 <= int(v) <= 2020,
	'eyr':lambda v: 2020 <= int(v) <= 2030,
	'hgt':height_validator,
	'hcl':lambda v: re.match(r'#[0-9 a-f]{6}$', v),
	'ecl':lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
	'pid':lambda v: re.match(r'[0-9]{9}$', v),
	#'cid',
}

def get_entries(lines):
	d = {}
	for l in lines:
		l = l.strip()
		if not l:
			yield d
			d = {}
		else:
			for e in l.split():
				k, v = e.split(':')
				d[k] = v
	yield d

#first part
with open('day04.txt', 'r') as f:
	res = 0
	for e in get_entries(f.readlines()):
		if all(k in e for (k, v) in fields.items()):
			res += 1
	print(res)

def check_entry(e):
	for (k, v) in fields.items():
		if not (k in e): print('no key for %s' % k); return False
		if not v(e[k]): print('cant validate %s : %s' % (k, e[k]));	return False
	return True

#second part
with open('day04.txt', 'r') as f:
	res = 0
	for e in get_entries(f.readlines()):
		if check_entry(e):
			res += 1
	print(res)