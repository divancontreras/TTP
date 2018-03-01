class Order():
    def __init__(self, start_time, duration, price):
        self.start_time = start_time
        self.duration = duration
        self.final_time = start_time + duration
        self.price = price

    def collision_exist(self, other_start, other_duration):
        other_final = other_start + other_duration
        if ((other_start > self.start_time and other_start < self.final_time) or
                (other_final > self.start_time and other_final < self.final_time) or
                (other_start < self.start_time and other_final > self.final_time) or
                (other_start == self.start_time) or other_final == self.final_time):
            return True
        else:
            return False


def visited_collision(visited, node):
    for x in visited.split():
        if list[int(x)][0].collision_exist(list[node][0].start_time, list[node][0].duration):
           return True
    return False

def find_largest_sum(start,allowed, sum= 0, visited=""):
        visited += str(start)+" "
        sum = sum + list[start][0].price
        largest = sum
        for node in list[start][1]:
            if (str(node) not in visited.split() and not visited_collision(visited, node) and node in allowed):
                new_sum = find_largest_sum(node,allowed, sum, visited)
                if new_sum > largest:
                    largest = new_sum
        return largest
#
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
    list = {}
    orders = int(raw_input())
    for y in range(int(orders)):
        entry = str(raw_input()).split()
        start_time = int(entry[0])
        duration = int(entry[1])
        price = int(entry[2])
        aux = [Order(start_time, duration, price),[]]
        for key in list:
            if not list[key][0].collision_exist(start_time, duration):
                aux[1].append(key)
        list[y] = aux
    results = []
    for key in list:
            # results.append(sum_them_all(list[key][0].price, list[key][1]))
            results.append(find_largest_sum(key, list[key][1]))
    print max(results)
