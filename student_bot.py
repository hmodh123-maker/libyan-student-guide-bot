import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
import logging

# ====================== CONFIG ======================
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "").strip().rstrip("/")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN غير موجود في متغيرات Render! أضفه في Dashboard.")
if not WEBHOOK_URL:
    raise ValueError("❌ WEBHOOK_URL غير موجود! أضف https://اسم-مشروعك.onrender.com")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Logging لـ Render Dashboard
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ====================== MENUS ======================
def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary"))
    markup.add(InlineKeyboardButton("📖 الإعدادية", callback_data="preparatory"))
    markup.add(InlineKeyboardButton("🏗️ الهندسة المدنية", callback_data="civil_levels"))
    markup.add(InlineKeyboardButton("🛢️ هندسة النفط", callback_data="petroleum"))
    markup.add(InlineKeyboardButton("🪨 الهندسة الجيولوجية", callback_data="geology"))
    markup.add(InlineKeyboardButton("⚡ الهندسة الكهربائية", callback_data="electrical"))
    markup.add(InlineKeyboardButton("💻 هندسة الحاسوب", callback_data="computer"))
    markup.add(InlineKeyboardButton("📊 كلية الاقتصاد", callback_data="economics"))
    markup.add(InlineKeyboardButton("💾 كلية تقنية المعلومات (IT)", callback_data="it_college"))
    markup.add(InlineKeyboardButton("💊 كلية الصيدلة", callback_data="pharmacy"))
    markup.add(InlineKeyboardButton("👥 الكليات البشرية", callback_data="humanities"))
    markup.add(InlineKeyboardButton("🌍 كلية اللغات", callback_data="languages"))
    markup.add(InlineKeyboardButton("👥 روابط القروبات", callback_data="groups"))
    markup.add(InlineKeyboardButton("☎️ تواصل مع الإدارة", callback_data="contact"))
    return markup


def back_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main"))
    return markup


def back_to_civil_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 رجوع لقائمة المستويات", callback_data="civil_levels"))
    markup.add(InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main"))
    return markup


def secondary_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📘 القسم العلمي", callback_data="secondary_science"))
    markup.add(InlineKeyboardButton("📗 القسم الأدبي", callback_data="secondary_literary"))
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="secondary_notes"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات سابقة", callback_data="secondary_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات وشرح", callback_data="secondary_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def preparatory_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📘 الصف الثالث إعدادي", callback_data="prep_3"))
    markup.add(InlineKeyboardButton("📗 الصف الثاني إعدادي", callback_data="prep_2"))
    markup.add(InlineKeyboardButton("📕 الصف الأول إعدادي", callback_data="prep_1"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def civil_levels_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🧱 مستوى 100", callback_data="civil_lvl_100"))
    markup.add(InlineKeyboardButton("📐 مستوى 200", callback_data="civil_lvl_200"))
    markup.add(InlineKeyboardButton("💧 مستوى 300", callback_data="civil_lvl_300"))
    markup.add(InlineKeyboardButton("🏗️ مستوى 400", callback_data="civil_lvl_400"))
    markup.add(InlineKeyboardButton("🚗 مستوى 500", callback_data="civil_lvl_500"))
    markup.add(InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main"))
    return markup


def geology_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات الجيولوجيا", callback_data="geo_syllabus"))
    markup.add(InlineKeyboardButton("🧪 جيوكيمياء - جزئية النصفي", callback_data="geo_geochemistry"))
    markup.add(InlineKeyboardButton("🌍 جيولوجيا عامة", callback_data="geo_general"))
    markup.add(InlineKeyboardButton("🗺️ خرائط جيولوجية", callback_data="geo_maps"))
    markup.add(InlineKeyboardButton("🪨 الصخور والمعادن", callback_data="geo_rocks"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def petroleum_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🕳️ Drilling", callback_data="pet_drilling"))
    markup.add(InlineKeyboardButton("🛢️ Reservoir", callback_data="pet_reservoir"))
    markup.add(InlineKeyboardButton("⚙️ Production", callback_data="pet_production"))
    markup.add(InlineKeyboardButton("📈 Well Logging", callback_data="pet_logging"))
    markup.add(InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="pet_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def electrical_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🔌 Circuits", callback_data="elec_circuits"))
    markup.add(InlineKeyboardButton("⚙️ Machines", callback_data="elec_machines"))
    markup.add(InlineKeyboardButton("🏭 Power Systems", callback_data="elec_power"))
    markup.add(InlineKeyboardButton("📟 Electronics", callback_data="elec_electronics"))
    markup.add(InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="elec_exams"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def computer_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="comp_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="comp_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="comp_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def economics_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="eco_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="eco_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="eco_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def it_college_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="it_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="it_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="it_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def pharmacy_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="pharm_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="pharm_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="pharm_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def humanities_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="hum_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="hum_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="hum_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


def languages_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📚 مناهج وملخصات", callback_data="lang_syllabus"))
    markup.add(InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="lang_exams"))
    markup.add(InlineKeyboardButton("🎥 كورسات", callback_data="lang_courses"))
    markup.add(InlineKeyboardButton("🔙 رجوع", callback_data="main"))
    return markup


# ====================== TEXTS (HTML) ======================
def welcome_text():
    return """
<b>✨ مرحباً بك في دليل الطالب الليبي الأرقى 🎓📚</b>

🚀 <b>Explorer شامل</b> يجمع لك كل المواد الدراسية في مكان واحد:
• الثانوية + الإعدادية
• كل كليات الهندسة
• الاقتصاد + IT + الصيدلة + البشري + اللغات

👇 <b>اختر القسم أو الكلية وابدأ التصفح الآن</b>
"""


def help_text():
    return """
<b>💡 دليل الاستخدام السريع:</b>
• /start → القائمة الرئيسية في أي وقت
• اضغط على الأزرار التفاعلية
• كل الروابط تفتح مباشرة على Google Drive

📥 <b>تريد المساهمة؟</b> ارسل ملفاتك عبر "تواصل مع الإدارة"
"""


# ====================== COMMANDS ======================
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        welcome_text(),
        reply_markup=main_menu(),
        parse_mode="HTML",
        disable_web_page_preview=True
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.chat.id, help_text(), parse_mode="HTML")


# ====================== CALLBACK HANDLER ======================
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    try:
        bot.answer_callback_query(call.id)
    except:
        pass

    data = call.data
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    logger.info(f"📩 Callback received: {data}")

    # القوائم الرئيسية
    if data == "secondary":
        bot.edit_message_text("🎒 <b>قسم الشهادة الثانوية</b>\n\nاختر القسم الدراسي أو نوع الخدمة المطلوبة:", chat_id, message_id, reply_markup=secondary_menu(), parse_mode="HTML")
    elif data == "preparatory":
        bot.edit_message_text("📖 <b>قسم الإعدادية</b>\n\nاختر الصف الدراسي:", chat_id, message_id, reply_markup=preparatory_menu(), parse_mode="HTML")
    elif data == "civil_levels":
        bot.edit_message_text("🏗️ <b>كلية الهندسة - قسم الهندسة المدنية</b>\n\n👇 اختر المستوى الدراسي:", chat_id, message_id, reply_markup=civil_levels_menu(), parse_mode="HTML")
    elif data == "geology":
        bot.edit_message_text("🪨 <b>قسم الهندسة الجيولوجية</b>\n\nاختر المادة أو الخدمة:", chat_id, message_id, reply_markup=geology_menu(), parse_mode="HTML")
    elif data == "petroleum":
        bot.edit_message_text("🛢️ <b>قسم هندسة النفط</b>\n\nاختر المجال:", chat_id, message_id, reply_markup=petroleum_menu(), parse_mode="HTML")
    elif data == "electrical":
        bot.edit_message_text("⚡ <b>قسم الهندسة الكهربائية</b>\n\nاختر المجال الفرعي:", chat_id, message_id, reply_markup=electrical_menu(), parse_mode="HTML")
    elif data == "computer":
        bot.edit_message_text("💻 <b>هندسة الحاسوب</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=computer_menu(), parse_mode="HTML")
    elif data == "economics":
        bot.edit_message_text("📊 <b>كلية الاقتصاد</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=economics_menu(), parse_mode="HTML")
    elif data == "it_college":
        bot.edit_message_text("💾 <b>كلية تقنية المعلومات (IT)</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=it_college_menu(), parse_mode="HTML")
    elif data == "pharmacy":
        bot.edit_message_text("💊 <b>كلية الصيدلة</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=pharmacy_menu(), parse_mode="HTML")
    elif data == "humanities":
        bot.edit_message_text("👥 <b>الكليات البشرية</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=humanities_menu(), parse_mode="HTML")
    elif data == "languages":
        bot.edit_message_text("🌍 <b>كلية اللغات</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=languages_menu(), parse_mode="HTML")

    # مستويات الهندسة المدنية (كاملة بنفس الروابط الأصلية)
    elif data == "civil_lvl_100":
        text = """🧱 <b>الهندسة المدنية - مستوى 100</b>

📝 <b>المواد المتاحة حالياً:</b>

🗂️ <b>خواص مواد (CE133):</b> <a href="https://drive.google.com/file/d/1gpgq8yERZvk9X3rTSQoB6g-6HusfN9LT/view?usp=drivesdk">فتح المجلد</a>

📝 <b>كتابة تقارير (GH152):</b> <a href="https://drive.google.com/drive/folders/1IqkfVOSphPkES4HCJgGn3o8m9RE0mlAw?usp=drive_link">فتح المجلد</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data == "civil_lvl_200":
        text = """📐 <b>الهندسة المدنية - مستوى 200</b>

📝 <b>المواد المتاحة حالياً:</b>

💧 <b>فلود 1 (CE221):</b> <a href="https://drive.google.com/file/d/1GM-Pvf9QDmOdaGyXvJJjW3UyLh2K-Lg8/view?usp=drivesdk">فتح المجلد</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data == "civil_lvl_300":
        text = """💧 <b>الهندسة المدنية - مستوى 300</b>

📝 <b>المواد المتاحة حالياً حسب الشعب:</b>

📐 <b>تحليل إنشائي 1 (شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/1MW6cp8JzFS9TWdS2rrFzquv2aNIFgYYD?usp=drive_link">فتح المجلد</a>

📐 <b>تحليل إنشائي 2 (CE303):</b> <a href="https://drive.google.com/file/d/1adZECZXZpD99P7zT-DIom8N_1IXfXGYi/view?usp=drivesdk">فتح المجلد</a>

🚗 <b>ترانس (CE311):</b> <a href="https://drive.google.com/file/d/1FNU8Sxvjqeb9Gz_fD_fsW1dCeI9HNkyx/view?usp=drivesdk">فتح المجلد</a>

💧 <b>هيدرولوجيا (CE325 - شعبة المياه):</b> <a href="https://drive.google.com/drive/folders/14QBqY2p96-GbbDnFf3kHuJiioCr9SDIb?usp=drive_link">فتح المجلد</a>

💧 <b>فلود 2 (CE322 - شعبة المياه):</b> <a href="https://drive.google.com/drive/folders/19byfltCT13ebw9GCEEK53HZ0VGuZD6e1?usp=drive_link">فتح المجلد</a>

🌱 <b>سويل 1 (CE342):</b> <a href="https://drive.google.com/file/d/1xiUoWYVH1UJKsTTU_RAXA7wEXMNF8Xpc/view?usp=drivesdk">فتح المجلد</a>

📏 <b>مساحة 1:</b> <a href="https://drive.google.com/file/d/1xWiBFkdIqwh5kIwvWbGneApesv5vgn9K/view?usp=drivesdk">فتح المجلد</a>

📏 <b>مساحة 2 (شعبة الطرق):</b> <a href="https://drive.google.com/drive/folders/1KP4R9X1L3usjzU1cpbIGLrP5kSWCukle?usp=drive_link">فتح المجلد</a>

🏥 <b>صحية 1 (CE372 - شعبة المياه):</b> <a href="https://drive.google.com/drive/folders/1mpZXnVGn-g8nqUWnpw3tCy0DrUV4_DW9?usp=drive_link">فتح المجلد</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data == "civil_lvl_400":
        text = """🏗️ <b>الهندسة المدنية - مستوى 400</b>

📝 <b>المواد المتاحة حالياً حسب الشعب:</b>

📐 <b>تحليل إنشائي (CE403 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/1oUE7FjoPgObWbwJ8vmGi6rcB7JDHTduT?usp=drive_link">فتح المجلد</a>

🧱 <b>كونكريت 2 (CE405 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/1D7Km1YxYo2uqRE2WqV9LgPALng1HGiLm?usp=drive_link">فتح المجلد</a>

🏗️ <b>ستيل 2 (CE407 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/1hPtxESsngT1AUc9OW16QXF3iwflQ2U74?usp=drive_link">فتح المجلد</a>

🚗 <b>رصف طرق (CE414 - شعبة الطرق):</b> <a href="https://drive.google.com/drive/folders/1hgdRsP6osFpc70AcJQX0lidjBsHaHq3N?usp=drive_link">فتح المجلد</a>

🚗 <b>طرق (CE416 - شعبة الطرق):</b> <a href="https://drive.google.com/drive/folders/1oaKd7NkaEiB_-jxSvlOIZPAXGRT2j9TE?usp=drive_link">فتح المجلد</a>

🌱 <b>تربة 2 (CE442 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/126fextvm80VLf7pyOI2p5cf0ZwioYFp9?usp=drive_link">فتح المجلد</a>

🏢 <b>بلدنق / مباني (CE462 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/14st9edYJWUIMLIwEqJfiH2yOPfCBAIy_?usp=drive_link">فتح المجلد</a>

📄 <b>مواصفات وعقود البناء (CE463 - شعبة الإنشاءات):</b> <a href="https://drive.google.com/drive/folders/1GcLy8xkYtmrKDHUcW2USOGecxVMuZzYr?usp=drive_link">فتح المجلد</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data == "civil_lvl_500":
        text = """🚗 <b>الهندسة المدنية - مستوى 500</b>

📝 <b>المواد المتاحة حالياً حسب الشعب:</b>

🛣️ <b>شعبة الطرق (CE512):</b> <a href="https://drive.google.com/drive/folders/1OopY5wyAvXMi7dLs8ZG1so77Bnv9t9f4?usp=drive_link">فتح المجلد</a>

🚦 <b>هندسة المرور (CE513):</b> <a href="https://drive.google.com/drive/folders/1oOccHRiV8PanIAms7jdAEuGP_kVV350p?usp=drive_link">فتح المجلد</a>

⚙️ <b>مادة كود الكلية المتخصصة (CE597T):</b> <a href="https://drive.google.com/drive/folders/1hy2gPFAr9nVm3THPJg1IFPEFxhx5rnHr?usp=drive_link">فتح المجلد</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="HTML", disable_web_page_preview=True)

    # الشهادة الثانوية
    elif data == "secondary_notes":
        text = """📚 <b>مناهج وملخصات الشهادة الثانوية</b>

📘 <b>ثالثة ثانوي - القسم العلمي</b>

🧮 <b>رياضيات علمي:</b> <a href="https://drive.google.com/file/d/1ThvdAywO6RhDcykaQm6sagft-vy5Y8a2/view?usp=drivesdk">رابط شيت مادة الرياضيات</a>

💡 سيتم إضافة باقي المواد تدريجيًا."""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data in ["secondary_science", "secondary_literary", "secondary_exams", "secondary_courses"]:
        bot.edit_message_text("📘 <b>القسم قيد التطوير</b>\n\nسيتم إضافة المحتوى قريباً بإذن الله.", chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")

    # جيولوجيا
    elif data == "geo_syllabus":
        text = """📚 <b>مناهج وملخصات الهندسة الجيولوجية</b>

🧪 <b>جيوكيمياء - جزئية النصفي:</b> <a href="https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk">فتح الملف</a>

💡 سيتم إضافة المزيد تباعاً."""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data == "geo_geochemistry":
        text = """🧪 <b>مادة الجيوكيمياء - جزئية النصفي</b>

<a href="https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk">رابط التحميل المباشر</a>"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML", disable_web_page_preview=True)

    elif data in ["geo_general", "geo_maps", "geo_rocks"]:
        bot.edit_message_text("🪨 <b>تنبيه قسم الجيولوجيا</b>\n\nالمحتوى جارٍ تجهيزه وسيتم توفيره قريباً.", chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")

    # باقي الأقسام (قيد التطوير)
    elif data in ["pet_drilling", "pet_reservoir", "pet_production", "pet_logging", "pet_exams",
                  "elec_circuits", "elec_machines", "elec_power", "elec_electronics", "elec_exams",
                  "prep_1", "prep_2", "prep_3",
                  "comp_syllabus", "comp_exams", "comp_courses",
                  "eco_syllabus", "eco_exams", "eco_courses",
                  "it_syllabus", "it_exams", "it_courses",
                  "pharm_syllabus", "pharm_exams", "pharm_courses",
                  "hum_syllabus", "hum_exams", "hum_courses",
                  "lang_syllabus", "lang_exams", "lang_courses"]:
        bot.edit_message_text("🔄 <b>هذا القسم قيد التطوير</b>\n\nسيتم رفع الشيتات والملخصات قريباً جداً.", chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")

    # روابط القروبات + تواصل
    elif data == "groups":
        text = """👥 <b>الدليل الشامل لروابط قروبات التليجرام والواتساب</b>

🎒 <b>الشهادة الثانوية:</b> [ضع الرابط هنا]
🏗️ <b>الهندسة المدنية:</b> [ضع الرابط هنا]
🪨 <b>الهندسة الجيولوجية:</b> [ضع الرابط هنا]
🛢️ <b>هندسة النفط:</b> [ضع الرابط هنا]
⚡ <b>الهندسة الكهربائية:</b> [ضع الرابط هنا]"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")

    elif data == "contact":
        text = """☎️ <b>تواصل المباشر مع إدارة دليل الطالب الليبي</b>

مرحباً بك، يسعدنا تواصلك معنا.

📬 <b>معرف الإدارة:</b> @hmodh123

📋 <b>يرجى عند إرسال مساهمتك:</b>
1️⃣ اسم التخصص والقسم
2️⃣ اسم المادة وكودها
3️⃣ نوع الملف
4️⃣ إرفاق الملف أو رابط Google Drive"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")

    # رجوع للرئيسية
    elif data == "main":
        bot.edit_message_text("🗂️ <b>القائمة الرئيسية</b>\n\nاختر القسم أو الكلية:", chat_id, message_id, reply_markup=main_menu(), parse_mode="HTML")

    else:
        bot.edit_message_text("📚 <b>قسم قيد التطوير</b>\n\nسيتم إضافة المحتوى قريباً.", chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")


# ====================== FLASK ======================
@app.route("/")
def home():
    return "✅ Libyan Student Guide Bot is LIVE on Render!"


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        logger.info("✅ Update processed successfully")
    except Exception as e:
        logger.error(f"❌ Webhook Error: {e}")
    return "OK", 200


# ====================== SET WEBHOOK ======================
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    logger.info(f"✅ Webhook set successfully to: {WEBHOOK_URL}/webhook")

    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
