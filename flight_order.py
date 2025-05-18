from flight_menu import FlightMenu


class FlightOrderItem:
    def __init__(self, flight, jumlah):
        self.flight = flight
        self.jumlah = jumlah

    def subtotal(self):
        return self.flight.harga * self.jumlah

    def __str__(self):
        return f"{self.flight.maskapai} ke {self.flight.tujuan} x {self.jumlah} - Rp{self.subtotal()}"


class FlightOrder:
    def __init__(self):
        self.keranjang = []

    def tambah_pesanan(self, flight_menu, id_flight, jumlah):
        flight = flight_menu.get_flight_by_id(id_flight)
        if flight:
            self.keranjang.append(FlightOrderItem(flight, jumlah))
            print(f"Tiket {flight.maskapai} ke {flight.tujuan} x {jumlah} berhasil ditambahkan.")
        else:
            print("Penerbangan tidak ditemukan.")

    def tampilkan_keranjang(self):
        print("===== KERANJANG TIKET =====")
        total = 0
        for item in self.keranjang:
            print(item)
            total += item.subtotal()
        print(f"Total: Rp{total}")
        return total
