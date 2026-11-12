# algoritma-pemdas-1

soal 1
Penjelasan kode rekap nilai mahasiswa

Tabel rancangan fungsi (ditulis biasa):
hitung_nilai | masukan: tugas, uts, uas | non-void | keluaran: nilai akhir
nilai_huruf | masukan: nilai | non-void | keluaran: huruf A/B/C/D/E
kelulusan | masukan: huruf | non-void | keluaran: LULUS atau TIDAK LULUS
tampilkan_nilai | masukan: nama, tugas, uts, uas | void | hanya mencetak hasil
main | tanpa masukan | void | mengatur jalannya program

Fungsi non-void mengembalikan hasil dengan return. Fungsi void tidak mengembalikan apa-apa, hanya menjalankan aksi seperti print.

Perhitungan manual (nilai = tugas x 0,3 + uts x 0,3 + uas x 0,4):
Andi: 24 + 21 + 36 = 81 (B, LULUS)
Bunga: 27 + 25,5 + 35,2 = 87,7 (A, LULUS)
Citra: 18 + 13,5 + 20 = 51,5 (D, TIDAK LULUS)
Dimas: 22,5 + 24 + 26 = 72,5 (B, LULUS)
Eka: 9 + 12 + 14 = 35 (E, TIDAK LULUS)
Total = 327,7, rata-rata = 327,7 / 5 = 65,54, jumlah lulus = 3

Penjelasan kode:

hitung_nilai menghitung nilai akhir, tugas 30%, UTS 30%, UAS 40%, lalu mengembalikan hasilnya.
nilai_huruf mengubah angka jadi huruf. 85 ke atas A, 70 ke atas B, 55 ke atas C, 40 ke atas D, selain itu E. Pengecekan dari atas ke bawah, jadi yang cocok duluan yang dipakai.
kelulusan: kalau huruf A, B, atau C maka LULUS, selain itu TIDAK LULUS.
tampilkan_nilai memanggil tiga fungsi di atas secara berurutan (nilai, huruf, status), lalu mencetak nama, nilai, huruf, dan status.
main menyiapkan data dalam list: nama, tugas, uts, uas. Data satu mahasiswa diambil dari urutan (indeks) yang sama.
Variabel total dan jumlah_lulus dimulai dari 0.
Perulangan for i in range(5) memproses lima mahasiswa. Tiap putaran: cetak hasil, hitung nilai lagi lalu tambahkan ke total, ubah ke huruf, dan kalau statusnya LULUS maka jumlah_lulus ditambah 1.
Setelah perulangan, rata_rata = total / 5, lalu rata-rata kelas dan jumlah lulus dicetak.
if name == “main”: main() artinya main hanya dijalankan otomatis kalau file ini dijalankan langsung.


soal 2
Penjelasan kode struk pengiriman toko daring

Tabel rancangan fungsi:
judul | tanpa masukan | void | mencetak judul
ongkos_berat | masukan: berat | non-void | keluaran: biaya berat
ongkos_jarak | masukan: jarak | non-void | keluaran: biaya jarak
diskon | masukan: ongkir, anggota | non-void | keluaran: besar potongan
tampilkan_struk | masukan: nama, berat, jarak, anggota | non-void | mencetak struk dan mengembalikan total
main | tanpa masukan | void | mengatur jalannya program

Perhitungan manual:
Rina (1 kg, 10 km, Bukan): 10.000 + 0 = 10.000, diskon 0, total 10.000
Sari (5 kg, 25 km, Bukan): 10.000 + 3 x 4.000 = 22.000, jarak 5.000, ongkir 27.000, total 27.000
Tono (5 kg, 25 km, Ya): ongkir 27.000, diskon 2.700, total 24.300
Umar (2 kg, 30 km, Ya): 10.000 + 5.000 = 15.000, diskon 1.500, total 13.500
Vina (8 kg, 15 km, Bukan): 10.000 + 6 x 4.000 = 34.000, jarak 0, total 34.000
Total pendapatan = 10.000 + 27.000 + 24.300 + 13.500 + 34.000 = Rp 108.800

Penjelasan kode:

judul mencetak tulisan judul dan garis pemisah.
ongkos_berat: kalau berat 2 kg ke bawah, biayanya 10.000. Kalau lebih, 10.000 ditambah 4.000 untuk setiap kg di atas 2.
ongkos_jarak: kalau jarak 20 km ke bawah, biayanya 0. Kalau lebih, 5.000.
diskon: kalau anggota “Ya”, potongannya 10% dari ongkir (ongkir x 0.1). Kalau tidak, 0.
tampilkan_struk menghitung biaya berat dan biaya jarak, menjumlahkannya jadi ongkir, menghitung potongan, lalu total = ongkir - potongan. Semua rincian dicetak, lalu total dikembalikan dengan return.
main memanggil judul, lalu membuat total_pendapatan = 0.
Lima pelanggan diproses lewat tampilkan_struk. Total tiap pelanggan langsung ditambahkan ke total_pendapatan.
Terakhir, total pendapatan dicetak.
if name == “main”: main() artinya main hanya dijalankan otomatis kalau file ini dijalankan langsung.
