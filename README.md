# flight-booking-ticket
## 1. Pendahuluan
### 1.1 Tujuan
Dokumen ini menjelaskan kebutuhan fungsional dan non-fungsional dari Sistem Pemesanan Tiket Pesawat Sederhana yang dibangun menggunakan Python. Sistem ini bertujuan untuk mempermudah proses pemesanan tiket pesawat melalui antarmuka terminal (CLI).
### 1.2 Lingkup
Sistem memungkinkan pengguna untuk :
* Menampilkan daftar penerbangan
* Memesan tiket berdasarkan maskapai dan tujuan
* Melihat keranjang pesanan
* Melakukan pembayaran dan menampilkan kembalian
### 1.3 Definisi, Akronim, dan Singkatan
| Istilah | Arti                               |
----------|------------------------------------|
| CLI	    |Command Line Interface              |
| SRS	    |Software Requirements Specification |
| User	  | Pengguna akhir aplikasi            |
| Admin	  | Pemilik/pengelola sistem           |
## 2. Deskripsi Umum
### 2.1 Perspektif Produk
Aplikasi ini adalah standalone berbasis terminal, Tidak memerlukan koneksi internet atau database eksternal, dan dapat dijalankan pada komputer yang telah terpasang python.
### 2.2 Fungsi Sistem
* Menampilkan daftar penerbangan dari data statis
* Menambahkan tiket ke keranjang
* Menampilkan isi keranjang dan subtotal
* Menghitung total harga dan memproses pembayaran
* Menampilkan kembalian atau pesan kesalahan jika pembayaran kurang
### 2.3 Karakteristik Pengguna
Pengguna adalah calon penumpang atau petugas tiket. Tidak dibutuhkan latar belakang teknis; sistem dirancang untuk kemudahan pengguna melalui input numerik sederhana di terminal.
## 3. Kebutuhan Fungsional
|  Kode  | Nama Fitur                   | Deskripsi                                                                |
|--------|------------------------------|--------------------------------------------------------------------------|
| RF001  | Tampilkan daftar penerbangan | Sistem menampilkan daftar penerbangan berdasarkan data statis            |
| RF002  | Tambah pesanan               | Pengguna dapat memilih penerbangan berdasarkan ID dan Jumlah tiket       |
| RF003  | Tampilkan keranjang          | Sistem menampilan isi pesanan dan subtotal                               |
| RF004  | Proses pembayaran            | Sistem menerima jumlah uang, menghtung total, dan menampilkan kembali    |
| RF005  | Validasi pembayran           | Sistem menolak pembayaran jika jumlah uang kurang dari total harga tiket |
## 4. Kebutuhan Non-Fungsional
| Kode   | Deskripsi                                                                 |
|--------|---------------------------------------------------------------------------|
| RNF001 | Sistem merespons input pengguna dalam waktu kurang dari 1 detik.         |
| RNF002 | Sistem dapat dijalankan di Python 3.x tanpa library eksternal tambahan.  |
| RNF003 | Antarmuka berbasis teks sederhana (CLI) untuk kemudahan penggunaan.      |
## 5. Antarmuka Sistem
### 5.1 Antarmuka Pengguna
* CLI (Command Line Interface) berbasis teks.
* Navigasi menggunakan input numerik (contoh: pilih 1 untuk lihat penerbangan).
* Umpan balik langsung saat input salah atau proses berhasil/gagal.
* Tampilan terminal yang sederhana dan informatif untuk daftar penerbangan, keranjang, dan pembayaran.
### 5.2 Antarmuka Perangkat Keras
* Komputer/Laptop yang mendukung Python 3.x.
* Tidak membutuhkan perangkat keras tambahan (printer, scanner, dll).
* Input: keyboard. Output: layar terminal/console.
### 5.3 Antarmuka Perangkat Lunak
* Interpreter Python
* Tidak memerlukan library ekseternal tambahan
## 6. Batasan Sistem
* Tidak menyimpan data secara permanen
* Hanya melayani satu transaksi pada satu waktu
* Tidak ada fitur login atau manajemen pengguna
* Tidak tersedia dalam bentuk GUI atau web
## 7. Lampiran
* Struktur kode program (terpisah dalam 4 file: flight_menu.py, flight_order.py, flight_payment.py, main_flight.py)
#### 1. flight_menu.py
  ![Image](https://github.com/user-attachments/assets/5a8542ef-80a6-49d8-ada1-1cb0a57837fc)
#### 2. flight_order.py
![Image](https://github.com/user-attachments/assets/d3869c8f-959e-48b0-adc5-679ff7cfc274)
#### 2. flight_payment.py
![Image](https://github.com/user-attachments/assets/c290f591-bedf-4696-996f-bb1489dd4b7a)
#### 2. mian_flight.py
![Image](https://github.com/user-attachments/assets/afc2ef88-1f54-4f22-bf57-06e0d8b827c7)

##### Screenshot contoh penggunaan program
![Image](https://github.com/user-attachments/assets/0002555a-b5d5-49ca-9fea-c1ce02d275ac)
![Image](https://github.com/user-attachments/assets/4a1f8f52-79c3-4a66-97c2-13fc4d89a747)

