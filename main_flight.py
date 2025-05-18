from flight_menu import FlightMenu
from flight_order import FlightOrder
from flight_payment import FlightPayment


def validasi_input_angka(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None


def main():
    flight_menu = FlightMenu()
    order = FlightOrder()

    while True:
        print("\n===== SISTEM PEMESANAN TIKET PESAWAT =====")
        print("1. Lihat Daftar Penerbangan")
        print("2. Pesan Tiket")
        print("3. Lihat Keranjang")
        print("4. Bayar")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            flight_menu.tampilkan_penerbangan()
        elif pilihan == "2":
            flight_menu.tampilkan_penerbangan()
            id_flight = validasi_input_angka("Masukkan ID penerbangan yang ingin dipesan: ")
            if id_flight is None:
                continue
            jumlah = validasi_input_angka("Masukkan jumlah tiket: ")
            if jumlah is None:
                continue
            order.tambah_pesanan(flight_menu, id_flight, jumlah)
        elif pilihan == "3":
            order.tampilkan_keranjang()
        elif pilihan == "4":
            total = order.tampilkan_keranjang()
            FlightPayment.proses_pembayaran(total)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
