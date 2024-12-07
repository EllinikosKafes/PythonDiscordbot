from typing import Final
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE

TOKEN: Final[str] = "TOKEN_HERE"

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return


    '''Simpler code
    if user_message[0] == '?':
        is_private = True
    else:
        is_private = False
    if is_private:
        user_message = user_message[1:]
    '''
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]


    #TAKING THE RESPONSE FROM THE "responses.py" AND SENDING IT TO PRIVATE OR CHANNEL CHAT
    try:
        response: str = get_response(user_message)

        """BASICALLY, IF THERE IS A '?' IN FRONT OF THE MESSAGE , THEN SEND THE MESSAGE TO AUTHOR(aka in private) , ELSE SEND
        IT TO THE CHANNEL (aka in public)"""
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:

    #Basically if the message's author is the bot itself (aka client.user) then return nothing , so we don't have a catastrophic loop
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    #WE USE PRINT SO WE CAN LOG THE MESSAGES OF THE CHANNELS
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()