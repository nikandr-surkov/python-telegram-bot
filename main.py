import logging
import sys
import os
import signal
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants
MINI_APP_URL = "https://make-ton-telegram-mini-app-1.vercel.app/"
WELCOME_IMAGE_PATH = 'preview.png'

# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Message texts
WELCOME_MESSAGE = (
    "👋 Welcome to my Demo Bot!\n\n"
    "This bot demonstrates basic Telegram bot functionality "
    "and integration with Telegram Mini Apps.\n\n"
    "🔍 Features:\n"
    "- Basic command handling\n"
    "- Inline keyboard integration\n"
    "- Mini App integration\n\n"
    "Click the button below to open my Mini App!"
)

HELP_MESSAGE = (
    "🤖 Available Commands:\n\n"
    "/start - Start the bot and see welcome message\n"
    "/help - Show this help message\n"
    "/info - Get information about the bot\n"
    "/contact - Get contact information\n"
    "/about - Learn more about the project"
)

INFO_MESSAGE = (
    "ℹ️ Bot Information\n\n"
    "This is a demo bot showing basic Telegram bot capabilities "
    "and integration with Mini Apps. It's built using python-telegram-bot "
    "library and serves as an educational example."
)

CONTACT_MESSAGE = (
    "📞 Contact Information\n\n"
    "Website: https://nikandr.com\n"
    "Telegram: @nikandr_s\n"
    "Email: nikandr.dev@gmail.com\n"
    "GitHub: https://github.com/nikandr-surkov"
)

ABOUT_MESSAGE = (
    "🔍 About This Project\n\n"
    "This bot was created as a demonstration of Telegram bot development "
    "using Python. It showcases various bot features including:\n\n"
    "• Command handling\n"
    "• Inline keyboards\n"
    "• Mini App integration\n"
    "• Image sharing\n"
    "• Interactive responses"
)


async def start(update: Update, context: CallbackContext):
    logger.info(f"User {update.effective_user.id} started the bot")
    keyboard = [
        [InlineKeyboardButton(
            "Open Mini App",
            web_app={"url": MINI_APP_URL}
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        with open(WELCOME_IMAGE_PATH, 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=WELCOME_MESSAGE,
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        logger.error(f"Welcome image not found at {WELCOME_IMAGE_PATH}")
        await update.message.reply_text(
            WELCOME_MESSAGE,
            reply_markup=reply_markup
        )


async def help(update: Update, context: CallbackContext):
    logger.info(f"User {update.effective_user.id} requested help")
    await update.message.reply_text(HELP_MESSAGE)


async def info(update: Update, context: CallbackContext):
    logger.info(f"User {update.effective_user.id} requested info")
    await update.message.reply_text(INFO_MESSAGE)


async def contact(update: Update, context: CallbackContext):
    logger.info(f"User {update.effective_user.id} requested contact info")
    await update.message.reply_text(CONTACT_MESSAGE)


async def about(update: Update, context: CallbackContext):
    logger.info(f"User {update.effective_user.id} requested about info")
    await update.message.reply_text(ABOUT_MESSAGE)


async def error_handler(update: Update, context: CallbackContext):
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, something went wrong. Please try again later."
        )


def signal_handler(signum, frame):
    logger.info('Signal received, shutting down...')
    exit(0)


def main():
    # Initialize bot
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("about", about))

    # Add error handler
    application.add_error_handler(error_handler)

    # Setup signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Start the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()