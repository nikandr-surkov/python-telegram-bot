# Python Telegram Bot with Mini App Integration
A Python-based Telegram bot demonstrating basic bot functionality and Mini App integration. This project showcases how to create a fully functional Telegram bot with interactive features and web app integration using modern technologies.

## Project Overview
This bot demonstrates:
- Basic command handling
- Inline keyboard integration 
- Mini App integration
- Image sharing capability
- Interactive responses
- Logging and error handling

## Bot Features
- `/start` - Welcome message with Mini App button
- `/help` - List all available commands
- `/info` - Get bot information
- `/contact` - Display contact details
- `/about` - Learn about the project

## Prerequisites
- Python 3.7 or higher
- python-telegram-bot library
- python-dotenv library
- A Telegram Bot Token (from @BotFather)
- A web server for hosting Mini App (optional)

## Getting Started

### Option 1: Using PyCharm
1. Open PyCharm
2. Go to `File > Project from Version Control`
3. Enter URL: `https://github.com/nikandr-surkov/python-telegram-bot.git`
4. Choose your project directory
5. Click "Clone"
6. Install dependencies:
   ```bash
   pip install python-telegram-bot python-dotenv
   ```

### Option 2: Using Terminal
1. Clone the repository:
   ```bash
   git clone https://github.com/nikandr-surkov/python-telegram-bot.git
   cd python-telegram-bot
   ```

2. Install dependencies:
   ```bash
   pip install python-telegram-bot python-dotenv
   ```

3. Create a `.env` file:
   ```
   BOT_TOKEN=your_bot_token_here
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py`: Main bot script with all handlers and logic
- `.env`: Environment variables (not included in repo)
- `preview.png`: Welcome image
- `README.md`: Project documentation

## Key Features
- Asynchronous command handling
- Inline keyboard for Mini App launch
- Error handling and logging
- Signal handling for graceful shutdown
- Environment variable management
- Image sharing capability

## Technologies Used
- Python 3
- python-telegram-bot
- python-dotenv
- Telegram Bot API
- Telegram Mini Apps

## Bot Configuration
1. Create a new bot with @BotFather
2. Enable inline mode if needed
3. Set up commands using /setcommands:
   ```
   start - Start the bot and see welcome message
   help - Show help message
   info - Get information about the bot
   contact - Get contact information
   about - Learn more about the project
   ```
4. Set up your Mini App domain in Bot Settings

## Mini App Integration
The bot includes a button that opens a Mini App. To set up your own Mini App:
1. Host your web application
2. Add domain to @BotFather's Bot Settings > Web App Settings
3. Update MINI_APP_URL in the code
4. Test the integration

## Error Handling
The bot includes comprehensive error handling:
- File not found handling
- Command execution errors
- General error catching
- Logging for debugging

## Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.

## Learn More
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot Documentation](https://python-telegram-bot.org/)
- [Telegram Mini Apps](https://core.telegram.org/bots/webapps)

## Author
### Nikandr Surkov
- 🌐 Website: [nikandr.com](https://nikandr.com)
- 📺 YouTube: [@NikandrSurkov](https://www.youtube.com/@NikandrSurkov)
- 📱 Telegram: [@nikandr_s](https://t.me/nikandr_s)
- 📢 Telegram Channel: [Nikandr's Apps](https://t.me/+hL2jdmRkhf9jZjQy)
- 📰 Clicker Game News: [Clicker Game News](https://t.me/clicker_game_news)
- 💻 GitHub: [nikandr-surkov](https://github.com/nikandr-surkov)
- 🐦 Twitter: [@NikandrSurkov](https://x.com/NikandrSurkov)
- 💼 LinkedIn: [Nikandr Surkov](https://www.linkedin.com/in/nikandr-surkov/)
- ✍️ Medium: [@NikandrSurkov](https://medium.com/@NikandrSurkov)
