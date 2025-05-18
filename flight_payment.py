class FlightPayment:
    @staticmethod
    def proses_pembayaran(total):
        try:
            bayar = int(input("Masukkan jumlah uang: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            return

        if bayar >= total:
            kembalian = bayar - total
            print(f"Pembayaran: Rp{bayar} - Total: Rp{total} = Kembalian: Rp{kembalian}")
        else:
            print("Uang tidak cukup untuk melakukan transaksi.")
