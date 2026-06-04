import os
from netmiko import ConnectHandler
from dotenv import load_dotenv

# Muat variabel dari file .env
load_dotenv()

# Ambil kredensial dari environment
device = {
    "device_type": "mikrotik_routeros",
    "host": os.getenv("MIKROTIK_HOST"),
    "username": os.getenv("MIKROTIK_USERNAME"),
    "password": os.getenv("MIKROTIK_PASSWORD"),
}

# Cek apakah semua kredensial ada
if not all([device["host"], device["username"], device["password"]]):
    print("Error: Lengkapi kredensial di file .env")
    exit(1)

try:
    conn = ConnectHandler(**device)
    print(f"✅ Koneksi ke {device['host']} berhasil")

    # Baca perintah dari file
    config_path = os.path.join("config", "base_config.txt")
    with open(config_path, "r") as f:
        commands = f.read().splitlines()

    print(f"📄 Membaca {len(commands)} perintah dari {config_path}")

    for cmd in commands:
        if cmd.strip() and not cmd.strip().startswith(
            "#"
        ):  # lewati komentar/baris kosong
            print(f">>> {cmd}")
            output = conn.send_command(cmd)
            if output:
                print(output)
            print("-" * 40)

    conn.disconnect()
    print("✅ Provisioning selesai")
except Exception as e:
    print(f"❌ Gagal koneksi: {e}")
