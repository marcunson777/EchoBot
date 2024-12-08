from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN

# Función para el comando /start
async def start(update: Update, context):
    await update.message.reply_text('¡Hola! Soy un bot que repite lo que dices.')

# Función para manejar mensajes de texto
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Función principal que inicializa el bot
def main():
    # Crea la aplicación con el token del bot
    application = Application.builder().token(BOT_TOKEN).build()

    # Comandos y handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Ejecuta el bot
    application.run_polling()

if __name__ == '__main__':
    main()
