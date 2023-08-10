from pyrogram import Client, filters
from helper.start import start

#obtener los datos de https://my.telegram.org/auth
app = Client(
    "Tasky",
    api_id= 'API_ID',
    api_hash="API_HASH",
    bot_token="BOT_TOKEN")

@app.on_message(filters.command("start"))
def handle_start(client, message):
    start(client, message)

print('Bot Online')
app.run()