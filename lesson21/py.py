import telebot
TOKEN = "6713141695:AAGMXTZ5ZYMWeLG4B67euvpp0ylxZbxxy3o"
chat_id = "630037956"
tb = telebot.TeleBot(TOKEN)
with open('my.jpg', 'rb') as photo:
    tb.send_photo(chat_id, photo)