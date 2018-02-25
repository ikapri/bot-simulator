from direction import *
from navigator import *
from commands import Commands, CommandParser

STEP_SIZES = {Commands.FORWARD: 1, Commands.UP: 10 , Commands.DOWN: 10}

class Bot(object):
    def __init__(self, starting_point, direction_facing, command_parser=CommandParser, step_sizes_map=STEP_SIZES, default_step_size=1):
        self.current_position = starting_point
        self.current_direction = direction_facing
        self.default_step_size = default_step_size
        self.step_size_map = step_sizes_map
        self.command_parser = CommandParser

    def report_position(self):
        return "Current Position is {position}. Current Direction is {direction}".format(position=self.current_position, direction=self.current_direction)

    def navigate(self, commands):
        for parsed_command in self.parse_commands(commands):
            command_func = parsed_command['func']
            command_kwargs = parsed_command['kwargs']
            self.execute_command(command_func, **command_kwargs)

    def parse_commands(self, commands):
        parsed_commands = []
        for command in commands:
            parsed_commands.append(self.command_parser.parse(command, self))

        return parsed_commands

    def execute_command(self, func, **kwargs):
        func(**kwargs)

    def get_step_size_for_command(self, command):
        return self.step_size_map.get(command, self.default_step_size)

class GroundBot(Bot, Navigator):
    pass

class AirBot(Bot, Navigator, AirNavigator):
    pass

