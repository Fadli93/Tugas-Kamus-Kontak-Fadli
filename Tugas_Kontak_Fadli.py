class ManajerKontak:
    def __init__(self):
        self.kontak = {}
        self.kontak_diblokir = set()

    def tambah_kontak(self, nama, nomor):
        self.kontak[nama] = nomor
        print(f"Kontak '{nama}' berhasil ditambahkan.")

    def tampilkan_kontak(self):
        if not self.kontak:
            print("Daftar kontak kosong.")
        else:
            print("\nDaftar Kontak:")
            for nama, nomor in self.kontak.items():
                status = "(Diblokir)" if nama in self.kontak_diblokir else ""
                print(f"- {nama}: {nomor} {status}")

    def cari_kontak(self, nama):
        if nama in self.kontak:
            status = "(Diblokir)" if nama in self.kontak_diblokir else ""
            print(f"{nama}: {self.kontak[nama]} {status}")
        else:
            print("Kontak tidak ditemukan.")

    def hapus_kontak(self, nama):
        if nama in self.kontak:
            del self.kontak[nama]
            self.kontak_diblokir.discard(nama)
            print(f"Kontak '{nama}' berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    def blokir_kontak(self, nama):
        if nama in self.kontak:
            self.kontak_diblokir.add(nama)
            print(f"Kontak '{nama}' berhasil diblokir.")
        else:
            print("Kontak tidak ditemukan.")

    def tampilkan_kontak_diblokir(self):
        if not self.kontak_diblokir:
            print("Tidak ada kontak yang diblokir.")
        else:
            print("\nKontak yang Diblokir:")
            for nama in self.kontak_diblokir:
                print(f"- {nama}: {self.kontak[nama]}")


def main():
    manajer = ManajerKontak()
    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Tampilkan Semua Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Blokir Kontak")
        print("6. Tampilkan Kontak yang Diblokir")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor HP: ")
            manajer.tambah_kontak(nama, nomor)
        elif pilihan == '2':
            manajer.tampilkan_kontak()
        elif pilihan == '3':
            nama = input("Masukkan nama yang ingin dicari: ")
            manajer.cari_kontak(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama yang ingin dihapus: ")
            manajer.hapus_kontak(nama)
        elif pilihan == '5':
            nama = input("Masukkan nama yang ingin diblokir: ")
            manajer.blokir_kontak(nama)
        elif pilihan == '6':
            manajer.tampilkan_kontak_diblokir()
        elif pilihan == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
