def visited_collision(visited, node):
    for x in visited.split():
        if list[int(x)][0].collision_exist(list[node][0].start_time, list[node][0].duration):
           return True
    return False

def collision_exist(self_start, self_duration, other_start, other_duration):
    other_final = other_start + other_duration
    self_final = self_start + self_duration
    if ((other_start > self_start and other_start < self_final) or
            (other_final > self_start and other_final < self_final) or
            (other_start < self_start and other_final > self_final) or
            (other_start == self_start) or other_final == self_final):
        return True
    else:
        return False

def sum_them_all(initial_price, set):
    sum = initial_price
    visited = ""
    for node in set:
        if not visited_collision(visited, node):
            visited += str(node) + " "
            sum += list[node][0].price
    return sum


cases = int(raw_input())
for x in range(cases):
    list = []
    orders = int(raw_input())
    for y in range(int(orders)):
        entry = str(raw_input()).split()
        start_time = int(entry[0])
        duration = int(entry[1])
        price = int(entry[2])
        aux = [[start_time, duration, price],[]]
        for x, item in enumerate(list):
            if not collision_exist(aux[0][0], aux[0][1], item[0][0], item[0][1]):
                item[1].append(y)
                aux[1].append(x)
        list.append(aux)
    results = []
    for item in list:
            results.append(sum_them_all(item[0][2], item[1]))
    print("e")
    print max(results)