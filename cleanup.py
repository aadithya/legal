import re
f = open('advocate.txt')
o = open('clean_adv.csv','w')
for line in f:
    a = r'(.*):(.*), Advocate'
    m = re.match(a, line)
    if m:
        o.write("%s, %s \n" % (m.group(1), m.group(2)))
o.close()

