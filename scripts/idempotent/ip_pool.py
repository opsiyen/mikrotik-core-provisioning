import logging


def ensure_ip_pool_exists(conn, name, ranges, dry_run=False):
    """Buat ip pool hanya jika belum ada. Mode dry_run hanya mencetak."""
    # cek apakah ip pool sudah ada
    output = conn.send_command(f'/ip pool print where name="{name}"')
    if name in output and ranges in output:
        logging.info(
            f"󰡕 Ip pool '{name}' sudah ada di range '{ranges}', lewati pembuatan"
        )
        return
    else:
        if dry_run:
            logging.info(f" Akan membuat ip pool '{name}' di range '{ranges}'")
        else:
            logging.info(f" Membuat ip pool '{name}' di range '{ranges}'")
            conn.send_command(f"/ip pool add name={name} ranges={ranges}")
