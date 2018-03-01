import math
entry = int(raw_input())
results = []
for x in range(entry):
    persons = int(raw_input())
    results.append((math.factorial(persons)))
for x, val in enumerate(results):
    print "Case #"+str(x+1)+":",results[x]
