from enum import Enum

class CommandType:
    DEFAULT = 0
    ANNOY = 1
    GREET = 2

COMMAND_LIST = (
    'annoy'
)

class Command:
    def __init__(self, command_type: CommandType, execute: bool, target: str, text: str) -> None:
        self.type = command_type
        self.execute = execute
        self.target = target
        self.text = text

    @staticmethod
    def empty() -> any:
        return Command(
        command_type=CommandType.DEFAULT,
        execute=False, target='', 
        text=''
        )

    @staticmethod
    def greet(who: str) -> any:
        return Command(
        command_type=CommandType.GREET,
        execute=True, target=who, 
        text='wesh'
        )
    
    @staticmethod
    def annoy(target_id: str) ->any:
        return Command(
            CommandType.ANNOY,
            True,
            target_id,
            'thared :man_shrugging:'
        )
