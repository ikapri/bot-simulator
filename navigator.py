import operator
from direction import Direction
from coordinates import Coordinates


class Navigator(object):
    """
    Interface for Navigation.
    """
    DIRECTION_MOVEMENT_MAP = {
                        Direction.NORTH: {"index": 1, "operation": operator.add},
                        Direction.SOUTH: {"index": 1, "operation": operator.sub},
                        Direction.EAST: {"index": 0, "operation": operator.add},
                        Direction.WEST: {"index": 0, "operation": operator.sub}
                   }

    def move_forward(self, step_size):
        movement_map = self.DIRECTION_MOVEMENT_MAP[self.current_direction]
        point1 = [0, 0, 0]
        index = movement_map['index']
        point1[index] = step_size
        coordinates1 = Coordinates(*point1)
        operation = movement_map['operation']

        self.current_position = operation(self.current_position, coordinates1)

    def turn_left(self):
        self.current_direction = Direction.left(self.current_direction)

    def turn_right(self):
        self.current_direction = Direction.right(self.current_direction)


class AirNavigator(object):
    """
    Interface for Air Navigation.
    """
    def move_up(self, step_size):
        current_position = self.current_position
        new_z_coordinates = current_position.z + step_size
        self.current_position = Coordinates(current_position.x, current_position.y, new_z_coordinates)

    def move_down(self, step_size):
        current_position = self.current_position
        new_z_coordinates = current_position.z - step_size
        self.current_position = Coordinates(current_position.x, current_position.y, new_z_coordinates)

