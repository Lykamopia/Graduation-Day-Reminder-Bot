from dotenv import load_dotenv
import os
import datetime
import telegram
import asyncio

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Replace with your actual graduation date
GRADUATION_DATE = datetime.date(2024, 8, 3)

async def post_countdown_to_telegram():
    days_left = get_days_until_graduation()
    message = f"Countdown to Graduation: \n"
    message += generate_realtime_countdown(days_left)

    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        # Send the text message
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='HTML')
        print(f"Posted to Telegram: {message}")

        # Send the corresponding image if available
        image_filename = f"{days_left}.png"
        image_path = f"image/{image_filename}"  # Replace with your actual image folder path
        if days_left >= 0 and days_left <= 50:  # Assuming images are available for days 1 to 50
            if os.path.exists(image_path):
                with open(image_path, 'rb') as photo:
                    await bot.send_photo(chat_id=CHAT_ID, photo=photo)
                    print(f"Posted image to Telegram: {image_filename}")
            else:
                print(f"Image file does not exist: {image_path}")
        elif days_left == 0:
            print("Graduation Day! No image to send.")
        else:
            print(f"No image available for {days_left} days left.")
    except telegram.error.TelegramError as e:
        print(f"Failed to post to Telegram: {e}")

def get_days_until_graduation():
    today = datetime.date.today()
    days_left = (GRADUATION_DATE - today).days
    return days_left

def generate_realtime_countdown(days_left):
    if days_left > 0:
        countdown_str = f"<b>Days left:</b> {days_left} days\n"
        countdown_str += generate_progress_bar(days_left)
    elif days_left == 0:
        countdown_str = "<b>Today is Graduation Day!</b>"
    else:
        countdown_str = "<b>Graduation has already passed!</b>"

    return countdown_str

def generate_progress_bar(days_left, bar_length=20):
    total_days = (GRADUATION_DATE - datetime.date.today()).days + days_left
    progress_percent = int((total_days - days_left) / total_days * bar_length)
    bar = '▓' * progress_percent + '░' * (bar_length - progress_percent)
    return f"<code>{bar}</code>"

async def main():
    while True:
        await post_countdown_to_telegram()
        # Wait for 24 hours (86400 seconds) before sending the next message
        await asyncio.sleep(86500)

if __name__ == "__main__":
    asyncio.run(main())
