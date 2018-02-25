class Commands(object):
    RIGHT = 'R'
    LEFT = 'L'
    FORWARD = 'F'
    UP = 'U'
    DOWN = 'D'

class CommandParser(object):
    COMMAND_FUNC_MAP = {Commands.RIGHT: 'turn_right',
                        Commands.LEFT: 'turn_left',
                        Commands.FORWARD: 'move_forward',
                        Commands.UP: 'move_up',
                        Commands.DOWN: 'move_down'
                        }

    MOVEMENT_COMMANDS = [Commands.FORWARD, Commands.UP, Commands.DOWN]

    @classmethod
    def parse(cls, command_string, bot):
        func_name = cls.COMMAND_FUNC_MAP[command_string.upper()]
        func = getattr(bot, func_name, None)
        if not func:
            raise Exception("Invalid Command {} for bot {}".format(command_string, type(bot)))
        func_kwargs = {}

        if command_string in cls.MOVEMENT_COMMANDS:
            step_size = bot.get_step_size_for_command(command_string)
            func_kwargs['step_size'] = step_size

        return {"func": func, "kwargs": func_kwargs}



