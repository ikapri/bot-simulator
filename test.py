import unittest
from direction import Direction
from coordinates import Coordinates
from bot import GroundBot, AirBot
from commands import Commands

class DirectionTest(unittest.TestCase):
    def test_rotations(self):
        west = Direction.WEST
        north = Direction.NORTH
        east = Direction.EAST
        south = Direction.SOUTH

        self.assertTrue(Direction.right(west) == Direction.NORTH)
        self.assertTrue(Direction.left(north) == Direction.WEST)
        self.assertTrue(Direction.left(west) == Direction.SOUTH)
        self.assertTrue(Direction.right(north) == Direction.EAST)

        self.assertTrue(Direction.right(east) == Direction.SOUTH)
        self.assertTrue(Direction.left(south) == Direction.EAST)
        self.assertTrue(Direction.left(east) == Direction.NORTH)
        self.assertTrue(Direction.right(south) == Direction.WEST)

class BotMovemenTest(unittest.TestCase):
    def test_movements(self):
        origin = Coordinates(0,0,0)
        north = Direction.NORTH
        bot = GroundBot(origin, north)

        step_size_map = {Commands.FORWARD: 5}
        bot1 = GroundBot(origin, north, step_sizes_map=step_size_map)

        bot.navigate('FFR')
        self.assertTrue(bot.current_position == Coordinates(0,2,0))
        self.assertTrue(bot.current_direction == Direction.EAST)

        bot1.navigate('FFR')
        self.assertTrue(bot1.current_position == Coordinates(0,10,0))
        self.assertTrue(bot1.current_direction == Direction.EAST)
        
if __name__ == '__main__':
    unittest.main()
