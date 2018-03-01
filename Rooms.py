class Group():
    def __init__(self, persons):
        self.persons = persons

    def lil_pop(self):
        self.persons -= 1
        return 1

    def pop(self):
        if self.persons > 1:
            self.persons -= 2
            return 2
        elif self.persons == 0:
            return 0
        else:
            self.persons = 0
            return 1

    def check_pop(self):
        if self.persons > 1:
            return 2
        elif self.persons == 0:
            return 0
        else:
            return 1

    def waiting(self):
        if self.persons > 0:
            return True
        else:
            return False

class Room():
    def __init__(self):
        self.available_beds = 2
        self.guests = 0

    def is_full(self):
        if self.available_beds == 0:
            return True
        else:
            return False

    def occupied(self):
        if self.available_beds < 2:
            return True
        else:
            return False

    def fits(self, number):
        if self.available_beds - number >= 0:
            return True
        else:
            return False

    def insert_guests(self, number):
        self.available_beds -= number
        self.guests += number

class Hotel():
    def __init__(self, rooms_number):
        self.rooms = []
        self.available_rooms = rooms_number
        for x in range(rooms_number):
            self.rooms.append(Room())

    def insert_guests(self, guests):
        if self.available_rooms > 0:
            self.normal_insert(guests)
        else:
            self.softly_insert(guests)

    def normal_insert(self, guests):
        for x in range(len(self.rooms)):
            if guests.waiting() and self.available_rooms > 0:
                if not self.rooms[x].occupied():
                    if self.rooms[x].fits(guests.check_pop()):
                        self.rooms[x].insert_guests(guests.pop())
                        self.available_rooms -= 1
            elif guests.waiting():
                self.softly_insert(guests)
            else:
                return

    def softly_insert(self, guests):
        for x in range(len(self.rooms)):
            if guests.waiting():
                if not self.rooms[x].is_full():
                    self.rooms[x].insert_guests(guests.lil_pop())
            else:
                return
try:
    entry = raw_input().split()
    rooms = int(entry[0])
    groups = int(entry[1])
    if rooms == 0 or groups == 0:
        exit()
    my_hotel = Hotel(rooms)
    for x in range(groups):
        guests = int(raw_input())
        my_hotel.insert_guests(Group(guests))
    for x in range(len(my_hotel.rooms)):
        print(my_hotel.rooms[x].guests)
    exit()
except EOFError:
    exit()