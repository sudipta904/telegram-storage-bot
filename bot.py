from pyrogram import Client, filters
import os

# 🔹 Railway ke Environment Variables se values le raha hai
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

# 🔹 Bot initialize
app = Client(
    "storage_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ Start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Hello 👋\n\n"
        "Main ek **Storage Bot** hoon.\n"
        "Tum jo bhi file bhejoge, main usse storage channel me save kar dunga ✅"
    )

# ✅ Jab koi file aaye (video, photo, document, audio, etc.)
@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def save_file(client, message):
    # File ko storage channel me forward karna
    sent = await message.forward(CHANNEL_ID)

    # File ka link reply me dena
    file_link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.id}"
    await message.reply_text(f"✅ File Saved!\n\n📂 [Open File Link]({file_link})", disable_web_page_preview=True)

# 🔹 Bot run karega
app.run()
