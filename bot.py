import subprocess
import sys
import os
import time

# Lokasi proyekmu
FE_PATH = r"C:\Users\Daffaprima\Documents\GitHub\Art-and-Cosmetic-Dental-\Sistem-Operasi\FE"
BE_PATH = r"C:\Users\Daffaprima\Documents\GitHub\Art-and-Cosmetic-Dental-\Sistem-Operasi\BE"

# Inisialisasi global variable process
fe_process = None
be_process = None

# Perintah untuk nyalakan Frontend
def run_fe():
    global fe_process
    print("⚙️ Menyalakan Frontend...")
    fe_process = subprocess.Popen(["npm", "run", "dev"], cwd=FE_PATH, shell=True)

# Perintah untuk nyalakan Backend
def run_be():
    global be_process
    print("⚙️ Menyalakan Backend...")
    be_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--reload"],
        cwd=BE_PATH,
        shell=True
    )

if __name__ == "__main__":
    print("🚀 Memulai sistem...")
    
    # Jalankan Frontend
    run_fe()

    # Jeda 2 detik sebelum run BE
    time.sleep(2)

    # Jalankan Backend
    run_be()

    print("✅ Frontend & Backend berhasil dinyalakan.")
    print("🌐 Buka: http://localhost:5173/")

    # Supaya script tidak langsung close
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 FE dan BE akan dimatikan...")
        time.sleep(2)

        if fe_process:
            fe_process.terminate()
            print("✅ FE dimatikan.")

        if be_process:
            be_process.terminate()
            print("✅ BE dimatikan.")

        print("👋 Program selesai. Bye.")
