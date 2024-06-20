from dotenv import load_dotenv
import os
import telegram
import asyncio

# Load environment variables from.env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def get_updates():
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    updates = await bot.get_updates()

    for update in updates:
        if update.message:
            chat_id = update.message.chat_id
            print(f"Chat ID: {chat_id}")
        else:
            print("No message found in this update")

if __name__ == "__main__":
    asyncio.run(get_updates())
