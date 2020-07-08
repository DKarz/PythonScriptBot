import telebot
import sys

bot = telebot.TeleBot("1191221513:AAEABQaWkHG2AFPcMbVSf6FL6zRpIL7IPs0")


def redirect_to_file(code):
    original = sys.stdout
    sys.stdout = open('redirect.txt', 'w')
    exec(code)
    sys.stdout = original
    

@bot.message_handler(content_types=["text"])
def handle_text(message):

    code = message.text.strip()
    try: 
        data = ""
        redirect_to_file(code)
        with open('redirect.txt', 'r') as file:
            data = file.read()
        bot.send_message(message.chat.id, data)
    except Exception as e:
        print("Error")
        bot.send_message(message.chat.id, "Something is wrong, I can feel it!")
    


bot.polling(none_stop=True, interval=0)
