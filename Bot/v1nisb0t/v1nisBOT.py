import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("917126216:AAGQbec6upzjvqbLhjUsz5b-FDZT5Ol_O1o")
bot = Chatbot("b1gbot")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass






