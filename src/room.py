class Room:

    def __init__(self, name, capacity, till, genre):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.genre = genre
        self.room = []
        self.playlist = []
        self.vibe = 0
        
    def open_room(self, room):
        return self.room.append(room)