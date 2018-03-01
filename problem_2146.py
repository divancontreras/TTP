entry = raw_input().split()
vertex = int(entry[1])
if ((vertex*(vertex-3))/2) == int(entry[0]):
    print "yes"
else:
    print "no"