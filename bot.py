import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, ContextTypes,
    MessageHandler, CommandHandler, CallbackQueryHandler,
    filters
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

# Tag pairs: (English, Russian)
TAGS = [
    ("War", "Война"),
    ("Meme", "Мем"),
    ("News", "Новости"),
    ("Idea", "Идея"),
    ("Offtopic", "Флуд")
]

# Per-user message storage for callback handling
user_message_cache = {}

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Welcome message
WELCOME_MESSAGE = (
    "👋 Welcome!\n"
    "Send me a post (text, image, or file), and I’ll forward it to the channel anonymously.\n"
    "You’ll be asked to choose a topic tag first.\n\n"
    "👋 Добро пожаловать!\n"
    "Отправьте сообщение (текст, изображение или файл), и я анонимно опубликую его в канале.\n"
    "Сначала вам нужно будет выбрать тему."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    # Store message content for later use
    user_message_cache[message.from_user.id] = message

    # Build tag keyboard
    keyboard = [
        [InlineKeyboardButton(f"{en} / {ru}", callback_data=en)]
        for en, ru in TAGS
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await message.reply_text("📌 Choose a tag / Выберите тег:", reply_markup=reply_markup)

async def tag_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    if user_id not in user_message_cache:
        await query.edit_message_text("⚠️ No message found. Please send a message first.")
        return

    # Find both tags
    tag_en = query.data
    tag_pair = next(((en, ru) for en, ru in TAGS if en == tag_en), None)
    if not tag_pair:
        await query.edit_message_text("⚠️ Tag not recognized.")
        return

    hashtags = f"#{tag_pair[0].lower()} #{tag_pair[1].lower()}"
    message = user_message_cache.pop(user_id)  # Clear after use
    text = (message.text or message.caption or "").strip()
    final_text = f"{hashtags}\n{text}" if text else hashtags

    if message.photo:
        photo = message.photo[-1].file_id
        await context.bot.send_photo(chat_id=CHANNEL_USERNAME, photo=photo, caption=final_text)

    elif message.document:
        doc = message.document.file_id
        await context.bot.send_document(chat_id=CHANNEL_USERNAME, document=doc, caption=final_text)

    elif text:
        await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=final_text)

    else:
        await query.edit_message_text("❗ Unsupported message type.")

    await query.edit_message_text("✅ Post sent! / Пост опубликован!")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), handle_message))
    app.add_handler(CallbackQueryHandler(tag_chosen))

    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

