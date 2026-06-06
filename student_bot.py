import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"].rstrip("/")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)


def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary"))
    markup.add(InlineKeyboardButton("🏗️ الهندسة المدنية", callback_data="civil"))
    markup.add(InlineKeyboardButton("🪨 الجيولوجيا", callback_data="geology"))
    markup.add(InlineKeyboardButton("🛢️ هندسة النفط", callback_data="petroleum"))
    markup.add(InlineKeyboardButton("⚡ الهندسة الكهربائية", callback_data="electrical"))
    markup.add(InlineKeyboardButton("👥 روابط القروبات", callback_data="groups"))
    markup.add(InlineKeyboardButton("☎️ تواصل مع الإدارة", callback_data="contact"))
    return markup


def back_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main"))
    return markup


def secondary_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📘 القسم العلمي", callback_data="secondary_science"))
    markup.add(InlineKeyboardButton("📗 القسم الأدبي", callback_data="secondary_literary"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات سابقة", callback_data="secondary_exams"))
    markup.add(InlineKeyboardButton("📚 ملخصات ومناهج", callback_data="secondary_notes"))
    markup.add(InlineKeyboardButton("🎥 كورسات وشرح", callback_data="secondary_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def civil_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🧱 خواص مواد CE133", callback_data="civil_ce133"))
    markup.add(InlineKeyboardButton("📐 تحليل إنشائي CE203", callback_data="civil_ce203"))
    markup.add(InlineKeyboardButton("🚗 هندسة النقل CE311", callback_data="civil_ce311"))
    markup.add(InlineKeyboardButton("🚰 الهندسة الصحية", callback_data="civil_sanitary"))
    markup.add(InlineKeyboardButton("📚 مناهج القسم", callback_data="civil_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="civil_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def geology_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🌍 جيولوجيا عامة", callback_data="geo_general"))
    markup.add(InlineKeyboardButton("🗺️ خرائط جيولوجية", callback_data="geo_maps"))
    markup.add(InlineKeyboardButton("🪨 الصخور والمعادن", callback_data="geo_rocks"))
    markup.add(InlineKeyboardButton("🛢️ جيولوجيا النفط", callback_data="geo_petroleum"))
    markup.add(InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="geo_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def petroleum_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🕳️ Drilling", callback_data="pet_drilling"))
    markup.add(InlineKeyboardButton("🛢️ Reservoir", callback_data="pet_reservoir"))
    markup.add(InlineKeyboardButton("⚙️ Production", callback_data="pet_production"))
    markup.add(InlineKeyboardButton("📈 Well Logging", callback_data="pet_logging"))
    markup.add(InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="pet_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def electrical_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔌 Circuits", callback_data="elec_circuits"))
    markup.add(InlineKeyboardButton("⚙️ Machines", callback_data="elec_machines"))
    markup.add(InlineKeyboardButton("🏭 Power Systems", callback_data="elec_power"))
    markup.add(InlineKeyboardButton("📟 Electronics", callback_data="elec_electronics"))
    markup.add(InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="elec_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    text = """
أهلاً بك في دليل الطالب الليبي 🎓📚

هذا البوت يجمع كل ما يحتاجه الطالب في مكان واحد:

✅ أسئلة امتحانات سابقة
✅ مناهج وملخصات
✅ كورسات وشروحات
✅ روابط قروبات المواد
✅ ملفات ومراجع مفيدة

اختر القسم المطلوب:
"""
    bot.send_message(message.chat.id, text, reply_markup=main_menu())


@bot.message_handler(commands=["help"])
def help_command(message):
    text = """
طريقة استخدام البوت:

اضغط /start لفتح القائمة الرئيسية.
ثم اختر القسم المطلوب من الأزرار.

لإرسال ملفات أو أسئلة امتحانات للإضافة:
راسل الإدارة.
"""
    bot.send_message(message.chat.id, text)


@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    data = call.data

    if data == "main":
        bot.edit_message_text(
            "🎓 القائمة الرئيسية\n\nاختر القسم المطلوب:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

    elif data == "secondary":
        bot.edit_message_text(
            "🎒 الشهادة الثانوية\n\nاختر القسم أو الخدمة:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=secondary_menu()
        )

    elif data == "civil":
        bot.edit_message_text(
            "🏗️ الهندسة المدنية\n\nاختر المادة أو الخدمة:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=civil_menu()
        )

    elif data == "geology":
        bot.edit_message_text(
            "🪨 الجيولوجيا\n\nاختر القسم:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=geology_menu()
        )

    elif data == "petroleum":
        bot.edit_message_text(
            "🛢️ هندسة النفط\n\nاختر المجال:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=petroleum_menu()
        )

    elif data == "electrical":
        bot.edit_message_text(
            "⚡ الهندسة الكهربائية\n\nاختر المجال:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=electrical_menu()
        )

    elif data == "groups":
        text = """
👥 روابط القروبات

🎒 الشهادة الثانوية:
ضع الرابط هنا

🏗️ الهندسة المدنية:
ضع الرابط هنا

🪨 الجيولوجيا:
ضع الرابط هنا

🛢️ هندسة النفط:
ضع الرابط هنا

⚡ الهندسة الكهربائية:
ضع الرابط هنا
"""
        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=back_menu()
        )

    elif data == "contact":
        text = """
☎️ تواصل مع الإدارة

لإرسال ملفات، أسئلة امتحانات، ملخصات، أو طلب إضافة قروب:

راسل الإدارة:
@hmodh123

أرسل:
1. اسم القسم
2. اسم المادة
3. نوع الملف
4. الملف أو الرابط
"""
        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=back_menu()
        )

    elif data.startswith("secondary_"):
        bot.edit_message_text(
            "🎒 سيتم إضافة محتوى الشهادة الثانوية هنا قريبًا بإذن الله.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=back_menu()
        )

    else:
        bot.edit_message_text(
            "📚 سيتم إضافة الملفات والأسئلة والملخصات هنا قريبًا بإذن الله.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=back_menu()
        )


@app.route("/")
def home():
    return "Libyan Student Guide Bot is running."


@app.route("/webhook", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.get_data().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200


bot.remove_webhook()
bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
