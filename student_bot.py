import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBHOOK_URL = os.environ["WEBHOOK_URL"].strip().rstrip("/")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)


# =========================
# MENUS & MARKUPS
# =========================

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary"))
    markup.add(InlineKeyboardButton("🏗️ الهندسة المدنية (المستويات)", callback_data="civil_levels"))
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


def back_to_civil_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 رجوع لقائمة المستويات", callback_data="civil_levels"))
    markup.add(InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main"))
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


# القائمة الجديدة للمستويات في الهندسة المدنية
def civil_levels_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🧱 مستوى 100", callback_data="civil_lvl_100"))
    markup.add(InlineKeyboardButton("📐 مستوى 200", callback_data="civil_lvl_200"))
    markup.add(InlineKeyboardButton("💧 مستوى 300", callback_data="civil_lvl_300"))
    markup.add(InlineKeyboardButton("🏗️ مستوى 400", callback_data="civil_lvl_400"))
    markup.add(InlineKeyboardButton("🚗 مستوى 500", callback_data="civil_lvl_500"))
    markup.add(InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main"))
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
# TEXTS & MESSAGES
# =========================

def welcome_text():
    return """
✨ أهلاً بك في دليل الطالب الليبي الأرقى 🎓📚

تم تصميم هذا البوت بمظهر عصري ليجمع لك كل ما تحتاجه في مسيرتك الدراسية بكل سهولة وسرعة 🚀

💼 **ماذا يقدم لك البوت؟**
✅ أسئلة امتحانات سابقة دورية
✅ مناهج، ملخصات، وشيتات منسقة
✅ كورسات وشروحات مميزة
✅ روابط قروبات المواد التفاعلية
✅ مراجع وملفات حصرية لكل التخصصات

👇 **اختر القسم المطلوب من الأسفل وابدأ التصفح الآن:**
"""


def help_text():
    return """
💡 **دليل استخدام البوت السريع:**

🔹 اضغط على الأمر /start لإظهار القائمة الرئيسية في أي وقت.
🔹 تنقل بين الأقسام والمستويات عبر الأزرار التفاعلية المرفقة أسفل كل رسالة.

📥 **هل تريد المساهمة وتطوير البوت؟**
إذا كان لديك ملفات، ملخصات، أو أسئلة امتحانات وترغب في إضافتها لتفيد زملائك، يمكنك مراسلة الدعم الفني مباشرة عبر قسم "تواصل مع الإدارة".
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
            "🗂️ **القائمة الرئيسية**\n\nيرجى اختيار القسم أو التخصص المطلوب استكشافه:",
            chat_id,
            message_id,
            reply_markup=main_menu()
        )

    elif data == "secondary":
        bot.edit_message_text(
            "🎒 **قسم الشهادة الثانوية**\n\nاختر القسم الدراسي أو نوع الخدمة المطلوبة:",
            chat_id,
            message_id,
            reply_markup=secondary_menu()
        )

    # ==========================================
    # CIVIL ENGINEERING - LEVELS (NEW STRUCTURE)
    # ==========================================
    elif data == "civil_levels":
        bot.edit_message_text(
            "🏗️ **كلية الهندسة - قسم الهندسة المدنية**\n\nمرحباً بك في الأرشيف المطور للمواد. تم تقسيم المواد حسب مستوياتها الأكاديمية لتسهيل وصولك المباشر:\n\n👇 اختر المستوى الدراسي المُراد تصفحه:",
            chat_id,
            message_id,
            reply_markup=civil_levels_menu()
        )

    elif data == "civil_lvl_100":
        text = """
🧱 **الهندسة المدنية - مواد مستوى 100**

📝 **المواد المتاحة حالياً:**

🗂️ **خواص مواد (CE133):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1gpgq8yERZvk9X3rTSQoB6g-6HusfN9LT/view?usp=drivesdk)

📝 **كتابة تقارير (GH152):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1IqkfVOSphPkES4HCJgGn3o8m9RE0mlAw?usp=drive_link)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "civil_lvl_200":
        text = """
📐 **الهندسة المدنية - مواد مستوى 200**

📝 **المواد المتاحة حالياً:**

💧 **فلود 1 (CE221):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1GM-Pvf9QDmOdaGyXvJJjW3UyLh2K-Lg8/view?usp=drivesdk)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "civil_lvl_300":
        text = """
💧 **الهندسة المدنية - مواد مستوى 300**

📝 **المواد المتاحة حالياً حسب الشعب:**

📐 **تحليل إنشائي 1 (شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1MW6cp8JzFS9TWdS2rrFzquv2aNIFgYYD?usp=drive_link)

📐 **تحليل إنشائي 2 (CE303):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1adZECZXZpD99P7zT-DIom8N_1IXfXGYi/view?usp=drivesdk)

🚗 **ترانس (CE311):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1FNU8Sxvjqeb9Gz_fD_fsW1dCeI9HNkyx/view?usp=drivesdk)

💧 **هيدرولوجيا (CE325 - شعبة المياه):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/14QBqY2p96-GbbDnFf3kHuJiioCr9SDIb?usp=drive_link)

💧 **فلود 2 (CE322 - شعبة المياه):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/19byfltCT13ebw9GCEEK53HZ0VGuZD6e1?usp=drive_link)

🌱 **سويل 1 (CE342):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1xiUoWYVH1UJKsTTU_RAXA7wEXMNF8Xpc/view?usp=drivesdk)

📏 **مساحة 1:**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/file/d/1xWiBFkdIqwh5kIwvWbGneApesv5vgn9K/view?usp=drivesdk)

📏 **مساحة 2 (شعبة الطرق):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1KP4R9X1L3usjzU1cpbIGLrP5kSWCukle?usp=drive_link)

🏥 **صحية 1 (CE372 - شعبة المياه):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1mpZXnVGn-g8nqUWnpw3tCy0DrUV4_DW9?usp=drive_link)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "civil_lvl_400":
        text = """
🏗️ **الهندسة المدنية - مواد مستوى 400**

📝 **المواد المتاحة حالياً حسب الشعب:**

📐 **تحليل إنشائي (CE403 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1oUE7FjoPgObWbwJ8vmGi6rcB7JDHTduT?usp=drive_link)

🧱 **كونكريت 2 (CE405 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1D7Km1YxYo2uqRE2WqV9LgPALng1HGiLm?usp=drive_link)

🏗️ **ستيل 2 (CE407 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1hPtxESsngT1AUc9OW16QXF3iwflQ2U74?usp=drive_link)

🚗 **رصف طرق (CE414 - شعبة الطرق):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1hgdRsP6osFpc70AcJQX0lidjBsHaHq3N?usp=drive_link)

🚗 **طرق (CE416 - شعبة الطرق):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1oaKd7NkaEiB_-jxSvlOIZPAXGRT2j9TE?usp=drive_link)

🌱 **تربة 2 (CE442 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/126fextvm80VLf7pyOI2p5cf0ZwioYFp9?usp=drive_link)

🏢 **بلدنق / مباني (CE462 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/14st9edYJWUIMLIwEqJfiH2yOPfCBAIy_?usp=drive_link)

📄 **مواصفات وعقود البناء (CE463 - شعبة الإنشاءات):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1GcLy8xkYtmrKDHUcW2USOGecxVMuZzYr?usp=drive_link)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "civil_lvl_500":
        text = """
🚗 **الهندسة المدنية - مواد مستوى 500**

📝 **المواد المتاحة حالياً حسب الشعب:**

🛣️ **شعبة الطرق (CE512):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1OopY5wyAvXMi7dLs8ZG1so77Bnv9t9f4?usp=drive_link)

🚦 **هندسة المرور (CE513):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1oOccHRiV8PanIAms7jdAEuGP_kVV350p?usp=drive_link)

⚙️ **مادة كود الكلية المتخصصة (CE597T):**
🌐 [اضغط هنا لفتح مجلد المادة](https://drive.google.com/drive/folders/1hy2gPFAr9nVm3THPJg1IFPEFxhx5rnHr?usp=drive_link)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_to_civil_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "geology":
        bot.edit_message_text(
            "🪨 **قسم الهندسة الجيولوجية**\n\nاختر المادة أو الخدمة المتوفرة في الأرشيف المرفق أدناه:",
            chat_id,
            message_id,
            reply_markup=geology_menu()
        )

    elif data == "petroleum":
        bot.edit_message_text(
            "🛢️ **قسم هندسة النفط**\n\nيرجى تحديد المجال الهندسي المطلوب للوصول لشيتاته وملخصاته:",
            chat_id,
            message_id,
            reply_markup=petroleum_menu()
        )

    elif data == "electrical":
        bot.edit_message_text(
            "⚡ **قسم الهندسة الكهربائية**\n\nاختر المجال الفرعي لعرض الشروحات والمناهج المتوفرة:",
            chat_id,
            message_id,
            reply_markup=electrical_menu()
        )

    # =========================
    # SECONDARY SCHOOL
    # =========================

    elif data == "secondary_notes":
        text = """
📚 **مناهج وملخصات الشهادة الثانوية**

📘 *ثالثة ثانوي - القسم العلمي*

🧮 **رياضيات علمي:**
🌐 [رابط شيت مادة الرياضيات](https://drive.google.com/file/d/1ThvdAywO6RhDcykaQm6sagft-vy5Y8a2/view?usp=drivesdk)

💡 *تنويه: سيتم إضافة باقي المواد والملخصات تدريجيًا فور توفرها من الإدارة.*
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "secondary_science":
        text = """
📘 **القسم العلمي - ثالثة ثانوي**

🧮 **رياضيات علمي:**
🌐 [رابط شيت مادة الرياضيات](https://drive.google.com/file/d/1ThvdAywO6RhDcykaQm6sagft-vy5Y8a2/view?usp=drivesdk)

💡 *تنويه: سيتم إضافة شروحات وملخصات الفيزياء، الكيمياء، الأحياء، وباقي المواد قريباً جداً.*
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "secondary_literary":
        bot.edit_message_text(
            "📗 **القسم الأدبي - ثالثة ثانوي**\n\nنحن نعمل حالياً على جمع وتنسيق الملفات والملخصات الخاصة بالقسم الأدبي وسيتم رفعها هنا قريباً جداً بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    elif data == "secondary_exams":
        bot.edit_message_text(
            "📝 **أسئلة امتحانات الشهادة الثانوية**\n\nترقبوا إضافة بنك الأسئلة الشامل والامتحانات الوزارية السابقة لكل الأقسام قريباً بإذن الله.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    elif data == "secondary_courses":
        bot.edit_message_text(
            "🎥 **كورسات وفيديوهات شرح الشهادة الثانوية**\n\nسيتم إدراج الروابط التعليمية وسلسلة الشروحات المرئية لأفضل المعلمين قريباً هنا.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    # =========================
    # GEOLOGY ENGINEERING HANDLER
    # =========================

    elif data == "geo_syllabus":
        text = """
📚 **مناهج وملخصات الهندسة الجيولوجية**

🧪 **جيوكيمياء - جزئية النصفي:**
🌐 [اضغط هنا لفتح رابط الملف](https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk)

💡 *سيتم إضافة المزيد من مواد القسم والمستويات تباعاً.*
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data == "geo_geochemistry":
        text = """
🧪 **مادة الجيوكيمياء - جزئية النصفي**

تحميل مباشر عبر قوقل درايف:
🌐 [رابط ملف الجيوكيمياء](https://drive.google.com/file/d/14TnsBIykI8-rbYrNY7wSq-pYvZiTdT6-/view?usp=drivesdk)
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown", disable_web_page_preview=True)

    elif data in ["geo_general", "geo_maps", "geo_rocks"]:
        bot.edit_message_text(
            "🪨 **تنبيه قسم الجيولوجيا**\n\nالمحتوى المختار جارٍ تجهيزه ومراجعته حالياً من قبل الإدارة، وسيتم توفيره قريباً.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )

    # =========================
    # OTHER SECTIONS
    # =========================

    elif data == "groups":
        text = """
👥 **الدليل الشامل لروابط قروبات التليجرام والواتساب**

اضغط على القروب المناسب لتخصصك لمتابعة المناقشات مع زملائك:

🎒 **الشهادة الثانوية:** [ضع الرابط هنا]
🏗️ **الهندسة المدنية:** [ضع الرابط هنا]
🪨 **الهندسة الجيولوجية:** [ضع الرابط هنا]
🛢️ **هندسة النفط:** [ضع الرابط هنا]
⚡ **الهندسة الكهربائية:** [ضع الرابط هنا]
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown")

    elif data == "contact":
        text = """
☎️ **تواصل المباشر مع إدارة دليل الطالب الليبي**

مرحباً بك، يسعدنا تواصلك معنا لإرسال ملفات جديدة، شيتات، أسئلة امتحانات، أو لطلب إضافة قروب للمواد الدراسية.

📬 **معرف الإدارة المباشر:** @hmodh123

📋 **يرجى عند إرسال مساهمتك تزويدنا بالتالي:**
1️⃣ اسم التخصص والقسم (مثال: هندسة مدنية).
2️⃣ اسم المادة وكودها (مثال: كونكريت 2 CE405).
3️⃣ نوع الملف المرسل (شيت، ملخص، امتحان سابق).
4️⃣ إرفاق الملف أو رابط قوقل درايف الخاص به.
"""
        bot.edit_message_text(text, chat_id, message_id, reply_markup=back_menu(), parse_mode="Markdown")

    else:
        bot.edit_message_text(
            "📚 **قسم قيد التطوير**\n\nسيتم إضافة بايات المواد الشيتات والملخصات المتبقية في أقرب وقت ممكن.",
            chat_id,
            message_id,
            reply_markup=back_menu()
        )


# =========================
# FLASK ROUTES
# =========================

@app.route("/")
def home():
    return "Libyan Student Guide Bot is running flawlessly."


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
