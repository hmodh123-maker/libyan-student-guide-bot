import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"].strip().rstrip("/")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)


# =========================
# MENUS
# =========================

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary"))
    markup.add(InlineKeyboardButton("🏗️ الهندسة المدنية", callback_data="civil"))
    markup.add(InlineKeyboardButton("🪨 الهندسة الجيولوجية", callback_data="geology"))
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
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="secondary_notes"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات سابقة", callback_data="secondary_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات وشرح", callback_data="secondary_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def civil_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات المدني", callback_data="civil_syllabus"))
    markup.add(InlineKeyboardButton("🧱 خواص مواد CE133", callback_data="civil_ce133"))
    markup.add(InlineKeyboardButton("🚗 ترانس CE311", callback_data="civil_ce311"))
    markup.add(InlineKeyboardButton("💧 فلود 1 CE221", callback_data="civil_ce221"))
    markup.add(InlineKeyboardButton("📏 مساحة 1", callback_data="civil_survey1"))
    markup.add(InlineKeyboardButton("📐 تحليل إنشائي 2 CE303", callback_data="civil_ce303"))
    markup.add(InlineKeyboardButton("🌱 سويل 1 CE342", callback_data="civil_ce342"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def geology_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات الجيولوجيا", callback_data="geo_syllabus"))
    markup.add(InlineKeyboardButton("🧪 جيوكيمياء - جزئية النصفي", callback_data="geo_geochemistry"))
    markup.add(InlineKeyboardButton("🌍 جيولوجيا عامة", callback_data="geo_general"))
    markup.add(InlineKeyboardButton("🗺️ خرائط جيولوجية", callback_data="geo_maps"))
    markup.add(InlineKeyboardButton("🪨 الصخور والمعادن", callback_data="geo_rocks"))
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


# =========================
# TEXTS
# =========================

def welcome_text():
    return """
أهلاً بك في دليل الطالب الليبي 🎓📚

هذا البوت يجمع كل ما يحتاجه الطالب في مكان واحد:

✅ أسئلة امتحانات سابقة
✅ مناهج وملخصات
✅ كورسات وشروحات
✅ روابط قروبات المواد
✅ ملفات ومراجع مفيدة

اختر القسم المطلوب:
"""


def help_text():
    return """
طريقة استخدام البوت:

اضغط /start لفتح القائمة الرئيسية.
ثم اختر القسم المطلوب من الأزرار.

لإرسال ملفات أو أسئلة امتحانات للإضافة:
راسل الإدارة.
"""


# =========================
# COMMANDS
# =========================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, welcome_text(), reply_markup=main_menu())


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.chat.id, help_text())


# =========================
# BUTTON HANDLER
# =========================

@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    try:
        bot.answer_callback_query(call.id)
    except Exception as e:
        print("answer_callback_query error:", repr(e))

    data = call.data
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    print("Callback data:", data)

    if data == "main":
        bot.edit_message_text(
            "🎓 القائمة الرئيسية\n\nاختر القسم المطلوب:",
            chat_id,
            message_id,
            reply_markup=main_menu()
        )

    elif data == "secondary":
        bot.edit_message_text(
            "🎒 الشهادة الثانوية\n\nاختر القسم أو الخدمة:",
            chat_id,
            message_id,
            reply_markup=secondary_menu()
        )

    elif data == "civil":
        bot.edit_message_text(
            "🏗️ الهندسة المدنية\n\nاختر المادة أو الخدمة:",
            chat_id,
            message_id,
            reply_markup=civil_menu()
        )

    elif data == "geology":
        bot.edit_message_text(
            "🪨 الهندسة الجيولوجية\n\nاختر المادة أو الخدمة:",
            chat_id,
            message_id,
            reply_markup=geology_menu()
        )

    elif data == "petroleum":
        bot.edit_message_text(
            "🛢️ هندسة النفط\n\nاختر المجال:",
            chat_id,
            message_id,
            reply_markup=petroleum_menu()
        )

    elif data == "electrical":
        bot.edit_message_text(
            "⚡ الهندسة الكهربائية\n\nاختر المجال:",
            chat_id,
            message_id,
            reply_markup=electrical_menu()
        )

    # =========================
    # SECONDARY SCHOOL
    # =========================

    elif data == "secondary_notes":
        text = """
📚 مناهج وملخصات الشهادة الثانوية

📘 ثالثة ثانوي - القسم العلمي

🧮 رياضيات علمي:
https://drive.google.com/file/d/1ThvdAywO6RhDcykaQm6sagft-vy5Y8a2/view?usp=drivesdk

سيتم إضافة باقي المواد تدريجيًا بإذن الله.
"""
        bot.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=back_menu(),
            disable_web_page_preview=True
        )

    elif data == "secondary_science":
        text = """
📘 القسم العلمي - ثالثة ثانوي

🧮 رياضيات علمي:
https://drive.google.com/file/d/1ThvdAywO6RhDcykaQm6sagft-vy5Y8a2/view?usp=drivesdk

سيتم إضافة الفيزياء والكيمياء والأحياء وباقي المواد تدريجيًا بإذن الله.
"""
        bot.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=back_menu(),
            disable_web_page_preview=True
        )

    elif data == "secondary_literary":
        bot.edit_message_text(
            "📗 القسم الأدبي\n\nسيتم إضافة ملفات القسم الأدبي قريبًا بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    elif data == "secondary_exams":
        bot.edit_message_text(
            "📝 أسئلة امتحانات الشهادة الثانوية\n\nسيتم إضافة الأسئلة السابقة قريبًا بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    elif data == "secondary_courses":
        bot.edit_message_text(
            "🎥 كورسات وشرح الشهادة الثانوية\n\nسيتم إضافة الشروحات والكورسات قريبًا بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    # =========================
    # CIVIL ENGINEERING
    # =========================

    elif data == "civil_syllabus":
        text = """
📚 مناهج وملخصات الهندسة المدنية

🧱 خواص مواد CE133:
https://drive.google.com/file/d/1gpgq8yERZvk9X3rTSQoB6g-6HusfN9LT/view?usp=drivesdk

🚗 ترانس CE311:
https://drive.google.com/file/d/1FNU8Sxvjqeb9Gz_fD_fsW1dCeI9HNkyx/view?usp=drivesdk

💧 فلود 1 CE221:
https://drive.google.com/file/d/1GM-Pvf9QDmOdaGyXvJJjW3UyLh2K-Lg8/view?usp=drivesdk

📏 مساحة 1:
https://drive.google.com/file/d/1xWiBFkdIqwh5kIwvWbGneApesv5vgn9K/view?usp=drivesdk

📐 تحليل إنشائي 2 CE303:
https://drive.google.com/file/d/1adZECZXZpD99P7zT-DIom8N_1IXfXGYi/view?usp=drivesdk

🌱 سويل 1 CE342:
https://drive.google.com/file/d/1xiUoWYVH1UJKsTTU_RAXA7wEXMNF8Xpc/view?usp=drivesdk
"""
        bot.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=back_menu(),
            disable_web_page_preview=True
        )

    elif data == "civil_ce133":
        text = """
🧱 خواص مواد CE133

رابط الملف:
https://drive.google.com/file/d/1gpgq8yERZvk9X3rTSQoB6g-6HusfN9LT/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data == "civil_ce311":
        text = """
🚗 ترانس CE311

رابط الملف:
https://drive.google.com/file/d/1FNU8Sxvjqeb9Gz_fD_fsW1dCeI9HNkyx/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data == "civil_ce221":
        text = """
💧 فلود 1 CE221

رابط الملف:
https://drive.google.com/file/d/1GM-Pvf9QDmOdaGyXvJJjW3UyLh2K-Lg8/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data == "civil_survey1":
        text = """
📏 مساحة 1

رابط الملف:
https://drive.google.com/file/d/1xWiBFkdIqwh5kIwvWbGneApesv5vgn9K/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data == "civil_ce303":
        text = """
📐 تحليل إنشائي 2 CE303

رابط الملف:
https://drive.google.com/file/d/1adZECZXZpD99P7zT-DIom8N_1IXfXGYi/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data == "civil_ce342":
        text = """
🌱 سويل 1 CE342

رابط الملف:
https://drive.google.com/file/d/1xiUoWYVH1UJKsTTU_RAXA7wEXMNF8Xpc/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    # =========================
    # GEOLOGY ENGINEERING
    # =========================

    elif data == "geo_syllabus":
        text = """
📚 مناهج وملخصات الهندسة الجيولوجية

🧪 جيوكيمياء - جزئية النصفي:
https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk

سيتم إضافة باقي مواد الجيولوجيا تدريجيًا بإذن الله.
"""
        bot.edit_message_text(
            text,
            chat_id,
            message_id,
            reply_markup=back_menu(),
            disable_web_page_preview=True
        )

    elif data == "geo_geochemistry":
        text = """
🧪 جيوكيمياء - جزئية النصفي

رابط الملف:
https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), disable_web_page_preview=True)

    elif data in ["geo_general", "geo_maps", "geo_rocks"]:
        bot.edit_message_text(
            "🪨 سيتم إضافة هذا المحتوى قريبًا بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    # =========================
    # OTHER SECTIONS
    # =========================

    elif data == "groups":
        text = """
👥 روابط القروبات

🎒 الشهادة الثانوية:
ضع الرابط هنا

🏗️ الهندسة المدنية:
ضع الرابط هنا

🪨 الهندسة الجيولوجية:
ضع الرابط هنا

🛢️ هندسة النفط:
ضع الرابط هنا

⚡ الهندسة الكهربائية:
ضع الرابط هنا
"""
        bot.edit_message_text(
            text,
            chat_id,
            message_id,
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
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    else:
        bot.edit_message_text(
            "📚 سيتم إضافة الملفات والأسئلة والملخصات هنا قريبًا بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )


# =========================
# FLASK ROUTES
# =========================

@app.route("/")
def home():
    return "Libyan Student Guide Bot is running."


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)

        print("Raw update:", json_string)

        if update.message and update.message.text:
            text = update.message.text.strip()
            chat_id = update.message.chat.id

            print("Message text:", text)

            if text.startswith("/start"):
                bot.send_message(chat_id, welcome_text(), reply_markup=main_menu())

            elif text.startswith("/help"):
                bot.send_message(chat_id, help_text())

        elif update.callback_query:
            print("Callback received:", update.callback_query.data)
            handle_buttons(update.callback_query)

        print("Update received and processed")

    except Exception as e:
        print("Webhook error:", repr(e))

    return "OK", 200


# =========================
# SET WEBHOOK
# =========================

bot.remove_webhook()
bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
print("Webhook set to:", f"{WEBHOOK_URL}/webhook")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
