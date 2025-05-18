class Flight:
    def __init__(self, id, maskapai, tujuan, harga):
        self.id = id
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.harga = harga

    def __str__(self):
        return f"{self.id}. {self.maskapai} ke {self.tujuan} - Rp{self.harga}"


class FlightMenu:
    def __init__(self):
        self.penerbangan = [
            Flight(1, "Garuda Indonesia", "Jakarta - Bali", 1500000),
            Flight(2, "Lion Air", "Jakarta - Surabaya", 900000),
            Flight(3, "Citilink", "Jakarta - Medan", 1200000),
        ]

    def tampilkan_penerbangan(self):
        print("===== DAFTAR PENERBANGAN =====")
        for flight in self.penerbangan:
            print(flight)

    def get_flight_by_id(self, id):
        for flight in self.penerbangan:
            if flight.id == id:
                return flight
        return None
