from discord import Client
from parse import parse_command
from command import Command, CommandType

class Bot(Client):
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
        print(f'Message from: {author}\nContent: {content}\nChannel: {channel}\nID: {user_id}\n')

        if content.startswith('!'):
            command = parse_command(message)
            
            if command.type == CommandType.GREET:
                print("GREET")
                await message.channel.send(command.text)

            if command.type == CommandType.ANNOY:
                print("ANNOY")
                await message.channel.send(command.text)   

        # if author == 'Zeke':
        #     if message.content.startswith('!wlido'):
        #         await message.channel.send('wesh papa!!!')
        #         return

        # elif message.content.startswith('!wlido'):
        #     await message.channel.send('wesh')
        #     return