import telebot;
import requests;
import re;

bot=telebot.TeleBot('1010086503:AAFfWdw6y21LoLpEPWdJoDpr74Z8TbPVJ_o')

txt = '';

def transfer(mytext):
    key = 'trnsl.1.1.20191117T095324Z.9caedac53d197ea6.18cf2120a10a3acb809912e31652eae3cabd861d' 
    data = {'lang':'en', 'key':key, 'text':mytext, 'format':'plain'} 
    r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data).json() 
    r['mytext'] = mytext 
    return r 



@bot.message_handler(content_types=['text'])

def get_txt(message):
    global a;
    a = transfer(message.text)
    bot.send_message(message.chat.id, (a['text'][0])) 
    


bot.polling()