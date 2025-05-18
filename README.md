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
