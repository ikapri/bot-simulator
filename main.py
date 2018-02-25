from bot import GroundBot, AirBot
from direction import Direction
from coordinates import Coordinates

origin = Coordinates(0,0,0)
north = Direction.NORTH

bot1 = GroundBot(origin, north)
bot2 = AirBot(origin, north)

bot1.navigate('FFRFFLFFLFRLF')
print 'BOT1--->', bot1.report_position()

bot2.navigate('FFUF')
print 'BOT2--->', bot2.report_position()
