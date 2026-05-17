import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from excel.convert import process_excel

TOKEN = os.getenv("TOKEN")


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document

    file = await context.bot.get_file(document.file_id)

    input_path = f"input_{document.file_name}"
    output_path = f"output_{document.file_name}"

    await file.download_to_drive(input_path)

    process_excel(input_path, output_path)

    await update.message.reply_document(document=open(output_path, "rb"))
    os.remove(output_path)
    os.remove(input_path)

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    print('Telegram bot started')
    app.run_polling()


