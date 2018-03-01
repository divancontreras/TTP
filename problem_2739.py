import math

class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        result_x = other.x - self.x
        result_y = other.y - self.y
        return math.sqrt(math.pow(result_x, 2) + math.pow(result_y, 2))

def get_path_distance(path):
    sum_distance = 0
    for x in range(len(path)-1):
        sum_distance += points[x].get_distance(points[x+1])
    return sum_distance

def find_shortest_path(start, end, sum_distance,visited):
    visited += str(start) + " "
    sum_distance += points[start].get_distance(points[x + 1])
    if start
    for node in points[start]:
        if node not in points:
            newpath = find_shortest_path( node, end, path)
            if newpath < shortest:
                shortest = newpath
    return shortest

points = {}
signaling = int(raw_input())
for x in range(signaling):
    point = str(raw_input()).split()
    points[int(point[0])] = Coordinates(float(point[1]), float(point[2]))
target_points = str(raw_input()).split()
distance = str(points[int(target_points[0])].get_distance(points[int(target_points[1])]))
print(distance[:distance.find(".")+3])
