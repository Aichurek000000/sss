import requests


class TelegramBot:
    # создание бота
    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{token}/"
    
    # получение обновлений (все последние сообщения)
    def get_updates(self):
        response = requests.get(f"{self.url}getUpdates")
        data = response.json()
        return data
    
    # получить текст последнего сообщения
    def get_last(self):
        data = self.get_updates()
        return data["result"][-1]["message"]["text"]
    
    # отправка сообщения
    def send_message(self, chat_id, text):
        requests.get(f"{self.url}sendMessage?chat_id={chat_id}&text={text}")

    # адресная справка
    def sync_chats(self):
        data = self.get_updates()
        chats = {}
        for update in data["result"]:
            key = update["message"]["chat"]["id"]
            value = update["message"]["from"]["first_name"]
            chats[key] = value
        self.chats = chats
        return chats
    
    def spam(self, text):
        for chat, name in self.chats.items():
            text_message = f"Hello, {name}! {text}"
            self.send_message(chat, text_message)

    def send_sticker(self, update, context):
    sticker_id = update.message.sticker.file_id
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker_id)



#import requests
#r#esponse = requests.get("https://api.telegram.org/bot6713141695:AAGMXTZ5ZYMWeLG4B67euvpp0ylxZbxxy3o/getMe")
#data = response.json()
#print(data["result"][0]["message"]["text"])