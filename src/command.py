from enum import Enum

class CommandType:
    DEFAULT = 0
    ANNOY = 1
    GREET = 2
    LOCK = 3
    UNLOCK = 4
    STOP = 5
    NEUTRAL = 6

    @staticmethod
    def to_str(cmd_type) -> str:
        if cmd_type == CommandType.DEFAULT:
            return 'DEFAULT'
        if cmd_type == CommandType.ANNOY:
            return 'ANNOY'
        if cmd_type == CommandType.GREET:
            return 'GREET'
        if cmd_type == CommandType.LOCK:
            return 'LOCK'
        if cmd_type == CommandType.UNLOCK:
            return 'UNLOCK'
        if cmd_type == CommandType.STOP:
            return 'STOP'
        if cmd_type == CommandType.NEUTRAL:
            return 'NEUTRAL'

COMMAND_LIST = (
    'annoy',
    'wesh',
    'stop'
)

class Command:
    def __init__(self, command_type: CommandType, execute: bool, target: int, text: str) -> None:
        self.type = CommandType.to_str(command_type)
        self.execute = execute
        self.target = target
        self.text = text

    @staticmethod
    def empty() -> any:
        return Command(
        command_type=CommandType.DEFAULT,
        execute=False, target='', text='')

    @staticmethod
    def greet(target_id: int) -> any:
        return Command(
        command_type=CommandType.GREET,
        execute=True, target=target_id, text='cv kho na7amdo rabi ou nechekrouh')
    
    @staticmethod
    def annoy(target_id: int) -> any:
        return Command(
        command_type=CommandType.ANNOY,
        execute=True, target=target_id, text=f'thared :man_shrugging: <@{target_id}>')
    
    @staticmethod
    def neutral(target_id: int) -> any:
        return Command(
            command_type=CommandType.NEUTRAL,
            execute=True, target=target_id, text='ye')

    #TODO add a database containing a few phrases
    #then make a word randomizer that picks
    #dialogue
    #TODO the dialogue has to be neutral
    #as in suitable for every situation
