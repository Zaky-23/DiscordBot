from command import Command, CommandType, COMMAND_LIST

def parse_command(message) -> Command:

    tokens = str(message.content).split(' ')
    command = tokens[1:2]
    arguments = tokens[2:]

    if command is None:
        return Command.greet()

    if commmand_exists(command[0]) == False:
        print(f'Command {command[0]} does not exist')
        return Command.empty()

    if command[0] == 'annoy':
        try:
            target_id = str(arguments[0])
        except:
            print('OutOfBoundaryIndex')
            target_id = ''

        return Command.annoy(target_id)

def commmand_exists(command : str) -> bool:
    if(command == 'annoy'):
        return True
    return False