import re

# text = open("sun.txt").read()

# text = "25/6/15 3:13:51 pm: Shyam Sundar: Heyy sorry for the late reply!"
count = 0
with open("sun.txt") as text:
	for line in text:
		count = count + 1	
	print 'Total conversations: %d' % count
	text.seek(0)
	input_text = text.read()
	match = re.findall('Shyam Sundar', input_text)
	print 'Shyam initiations: %d' % len(match)
	match = re.findall('Sunethra Sukumar', input_text)
	print 'Sunethra initiations: %d' % len(match)
	text.seek(0)
	dict = {}
	for line in text:
		match = re.search(r"(\d+)\/(\d+)\/(\d+)", line)
		if match:
			print match.groups(0)
			print match.group(1)
			print match.group(2)
			print match.group(3)
		if match:
			key = match.group(3) + '/' + match.group(2) + '/' + match.group(1)
			# print match.group(0)
			if key in dict:
				dict[key] = dict[key] + 1
			else:
				dict[key] = 1;
	from pprint import pprint
	pprint(dict)

	# import datetime

	# mydate = datetime.date(1990, 10, 27)  #year, month, day
	# print mydate.strftime("%d-%m-%Y")