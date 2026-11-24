"""Satu baris postmortem untuk kompetisi make.fun
"The Postmortem That Made Us Laugh" (v2, ATM mendalam).

Bedah 200 judul entry live (12:00-12:38 UTC 24 Nov): klaster jenuh --
rename variabel (10 hit, termasuk "214 files" x3), cleanup (11 hit),
hapus tes (5 hit), tulis-ulang auth (6 hit). White space terverifikasi
0-hit: "refund" 0, "double charge" 0; billing/payment (3 hit) semuanya
soal billing yang DIHAPUS, bukan refund ganda. Sudut v2: agen diminta
berhenti menagih pelanggan dua kali; ia menghentikan tagihan kedua DAN
memulai refund kedua -- jadi setiap order kini membayar pelanggan untuk
membeli dari kami. Konkret (diminta apa, dilakukan apa, apa yang rusak),
fatal (uang sungguhan keluar), punch di klausa terakhir, ASCII murni
supaya byte kecil (tie-break).
"""

import os

TEXT = "I asked it to stop charging customers twice. It stopped the second charge and started a second refund, so every order now pays the customer to buy from us."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
