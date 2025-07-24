from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess
import sys
import os

# Token bot dari @BotFather
TOKEN = "7649537068:AAHFR3QUZCtCbI3lqyAu4K9tS04iS40ra34"
PASSWORD = "acdc123"  # Ganti ke password lebih aman jika perlu

# Lokasi proyekmu
FE_PATH = r"C:\Users\Daffaprima\Documents\GitHub\Art-and-Cosmetic-Dental-\Sistem-Operasi\FE"
BE_PATH = r"C:\Users\Daffaprima\Documents\GitHub\Art-and-Cosmetic-Dental-\Sistem-Operasi\BE"

# Fungsi untuk cek password
def is_authorized(args):
    return args and args[0] == PASSWORD

# Perintah untuk nyalakan Frontend
def run_fe():
    subprocess.Popen(["npm", "run", "dev"], cwd=FE_PATH, shell=True)

# Perintah untuk nyalakan Backend
def run_be():
    subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--reload"],
        cwd=BE_PATH,
        shell=True
    )

# Handler untuk /startweb
async def start_web(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(context.args):
        return await update.message.reply_text("❌ Akses ditolak. Password salah.")
    
    try:
        run_be()
        run_fe()
        await update.message.reply_text("✅ Frontend & Backend berhasil dinyalakan.")
    except Exception as e:
        await update.message.reply_text(f"❌ Gagal menyalakan web: {e}")

# Bot setup
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("startweb", start_web))

print("🤖 Bot berjalan... Tekan Ctrl+C untuk berhenti.")
app.run_polling()
