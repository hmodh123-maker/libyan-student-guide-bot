import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get("PORT", 10000))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")


def main_menu():
    keyboard = [
        [InlineKeyboardButton("🎒 الشهادة الثانوية", callback_data="secondary")],
        [InlineKeyboardButton("🏗️ الهندسة المدنية", callback_data="civil")],
        [InlineKeyboardButton("🪨 الجيولوجيا", callback_data="geology")],
        [InlineKeyboardButton("🛢️ هندسة النفط", callback_data="petroleum")],
        [InlineKeyboardButton("⚡ الهندسة الكهربائية", callback_data="electrical")],
        [InlineKeyboardButton("👥 روابط القروبات", callback_data="groups")],
        [InlineKeyboardButton("☎️ تواصل مع الإدارة", callback_data="contact")],
    ]
    return InlineKeyboardMarkup(keyboard)


def back_menu():
    keyboard = [
        [InlineKeyboardButton("🔙 رجوع للقائمة الرئيسية", callback_data="main")]
    ]
    return InlineKeyboardMarkup(keyboard)


def secondary_menu():
    keyboard = [
        [InlineKeyboardButton("📘 القسم العلمي", callback_data="secondary_science")],
        [InlineKeyboardButton("📗 القسم الأدبي", callback_data="secondary_literary")],
        [InlineKeyboardButton("📝 أسئلة امتحانات سابقة", callback_data="secondary_exams")],
        [InlineKeyboardButton("📚 ملخصات ومناهج", callback_data="secondary_notes")],
        [InlineKeyboardButton("🎥 كورسات وشرح", callback_data="secondary_courses")],
        [InlineKeyboardButton("🔙 رجوع", callback_data="main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def civil_menu():
    keyboard = [
        [InlineKeyboardButton("🧱 خواص مواد CE133", callback_data="civil_ce133")],
        [InlineKeyboardButton("📐 تحليل إنشائي CE203", callback_data="civil_ce203")],
        [InlineKeyboardButton("🚗 هندسة النقل CE311", callback_data="civil_ce311")],
        [InlineKeyboardButton("🚰 الهندسة الصحية", callback_data="civil_sanitary")],
        [InlineKeyboardButton("📚 مناهج القسم", callback_data="civil_syllabus")],
        [InlineKeyboardButton("📝 أسئلة امتحانات", callback_data="civil_exams")],
        [InlineKeyboardButton("🔙 رجوع", callback_data="main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def geology_menu():
    keyboard = [
        [InlineKeyboardButton("🌍 جيولوجيا عامة", callback_data="geo_general")],
        [InlineKeyboardButton("🗺️ خرائط جيولوجية", callback_data="geo_maps")],
        [InlineKeyboardButton("🪨 الصخور والمعادن", callback_data="geo_rocks")],
        [InlineKeyboardButton("🛢️ جيولوجيا النفط", callback_data="geo_petroleum")],
        [InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="geo_exams")],
        [InlineKeyboardButton("🔙 رجوع", callback_data="main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def petroleum_menu():
    keyboard = [
        [InlineKeyboardButton("🕳️ Drilling", callback_data="pet_drilling")],
        [InlineKeyboardButton("🛢️ Reservoir", callback_data="pet_reservoir")],
        [InlineKeyboardButton("⚙️ Production", callback_data="pet_production")],
        [InlineKeyboardButton("📈 Well Logging", callback_data="pet_logging")],
        [InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="pet_exams")],
        [InlineKeyboardButton("🔙 رجوع", callback_data="main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def electrical_menu():
    keyboard = [
        [InlineKeyboardButton("🔌 Circuits", callback_data="elec_circuits")],
        [InlineKeyboardButton("⚙️ Machines", callback_data="elec_machines")],
        [InlineKeyboardButton("🏭 Power Systems", callback_data="elec_power")],
        [InlineKeyboardButton("📟 Electronics", callback_data="elec_electronics")],
        [InlineKeyboardButton("📝 أسئلة وملخصات", callback_data="elec_exams")],
        [InlineKeyboardButton("🔙 رجوع", callback_data="main")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(text, reply_markup=main_menu())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
طريقة استخدام البوت:

اضغط /start لفتح القائمة الرئيسية.
ثم اختر القسم المطلوب من الأزرار.

لإرسال ملفات أو أسئلة امتحانات للإضافة:
راسل الإدارة.
"""
    await update.message.reply_text(text)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "main":
        await query.edit_message_text(
            "🎓 القائمة الرئيسية\n\nاختر القسم المطلوب:",
            reply_markup=main_menu()
        )

    elif data == "secondary":
        await query.edit_message_text(
            "🎒 الشهادة الثانوية\n\nاختر القسم أو الخدمة:",
            reply_markup=secondary_menu()
        )

    elif data == "civil":
        await query.edit_message_text(
            "🏗️ الهندسة المدنية\n\nاختر المادة أو الخدمة:",
            reply_markup=civil_menu()
        )

    elif data == "geology":
        await query.edit_message_text(
            "🪨 الجيولوجيا\n\nاختر القسم:",
            reply_markup=geology_menu()
        )

    elif data == "petroleum":
        await query.edit_message_text(
            "🛢️ هندسة النفط\n\nاختر المجال:",
            reply_markup=petroleum_menu()
        )

    elif data == "electrical":
        await query.edit_message_text(
            "⚡ الهندسة الكهربائية\n\nاختر المجال:",
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
        await query.edit_message_text(text, reply_markup=back_menu())

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
        await query.edit_message_text(text, reply_markup=back_menu())

    elif data.startswith("secondary_"):
        await query.edit_message_text(
            "🎒 سيتم إضافة محتوى الشهادة الثانوية هنا قريبًا بإذن الله.",
            reply_markup=back_menu()
        )

    else:
        await query.edit_message_text(
            "📚 سيتم إضافة الملفات والأسئلة والملخصات هنا قريبًا بإذن الله.",
            reply_markup=back_menu()
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    if WEBHOOK_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
        )
    else:
        app.run_polling()


if __name__ == "__main__":
    main()
