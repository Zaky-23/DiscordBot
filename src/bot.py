from discord import Client
from parse import parse_command
from command import Command, CommandType

class Bot(Client):
    def update_info(self, command):
        self.current_target = command.target
        print(f'current_target: {self.current_target}' )
        self.execute = command.execute
    
    async def be_annoying(self, command, message):
        if not command.execute:
            return
        if message.author.id == self.current_target:
            command = Command.annoy(self.current_target)
            await message.channel.send(command.text)
            return

    async def on_ready(self):
        myName = str(self.user).split('#')[0]
        print(f'Hello I\'m {myName}')

    async def on_message(self, message):
        if message.author == self.user: 
            return

        author = str(message.author).split('#')[0]
        content = str(message.content)
        channel = str(message.channel)
        user_id = str(message.author.id)
        print(f'Message from: {author}\nContent: {content}\nChannel: {channel}\nID: {user_id}')

        if content.startswith('!'):
            command = parse_command(message)

            print(f'Executing Command {command.type}')
            await message.channel.send(command.text)
            return

        # if author == 'Zeke':
        #     if message.content.startswith('!wlido'):
        #         await message.channel.send('wesh papa!!!')
        #         return

        # elif message.content.startswith('!wlido'):
        #     await message.channel.send('wesh')
        #     return