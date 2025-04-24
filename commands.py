from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from ai import ask_ai


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = (
        "FURIA é uma das organizações mais icônicas do cenário de CS:GO!\n\n"
        "Criada em 2017, a equipe se destacou com grandes vitórias, incluindo títulos no ESL Pro League e muito mais!\n"
        "Com uma torcida apaixonada, a FURIA segue sendo um dos maiores nomes do CS global.\n\n"
        "Fique ligado para mais novidades!"
    )
    await update.effective_chat.send_message(info_text, parse_mode="Markdown")

async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agenda_text = (
        "Próximo campeonato da FURIA:\n"
        "Campeonato X - Data: 15 de Maio de 2025\n"
        "Fique ligado para mais informações!"
    )
    await update.effective_chat.send_message(agenda_text, parse_mode="Markdown")

async def jogadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    players_text = (
        "🎯 *Jogadores da FURIA - CS2*\n\n"
        "👑 *KSCERATO* - Rifler / Lenda silenciosa\n"
        "⚡ *yuurih* - Entry / Fragger incansável\n"
        "🎯 *chelo* - Rifler / Estilo agressivo\n"
        "🧠 *arT* - IGL / Mestre das estratégias arriscadas\n"
        "🧊 *drop* - Suporte / Frieza e precisão\n\n"
        "🔥 FURIA dominando o servidor! Qual o seu favorito?"
    )
    await update.effective_chat.send_message(players_text, parse_mode="Markdown")

async def fan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fan_text = (
        "💥 *Você é FURIA até o fim?*\n"
        "Mostre que é torcedor raiz com essas ações:\n\n"
        "🔥 [Twitter da FURIA](https://twitter.com/furia)\n"
        "🎥 [Canal da FURIA no YouTube](https://www.youtube.com/c/FURIA)\n"
        "🧢 [Loja Oficial](https://loja.furia.gg/)\n\n"
    )
    await update.effective_chat.send_message(fan_text, parse_mode="Markdown")

async def responder_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta_usuario = update.message.text

    if pergunta_usuario.lower() in ["oi", "olá", "hello", "olá bot", "menu"]:
        return await menu(update, context)
    prompt_ia = f"Responda de forma curta e objetiva: {pergunta_usuario}"
    resposta_ai = ask_ai(prompt_ia)
    await update.message.reply_text(resposta_ai)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📅 Agenda", callback_data='agenda')],
        [InlineKeyboardButton("🎮 Jogadores", callback_data='jogadores')],
        [InlineKeyboardButton("📣 Fã da FURIA", callback_data='fan')],
        [InlineKeyboardButton("ℹ️ Informações", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("🔥 Bem-vindo(a) ao universo da FURIA!\nEscolha uma opção ou me faça uma pergunta!", reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'agenda':
        await agenda(update, context)
    elif query.data == 'jogadores':
        await jogadores(update, context)
    elif query.data == 'fan':
        await fan(update, context)
    elif query.data == 'info':
        await info(update, context)