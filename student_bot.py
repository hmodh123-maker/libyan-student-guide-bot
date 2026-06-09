Import os

import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from flask import Flask, request

import logging



# ====================== CONFIG ======================

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "").strip().rstrip("/")



if not BOT_TOKEN:

raise ValueError("❌ BOT_TOKEN غير موجود في متغيرات Render!")

if not WEBHOOK_URL:

raise ValueError("❌ WEBHOOK_URL غير موجود!")



bot = telebot.TeleBot(BOT_TOKEN, threaded=False) # ← هذا التعديل المهم

app = Flask(__name__)



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



# ====================== TEXTS ======================

def welcome_text():

return """

<b>✨ مرحباً بك في دليل الطالب الليبي الأرقى 🎓📚</b>



🚀 <b>Explorer شامل</b> يجمع لك كل المواد الدراسية في مكان واحد.



👇 <b>اختر القسم أو الكلية وابدأ التصفح الآن</b>

"""



def help_text():

return """

<b>💡 دليل الاستخدام:</b>

• /start → القائمة الرئيسية

• اضغط على الأزرار

• كل الروابط تفتح مباشرة

"""



# ====================== COMMANDS ======================

@bot.message_handler(commands=["start"])

def start(message):

bot.send_message(message.chat.id, welcome_text(), reply_markup=main_menu(), parse_mode="HTML", disable_web_page_preview=True)



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



logger.info(f"Callback: {data}")



# باقي الكود كما هو (الـ if conditions) - لم أغيّر فيه شيئاً

if data == "secondary":

bot.edit_message_text("🎒 <b>قسم الشهادة الثانوية</b>\n\nاختر القسم الدراسي:", chat_id, message_id, reply_markup=secondary_menu(), parse_mode="HTML")

elif data == "preparatory":

bot.edit_message_text("📖 <b>قسم الإعدادية</b>\n\nاختر الصف:", chat_id, message_id, reply_markup=preparatory_menu(), parse_mode="HTML")

elif data == "civil_levels":

bot.edit_message_text("🏗️ <b>الهندسة المدنية</b>\n\nاختر المستوى:", chat_id, message_id, reply_markup=civil_levels_menu(), parse_mode="HTML")

elif data == "geology":

bot.edit_message_text("🪨 <b>الهندسة الجيولوجية</b>\n\nاختر المادة:", chat_id, message_id, reply_markup=geology_menu(), parse_mode="HTML")

elif data == "petroleum":

bot.edit_message_text("🛢️ <b>هندسة النفط</b>\n\nاختر المجال:", chat_id, message_id, reply_markup=petroleum_menu(), parse_mode="HTML")

elif data == "electrical":

bot.edit_message_text("⚡ <b>الهندسة الكهربائية</b>\n\nاختر المجال:", chat_id, message_id, reply_markup=electrical_menu(), parse_mode="HTML")

elif data == "computer":

bot.edit_message_text("💻 <b>هندسة الحاسوب</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=computer_menu(), parse_mode="HTML")

elif data == "economics":

bot.edit_message_text("📊 <b>كلية الاقتصاد</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=economics_menu(), parse_mode="HTML")

elif data == "it_college":

bot.edit_message_text("💾 <b>كلية IT</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=it_college_menu(), parse_mode="HTML")

elif data == "pharmacy":

bot.edit_message_text("💊 <b>كلية الصيدلة</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=pharmacy_menu(), parse_mode="HTML")

elif data == "humanities":

bot.edit_message_text("👥 <b>الكليات البشرية</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=humanities_menu(), parse_mode="HTML")

elif data == "languages":

bot.edit_message_text("🌍 <b>كلية اللغات</b>\n\nاختر الخدمة:", chat_id, message_id, reply_markup=languages_menu(), parse_mode="HTML")

elif data == "main":

bot.edit_message_text("🗂️ <b>القائمة الرئيسية</b>", chat_id, message_id, reply_markup=main_menu(), parse_mode="HTML")

else:

bot.edit_message_text("🔄 <b>هذا القسم قيد التطوير</b>\n\nسيتم إضافته قريباً.", chat_id, message_id, reply_markup=back_menu(), parse_mode="HTML")



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

logger.info("Update processed")

except Exception as e:

logger.error(f"Error: {e}")

return "OK", 200



# ====================== SET WEBHOOK ======================

if __name__ == "__main__":

bot.remove_webhook()

bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")

logger.info(f"Webhook set to: {WEBHOOK_URL}/webhook")



port = int(os.getenv("PORT", 10000))

app.run(host="0.0.0.0", port=port) 

