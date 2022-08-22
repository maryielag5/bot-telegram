import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# configurar logging
logging.basicConfig(
  level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()
# NOMBRE DEL BOT  @maryiela_bot:
TOKEN = "2053260815:-2Ho"  # cambiar TOKEN desdes BOTFather-TELEGRAM
print(TOKEN)

def bienvenida(update, context):
  logging.info(f"El usuario {update.effective_user['first_name']}, ha iniciado una conversación")
  name = update.effective_user['first_name']
  update.message.reply_text(f"Hola {name} BIENVENIDO, ¿Te puedo ayudar en algo?")
  print(update)

def responder_dia(update, context):
  print(update)
  text  = update.message.text
  user_id = update.effective_user['id']
  context.bot.sendMessage(
      chat_id = user_id,
      parse_mode="MarkdownV2",
      text= "Buenos noches, soy TU BOT estaré atenta para lo que necesites")


if __name__ == "__main__":
  #informacion del bot
  my_bot = telegram.Bot(token = TOKEN)
  print(my_bot.getMe())

# enlazando nuestro updater con nuestro bot
updater = Updater(my_bot.token, use_context=True)

# creamos un despachador
dp = updater.dispatcher

# Creamos los manejadores
dp.add_handler(CommandHandler("iniciar", bienvenida))  # iniciar con /start
dp.add_handler(MessageHandler(Filters.text, responder_dia))

updater.start_polling()

updater.idle() #permite finalizar el bot --- Contrl + C
