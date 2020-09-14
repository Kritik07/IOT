import telepot


token='1234280727:AAFM3LKbA6dVZER3Cl2jXELfQhuPNgX2vOI'
bot = telepot.Bot(token)
print (bot.getMe())

    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        bot.sendMessage(chat_id,"You said '{}'".format(msg['text']))
       
bot.message_loop(handle)
