# MikroTik Router Provisioning with Netmiko

Proyek ini adalah skrip automasi berbasis Python menggunakan pustaka **Netmiko** untuk melakukan konfigurasi awal (*provisioning*) pada perangkat MikroTik RouterOS. Skrip ini dirancang untuk menyederhanakan dan menstandardisasi implementasi jaringan, menggantikan konfigurasi manual.

## Fitur Utama
1. Melakukan distribusi VLAN (Services, CCTV, IoT, Private, Guest, Management).
2. Mengonfigurasi IP Addressing untuk setiap antarmuka.
3. Menerapkan *Security Hardening* dengan mematikan layanan tidak aman (Telnet, FTP, SMB).
4. Auto detiksi versi mayor v6 / v7
5. dry-run, mode simulasi tanpa eksikusi nyata.
6. Idempotensi, sebagai pencegahan error duplikasi.
7. Logging, sebagai catatan aktivitas.

## Persyaratan (Prerequisites)
- Python 3.11.2 atau lebih baru.
- MikroTik RouterOS (Diuji pada versi 6.49 / 7.22).
- Akses SSH ke router harus sudah aktif.

## Cara Instalasi
1. Clone repository:

2. Buat virtual environment (Direkomendasikan):
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows

3. Install dependensi:
   pip install -r requirements.txt

4. Konfigurasi Kredensial
   Salin file .env.example menjadi .env dan isi file .env dengan IP Router, Username, dan Password yang valid.

## Cara Penggunaan
- DRY_RUN=True python3 main.py
- python3 main.py
