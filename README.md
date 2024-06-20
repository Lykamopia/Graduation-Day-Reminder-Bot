# Graduation Day Countdown Bot

Welcome to the Graduation Day Countdown Bot repository! This Telegram bot helps you count down the days until your graduation day, providing daily reminders, the days left in image format and visual progress updates.

## Features

- **Countdown Updates**: Receive daily updates on the number of days left until your graduation.
- **Visual Progress Bar**: See a visual representation of the progress towards your graduation day.
- **Image Notifications**: Image updates for days left and special countdown milestones.

## Setup

To use the Graduation Day Countdown Bot, follow these steps:

1. **Clone the repository:**

   ```
   git clone https://github.com/Lykamopia/Graduation-Day-Reminder-Bot.git
   cd Graduation-Day-Reminder-Bot
   ```

2. **Install dependencies:**

   Ensure you have Python 3.x installed. Install required Python packages using pip:

   ```
   pip install python-telegram-bot schedule
   ```

3. **Set up your environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```

   ```
   CHAT_ID=your_chat_id
   ```

   Replace `your_telegram_bot_token` with your Telegram Bot API token obtained from [@BotFather](https://t.me/BotFather).

4. **Run the bot:**

   Execute the main script to start the bot:

   ```
   python countdown_bot.py
   ```

5. **Interact with the bot:**

   Start a chat with your bot on Telegram and type `/start` to begin receiving countdown updates.

## Contributing

Contributions are welcome! Here's how you can contribute to the project:

- Report bugs or suggest features by [creating an issue](https://github.com/Lykamopia/Graduation-Day-Reminder-Bot.git/issues).
- Fork the repository, make your changes, and submit a pull request for review.
- Help improve documentation by suggesting edits to this `README.md` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
