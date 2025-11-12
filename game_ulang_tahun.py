# game_ulang_tahun.py
import random
import time
import os

def loading(text="Mengemas hadiah"):
    for i in range(3):
        print(text + "." * (i + 1))
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("🎉 SELAMAT DATANG DI GAME ULANG TAHUN 🎉\n")
    nama = input("Masukkan nama ulang tahun: ").strip()
    print(f"\nSelamat ulang tahun, {nama}! 🎂🎁")
    print("Kamu punya 3 kesempatan untuk menebak isi hadiah misterius!\n")
    time.sleep(1)

    # daftar hadiah
    hadiah = {
        "buku": "Petunjuk: Bisa dibaca, banyak ilmu!",
        "jam tangan": "Petunjuk: Selalu ada di pergelangan tangan.",
        "boneka": "Petunjuk: Lucu, lembut, bisa dipeluk!",
        "coklat": "Petunjuk: Manis dan bikin bahagia!",
        "headphone": "Petunjuk: Untuk menikmati musik dengan damai."
    }

    isi_kado = random.choice(list(hadiah.keys()))
    hint = hadiah[isi_kado]

    kesempatan = 3
    while kesempatan > 0:
        print(f"\n{hint}")
        tebakan = input("Tebak isi kadonya: ").lower().strip()

        if tebakan == isi_kado:
            print(f"\n🎉 Benar sekali, {nama}! Kamu menebak dengan tepat! 🎉")
            print("💝 Hadiah kamu adalah:", isi_kado.upper(), "💝")
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"❌ Belum benar! Coba lagi ({kesempatan} kesempatan tersisa)")
            else:
                print(f"😢 Sayang sekali, {nama}! Kesempatanmu habis.")
                print(f"Isi kado sebenarnya adalah: 🎁 {isi_kado.upper()} 🎁")

    print("\nTerima kasih sudah bermain 💕")
    time.sleep(1)
    print("Semoga ulang tahunmu menyenangkan, penuh cinta dan tawa! 🎂")

if __name__ == "__main__":
    loading()
    main()