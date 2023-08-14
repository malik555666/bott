import logging
from telegram.ext import Updater, CommandHandler

# تفعيل تسجيل الأحداث لتتبع الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# تعيين مفتاح الوصول الخاص بالبوت
TOKEN = "6622736057:AAGh0dpVIt1eX4MhLyV_iBLtneqE25o3u1A"

# إنشاء كائن Updater وتمرير مفتاح الوصول إليه
updater = Updater(token=TOKEN)

# تعريف وظيفة لمعالجة أمر إرسال الرسالة
def send_welcome_message(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"وعليكم السلام أهلاً بك، {user.first_name} {user.last_name}!")

# إضافة معالج لأمر إرسال الرسالة
updater.dispatcher.add_handler(CommandHandler('abumalik', send_welcome_message))

# بدء الاستماع للأحداث وتشغيل البوت
updater.start_polling()
updater.idle()
