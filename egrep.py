import sys, re

regex = sys.argv[1]

# for every line passed into that script
for line in sys.stdin:
	# write it to stdout if it matches the reg
	if re.search(regex, line):
		sys.stdout.write(line)