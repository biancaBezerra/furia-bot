import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from commands import info, agenda, jogadores, fan,handle_callback, responder_pergunta

load_dotenv()

TOKEN = os.getenv("TOKEN")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.add_handler(CommandHandler("fan", fan))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_pergunta))
    app.add_handler(CallbackQueryHandler(handle_callback))


    print("Bot está rodando!")
    app.run_polling()
