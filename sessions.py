### TELETHON SESSION FILE ###
from telethon.sync import TelegramClient

api_id = 7712824
api_hash = '2d3673e18b462f8032c4eea2f50b9f52'
with TelegramClient('my_session.session', api_id, api_hash) as client:
    print("Your session file has been created successfully!")

#------------------------------------------

### TELETHON SESSION FILE WITH 2FA HANDLER ###
from telethon.sync import TelegramClient

api_id = 7712824
api_hash = '2d3673e18b462f8032c4eea2f50b9f52'

client = TelegramClient('my_session.session', api_id, api_hash)
client.start('PHONE_NUMBER', '2FA_HERE')
#client.start('+18032058891', '8275')

#------------------------------------------

### TELETHON SESSION STRING ###
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 7712824
api_hash = '2d3673e18b462f8032c4eea2f50b9f52'

with TelegramClient(StringSession(), api_id, api_hash) as client:
    session_string = client.session.save()
    print(f"Your session string:\n{session_string}")

#------------------------------------------

### PYROGRAM SESSION FILE ###
from pyrogram import Client

api_id = 7712824
api_hash = '2d3673e18b462f8032c4eea2f50b9f52'

with Client('my_session', api_id, api_hash) as app:
    app.send_message('me', 'Hello, Pyrogram!')
