import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8770069616:AAGcjYRyOQP84l-tYHrZ8F-4d1t03-ZgwjY"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"မင်္ဂလာပါ! သင်ပို့ထားသော စာကို လက်ခံရရှိပါပြီ: {update.message.text}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    print("Bot စတင်အလုပ်လုပ်နေပြီ...")
    application.run_polling()


