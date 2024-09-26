from telegram.ext import Updater, messagehandler, filters, commandhandler, CommandHandler, CallbackQueryHandler
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
API_KEY ='7330326835:AAGgMpAJ9_mH0_clk1kT-5rO5KT8jNWwBuE'
updater = Updater(token=API_KEY, use_context =True)

def show_btn(update,context):
    keyboard = [
        [InlineKeyboardButton("시작!", callback_data='1')
        ,InlineKeyboardButton("종료!",callback_data='2')]
    ]
    reply_markup= InlineKeyboardMarkup(keyboard)
    # 메세지와 버튼 보내기
    update.message.reply_text('선택 하세요!:', reply_markup=reply_markup)
def btn_event(update, context):
    query= update.callback_query
    query.answer(text='선택 확인!!') # dkfflacvkd
    # 선택버튼 응답
    query.edit_message_text(text=f'선택값은{query.data}')

updater.dispatcher.add_handler(CommandHandler('stock', show_btn))
updater.dispatcher.add_handler(CallbackQueryHandler(btn_event))
updater.start_polling()
updater.idle()