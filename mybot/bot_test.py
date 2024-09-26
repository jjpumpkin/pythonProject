# pip install python-telegram-bot==13.11
import os
import time

from telegram.ext import Updater ,MessageHandler, Filters ,CommandHandler

from Python_Base.ex_util.uid import time_filename

API_KEY ='7330326835:AAGgMpAJ9_mH0_clk1kT-5rO5KT8jNWwBuE'
updater = Updater(token=API_KEY, use_context =True)
f =None
def echo(update, context):
    user_id = update.effective_chat.id
    user_msg = update.message.text
    print(f"{user_id}, {user_msg}")
    context.bot.send_message(chat_id=user_id,text=user_msg)

def my_diary(update,context):
    global f #전역변수 사용
    print("파일로 저장")
    user_id = update.effective_chat.id
    user_msg = update.message.text

    if '종료' in user_msg:
        if f:
            f.close()
            context.bot.send_message(chat_id=user_id, text='다이어리 종료')
    else:
        f = open('my_diary.txt', 'a', encoding='utf8')
        f.write(user_msg.replace('/diary','').strip())
        f.writelines('\n')
        context.bot.send_message(chat_id=user_id ,text= '작성중...')

def save_photo(update, context):
    # 1.폴더 췍
    image_dir = './img'
    if not os.path.exists(image_dir):  # 해당 경로가 존재하지 않으면
        os.makedirs(image_dir)
    # 2.이름 생성
    time_filename = time.struct_time('%Y%m%d%H%M%S') +'.png'
    # 3.폴더 +이름
    img_path =os.path.join(image_dir, time_filename)
    print(img_path)
    # 4.저장
    photo_id= update.message.photo[-1].file_id
    photo_file= context.bot.getFile(photo_id)
    photo_file.download(img_path)

    photo_id=update.message.photo[-1].file_id
    photo_file= context.bot.getFile(photo_id)
    photo_file.download('save.png')
    update.message.reply_text('photo saved')

echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)
updater.dispatcher.add_handler(echo_handler)
diary_handler = CommandHandler('diary',my_diary)
updater.dispatcher.add_handler(diary_handler)
# 일기 저장
diary_handler = CommandHandler('diary', my_diary)
updater.dispatcher.add_handler(diary_handler)
# 사진 저장
photo_handler = MessageHandler(Filters.photo, save_photo)
updater.dispatcher.add_handler(photo_handler)

updater.start_polling()
updater.idle()

#str로 감싸준다