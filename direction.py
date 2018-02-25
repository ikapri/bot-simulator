
class Direction(object):
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'

    @classmethod
    def left(cls, current_direction):
        directions_dict = {cls.NORTH: cls.WEST, cls.SOUTH: cls.EAST, cls.EAST: cls.NORTH, cls.WEST: cls.SOUTH}
        return directions_dict[current_direction]

    @classmethod
    def right(cls, current_direction):
        directions_dict = {cls.NORTH: cls.EAST, cls.SOUTH: cls.WEST, cls.EAST: cls.SOUTH, cls.WEST: cls.NORTH}
        return directions_dict[current_direction]

