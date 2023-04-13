import re, os

id_pattern = re.compile(r'^.\d+$')

API_ID = os.environ.get("API_ID", "29874670")

API_HASH = os.environ.get("API_HASH", "09568c14cf0b998cd84d8eedef29dffb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6162348164:AAHriUkgrozAfz2jWdePYtHd7VilTbzPFSo")

FORCE_SUB = os.environ.get("FORCE_SUB", "PilotControl")

DB_NAME = os.environ.get("DB_NAME","pyro-botz")

DB_URL = os.environ.get("DB_URL","mongodb+srv://VsTech:VsTech309@cluster0.dmm01ai.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/04d08445dce68c9a57b25.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '889514276 1493545483').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
