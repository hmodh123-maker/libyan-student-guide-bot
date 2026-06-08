import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# إعداد البوت
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# --- القوائم الرئيسية ---
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary"))
    markup.add(InlineKeyboardButton("🏗️ الهندسة المدنية", callback_data="civil"))
    markup.add(InlineKeyboardButton("🪨 الهندسة الجيولوجية", callback_data="geology"))
    markup.add(InlineKeyboardButton("🛢️ هندسة النفط", callback_data="petroleum"))
    markup.add(InlineKeyboardButton("⚡ الهندسة الكهربائية", callback_data="electrical"))
    markup.add(InlineKeyboardButton("🏛️ هندسة العمارة", callback_data="architecture"))
    markup.add(InlineKeyboardButton("📊 الاقتصاد", callback_data="economy"))
    markup.add(InlineKeyboardButton("🗣️ اللغات", callback_data="languages"))
    markup.add(InlineKeyboardButton("📝 الشهادة الإعدادية", callback_data="prep"))
    return markup

# --- معالجة الأزرار ---
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    
    if call.data == "main":
        bot.edit_message_text("🎓 دليل الطالب الليبي - القائمة الرئيسية:", chat_id, msg_id, reply_markup=main_menu())
    
    # منطق الهندسة المدنية (كما أرسلت لي)
    elif call.data == "civil":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🧱 مستوى 100", callback_data="civil_100"))
        markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
        bot.edit_message_text("🏗️ الهندسة المدنية - اختر المستوى:", chat_id, msg_id, reply_markup=markup)
        
    elif call.data == "civil_100":
        text = "🧱 مواد مستوى 100:\n- خواص مواد (CE133)\n- كتابة تقارير (GH152)"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="civil"))
        bot.edit_message_text(text, chat_id, msg_id, reply_markup=markup)

    # منطق الجيولوجيا
    elif call.data == "geology":
        bot.edit_message_text("🪨 الهندسة الجيولوجية - قريباً سيتم إضافة المواد.", chat_id, msg_id, reply_markup=back_to_main())

    # يمكنك إضافة بقية الأقسام هنا بنفس الطريقة (petroleum, electrical, etc)
    else:
        bot.edit_message_text("🛠️ هذا القسم قيد التجهيز حالياً..", chat_id, msg_id, reply_markup=back_to_main())

def back_to_main():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main"))
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "✨ أهلاً بك في دليل الطالب الليبي، اختر تخصصك:", reply_markup=main_menu())

if __name__ == "__main__":
    print("🚀 البوت يعمل بنظام Polling...")
    bot.infinity_polling()
