import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


class TimeWriter:
    def day_write(self):
        markup = types.InlineKeyboardMarkup(row_width=5)
        day_1 = types.InlineKeyboardButton(
            text='1', callback_data=1)
        day_2 = types.InlineKeyboardButton(
            text='2', callback_data=2)
        day_3 = types.InlineKeyboardButton(
            text='3', callback_data=3)
        day_4 = types.InlineKeyboardButton(
            text='4', callback_data=4)
        day_5 = types.InlineKeyboardButton(
            text='5', callback_data=5)
        day_6 = types.InlineKeyboardButton(
            text='6', callback_data=6)
        day_7 = types.InlineKeyboardButton(
            text='7', callback_data=7)
        day_8 = types.InlineKeyboardButton(
            text='8', callback_data=8)
        day_9 = types.InlineKeyboardButton(
            text='9', callback_data=9)
        day_10 = types.InlineKeyboardButton(
            text='10', callback_data=10)
        day_11 = types.InlineKeyboardButton(
            text='11', callback_data=11)
        day_12 = types.InlineKeyboardButton(
            text='12', callback_data=12)
        day_13 = types.InlineKeyboardButton(
            text='13', callback_data=13)
        day_14 = types.InlineKeyboardButton(
            text='14', callback_data=14)
        day_15 = types.InlineKeyboardButton(
            text='15', callback_data=15)

        markup.add(day_1, day_2, day_3, day_4, day_5, day_6, day_7)
        return markup

    def time_write(self):
        keyboard = types.InlineKeyboardMarkup(row_width=3)

        time1 = types.InlineKeyboardButton(
            text='8:00', callback_data='time1_button')
        time2 = types.InlineKeyboardButton(
            text='9:00', callback_data='time2_button')
        time3 = types.InlineKeyboardButton(
            text='10:00', callback_data='time3_button')
        time4 = types.InlineKeyboardButton(
            text='11:00', callback_data='time4_button')
        time5 = types.InlineKeyboardButton(
            text='12:00', callback_data='time5_button')
        time6 = types.InlineKeyboardButton(
            text='13:00', callback_data='time6_button')
        time7 = types.InlineKeyboardButton(
            text='14:00', callback_data='time7_button')
        time8 = types.InlineKeyboardButton(
            text='15:00', callback_data='time8_button')
        time9 = types.InlineKeyboardButton(
            text='16:00', callback_data='time9_button')
        time10 = types.InlineKeyboardButton(
            text='17:00', callback_data='time10_button')
        time11 = types.InlineKeyboardButton(
            text='18:00', callback_data='time11_button')

        keyboard.add(time1, time2, time3, time4, time5, time6,
                     time7, time8, time9, time10, time11)
        return keyboard


@bot.message_handler(commands=['start'])
def start_message(message):
    TimeWriters = TimeWriter()
    bot.send_message(
        message.chat.id, text="Выберите чиcло на которое записатся:", reply_markup=TimeWriters.day_write())


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    TimeWriters = TimeWriter()
    # days
    if call.data == '1':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '2':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '3':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '4':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '5':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '6':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())
    elif call.data == '7':
        bot.send_message(
            call.message.chat.id, text="На который час сможыте прити?", reply_markup=TimeWriters.time_write())

    # times
    if call.data == '1' and call.data == 'time1_button':
        bot.answer_callback_query(
            callback_query_id=call.id, text='Вы записались к доктору!')

    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
