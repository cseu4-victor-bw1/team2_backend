from endpoint import contentGeneration
from random import randint
from adventure.models import Room

ROOMS = contentGeneration(100)

class World:
    def __init__(self):
        self.grid = []
    
    def generate_rooms(self):
        grid = [[None] * 10 for _ in range(10)]
        room_count = 0

        for row in range(len(grid)):
            for room in range(len(grid[row])):
                grid[row][room] = Room(title=ROOMS[room_count]['title'], description=ROOMS[room_count]['description'])
                grid[row][room].save()
                room_count += 1

        self.grid = grid

        for y, row in enumerate(self.grid):
            for x, room in enumerate(row):
                directions = ['s', 'e']
                direction = None

                if y-1 == 9 and x-1 == 9:
                    pass
                elif y-1 == 9:
                    direction = 's'
                elif x-1 == 9:
                    direction = 'e'
                else:
                    rand_direction = randint(0, 1)
                    direction = directions[rand_direction]
                if direction == "w":
                    complement = self.grid[y][x - 1]
                    room.connectRooms(complement, direction)
                    complement.connectRooms(room, "e")
                elif direction == "n":
                    complement = self.grid[y - 1][x]
                    room.connectRooms(complement, direction)
                    complement.connectRooms(room, "s")
