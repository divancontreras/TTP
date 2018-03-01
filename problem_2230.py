import itertools
class Vector:
    def __init__(self, values):
        self.vector = values
        self.length = len(values)

    def __add__(self, other):
        lowest = True
        for z in list(itertools.permutations(self.vector)):
            aux = 0
            for x in range(len(z)):
                aux += int(z[x]) * int(other.vector[x])
            if lowest == True or aux < lowest:
                lowest = aux
        return lowest


def get_lowest(a, b):
    lowest = []
    lowest.append(a + b)
    lowest.append(b + a)
    return lowest[0]



raw_input()
vector_a = Vector(raw_input().split())
vector_b = Vector(raw_input().split())
print(get_lowest(vector_a, vector_b))