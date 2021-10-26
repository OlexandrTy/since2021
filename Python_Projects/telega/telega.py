import telebot
import random
from graphics import *
win = GraphWin()
pt = Point(100, 50)
cir = Circle(pt, 25)
cir.draw(win)


bot = telebot.TeleBot('888716873:AAE_cr1wQt5IeeZbReR00S2hGvDq4cQpsxc')
koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)
i=0
gameover = 0
def _count(new):
        global i
        i+=new
        return i

#, use_context=True

#@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id,  message.text)



@bot.message_handler(commands=['start', 'black_jack'])
def send_welcome(message):
	bot.send_message(message.chat.id,  'Поиграем в очко?\nБудете брать карту? y/n\n')
	global i, gameover
	i = 0
	gameover = 2

@bot.message_handler(content_types=['text'])
def send_ifY(message):
        global gameover
        if message.text=="y" and gameover==2:
            current = koloda.pop()
            count = _count(current)
            #count += current
            bot.send_message(message.chat.id, 'Вам попалась карта достоинством %d' %count)
            
            print('Вам попалась карта достоинством %d' %current)
           
            if count > 21:
                    bot.send_message(message.chat.id, 'Извините, но вы проиграли')
                    bot.send_message(message.chat.id, 'До встречи')
                    gameover=1
            elif count == 21:
                    bot.send_message(message.chat.id, 'Поздравляю, вы набрали 21!')
                    gameover=1
            else:
                    bot.send_message(message.chat.id, 'У вас %d очков. \nБудете брать карту? y/n\n' %count)
    
        elif message.text == 'n':
            count = _count(0)
            bot.send_message(message.chat.id, 'У вас %d очков и вы закончили игру.' %count)
            bot.send_message(message.chat.id, 'До встречи')
            gameover=1
        if gameover==0:    
	        bot.send_message(message.chat.id,  'Cначала ')
#def send_welcome(message):
#	bot.send_message(message.chat.id,  'Поиграем в очко?')
	




#@bot.message_handler(commands=['BG'])
def black_jack():
    koloda = [6,7,8,9,10,2,3,4,11] * 4
    random.shuffle(koloda)
    print('Поиграем в очко?')
    count = 0

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current = koloda.pop()
            print('Вам попалась карта достоинством %d' %current)
            count += current
            if count > 21:
                print('Извините, но вы проиграли')
                break
            elif count == 21:
                print('Поздравляю, вы набрали 21!')
                break
            else:
                print('У вас %d очков.' %count)
        elif choice == 'n':
            print('У вас %d очков и вы закончили игру.' %count)
            break

    print('До новых встреч!')


    
bot.polling(none_stop = True)
