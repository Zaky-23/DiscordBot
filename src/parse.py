from command import Command, CommandType, COMMAND_LIST

def parse_command(message) -> Command:

    tokens = str(message.content).split(' ')
    try:
        command = tokens[1].lower()
    except IndexError: 
        print(f'{__file__} command: OutOfBoundaryIndex')
        return Command.neutral('')
    arguments = tokens[2:]        

    if commmand_exists(command) == False:
        print(f'Command "{command}" does not exist')
        return Command.empty()

    if command == 'annoy':
        try:
            target_id = str(arguments[0])
            return Command.annoy(target_id)
        except IndexError: 
            print('OutOfBoundaryIndex')
            return Command(CommandType.ANNOY, 
            True, '', "chkon lazem n9ela9?")

    if command == 'stop':
        return Command(
            CommandType.STOP,
            True, '', 'ok')
    
    if command == 'wesh':
        #TODO do somthing i forgot
        return Command.greet('')

def commmand_exists(command : str) -> bool:
    for cmd in COMMAND_LIST:
        if command == cmd:
            return True
    return False