max_end = 0
max_so_far = -999
a = map(int,raw_input().split(' '))
for i in a:
	max_end = max_end+i
	if max_so_far < max_end:
		max_so_far = max_end
	if max_end < 0:
		max_end = 0

if max_so_far == 0:
	print max(a)
else:
	print max_so_far
