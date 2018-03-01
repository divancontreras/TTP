class Doggo():
    def __init__(self, first_time, second_time):
        self.first_time = first_time
        self.second_time = second_time
        self.period = second_time + first_time

    def attacked(self, time):
        if time % self.period == 0:
            time = self.period
        else:
            time = time % self.period
        if time > self.first_time and time <= self.period:
            return False
        else:
            return True

try:
    results = {0:"none", 1:"one", 2:"both"}
    times = raw_input()
    workers_times = raw_input()
    workers_times = workers_times.split()
    times = times.split()

    first_doggo = Doggo(int(times[0]), int(times[1]))
    second_doggo = Doggo(int(times[2]), int(times[3]))
    for worker in workers_times:
        attacked_counter = 0
        if first_doggo.attacked(int(worker)):
            attacked_counter += 1
        if second_doggo.attacked(int(worker)):
            attacked_counter += 1
        print(results[attacked_counter])
except EOFError:
    exit