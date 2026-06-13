import os
import logging
from datetime import datetime
from netmiko import ConnectHandler
from dotenv import load_dotenv


def setup_logging():
    os.makedirs("logs", exist_ok=True)
    log_file = f"logs/provision_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )


def load_credentials():
    load_dotenv()
    return {
        "device_type": "mikrotik_routeros",
        "host": os.getenv("MIKROTIK_HOST"),
        "username": os.getenv("MIKROTIK_USERNAME"),
        "password": os.getenv("MIKROTIK_PASSWORD"),
    }


def connect_to_router(device_dict):
    try:
        conn = ConnectHandler(**device_dict)
        logging.info(f"󰌘 Terhubung ke {device_dict['host']}")
        return conn
    except Exception as e:
        logging.error(f"󰌙 Gagal koneksi: {e}")
        raise
