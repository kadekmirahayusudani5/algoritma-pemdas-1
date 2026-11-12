def judul():
    """judul program"""
    print("STRUK PENGIRIMAN TOKO DARING")
    print("----------------------------")

def ongkos_berat(berat):
    """Menghitung harga berdasarkan berat paket."""
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000

def ongkos_jarak(jarak):
    """Menghitung harga berdasarkan jarak pengiriman."""
    if jarak <= 20:
        return 0
    else:
        return 5000

def diskon(ongkir, anggota):
    """Menghitung diskon untuk pelanggan anggota."""
    if anggota == "Ya":
        return ongkir * 0.1
    else:
        return 0

def tampilkan_struk(nama, berat, jarak, anggota):
    """Menghitung dan menampilkan struk pengiriman."""
    biaya_1 = ongkos_berat(berat)
    biaya_2 = ongkos_jarak(jarak)

    ongkir = biaya_1 + biaya_2
    potongan = diskon(ongkir, anggota)
    total = ongkir - potongan

    print("\nNama pelanggan:", nama)
    print("ongkos berat: Rp", biaya_1)
    print("ongkos jarak: Rp", biaya_2)
    print("diskon: Rp", potongan)
    print("ongkir akhir: Rp", total)

    return total

def main():
    """Menjalankan program struk pengiriman."""
    judul()

    total_pendapatan = 0

    total_pendapatan = total_pendapatan + tampilkan_struk("Rina", 1, 10, "Bukan")
    total_pendapatan = total_pendapatan + tampilkan_struk("Sari", 5, 25, "Bukan")
    total_pendapatan = total_pendapatan + tampilkan_struk("Tono", 5, 25, "Ya")
    total_pendapatan = total_pendapatan + tampilkan_struk("Umar", 2, 30, "Ya")
    total_pendapatan = total_pendapatan + tampilkan_struk("Vina", 8, 15, "Bukan")

    print("\n-----------------------------")
    print("Total pendapatan: Rp", total_pendapatan)


if __name__ == "__main__":
    main()