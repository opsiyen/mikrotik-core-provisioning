import logging


def ensure_dhcp_server(conn, dhcp_config, dry_run=False):
    name = dhcp_config["name"]
    interface = dhcp_config["interface"]
    address_pool = dhcp_config["address_pool"]
    network = dhcp_config["network"]
    gateway = dhcp_config["gateway"]
    dns = dhcp_config["dns"]
    lease_time = dhcp_config.get("lease_time", "10m")  # default 10 menit

    # Cek apakah DHCP server sudah ada
    check = conn.send_command(f"/ip dhcp-server print where name={name}")
    if name in check:
        logging.info(f"󰡕 DHCP server '{name}' sudah ada, lewati pembuatan")
    else:
        if dry_run:
            logging.info(f" Akan membuat DHCP server '{name}' di {interface}")
        else:
            logging.info(f" Membuat DHCP server '{name}' di {interface}")
            conn.send_command(
                f"/ip dhcp-server add name={name} interface={interface} address-pool={address_pool} lease-time={lease_time} disabled=no"
            )

    # Cek apakah address pool sudah ada
    pool_check = conn.send_command(f"/ip pool print where name={address_pool}")
    if address_pool in pool_check:
        logging.info(f"󰡕 Address pool '{address_pool}' sudah ada, lewati pembuatan")
    else:
        if dry_run:
            logging.info(
                f" Akan membuat address pool '{address_pool}' range {gateway}? (sesuaikan)"
            )
        else:
            # Hitung range otomatis? Bisa hardcode dulu. Untuk contoh, kita buat pool /24 dari network
            # Misal network 192.168.88.0/24, maka range 192.168.88.2-192.168.88.254
            # Tapi sederhananya, Anda bisa tentukan range manual di YAML.
            # Di sini kita asumsikan range sudah ditentukan.
            # Untuk latihan, kita lewati dulu pembuatan pool karena perlu logika lebih.
            logging.warning(
                "Pembuatan address pool otomatis belum diimplementasikan, harap buat manual"
            )

    # Cek network configuration
    net_check = conn.send_command(
        f"/ip dhcp-server network print where address={network}"
    )
    if network in net_check:
        logging.info(f"󰡕 DHCP network '{network}' sudah ada, lewati pembuatan")
    else:
        if dry_run:
            logging.info(
                f" Akan menambah network {network} dengan gateway {gateway}, dns {dns}"
            )
        else:
            conn.send_command(
                f"/ip dhcp-server network add address={network} gateway={gateway} dns-server={dns}"
            )
