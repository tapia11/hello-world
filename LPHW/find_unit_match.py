def find_matches(list1, list2):
	matches = []
	for item in list1:
		if item in list2:
			matches.append(item)
			return matches

f = open('converged_list.txt', 'r+')
p = open('pkv_no_services.txt', 'r+')
c = open('clt_no_services.txt', 'r+')

comparing_read = f.readlines()
comparing_pkv = p.readlines()
comparing_clt = c.readlines()

match1 = find_matches(comparing_read, comparing_pkv)
if match1 is None:
	print "No matches found for file 1"
else:
	print match1

match2 = find_matches(comparing_read, comparing_clt)
if match2 is None:
	print "No matches found for file 2"
else:
	print match2


f.close()
c.close()
p.close()