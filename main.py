import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Bot Token ကို ထည့်ပါ (သို့မဟုတ် Environment Variable ကနေ ယူပါ)
"TOKEN = "သင့်ရဲ့_တကယ့်_Bot_Token"


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"မင်္ဂလာပါ! သင်ပို့ထား aတာကတော့: {update.message.text}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    application.run_polling()
