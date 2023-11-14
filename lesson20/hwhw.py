class MyBot:
    def __init__(self, token):
        self.token = token
        # Регистрируйте обработчики команд и сообщений
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("help", self.help))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.echo))
        self.dispatcher.add_handler(MessageHandler(Filters.sticker, self.send_sticker))
        self.dispatcher = self.updater.dispatcher
        
        # Запустите бота
        self.updater.start_polling()
        
    def start(self, update, context):
        # Обработчик команды /start
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I have all the songs of BLACKPINK!.")
        
    def help(self, update, context):
        # Обработчик команды /help
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я могу отправлять текстовые сообщения, стикеры и получать ID чатов.")
        
    def echo(self, update, context):
        # Обработчик текстовых сообщений
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
        
    def send_sticker(self, update, context):
        # Обработчик получения стикеров
        context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=update.message.sticker.file_id)
        
# Создайте экземпляр вашего бота, передав ему токен
bot = MyBot("6713141695:AAGMXTZ5ZYMWeLG4B67euvpp0ylxZbxxy3o")