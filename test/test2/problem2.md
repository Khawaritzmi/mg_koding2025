# Soal Evaluasi Pemrograman Python

Lengkapi setiap bagian kode dari soal berikut ini:

## 2. Konversi USD ke IDR dan Sebaliknya
Buatkan aplikasi konversi antara **USD** (Dolar AS) dan **IDR** (Rupiah). Aplikasi ini harus dapat mengonversi nilai dari **USD ke IDR** dan **IDR ke USD**.

### Cerita:
Toko online di Indonesia menerima pembayaran menggunakan USD. Pelanggan dari Amerika ingin mengetahui berapa banyak Rupiah yang mereka bayar jika harga produk di toko tersebut adalah 100 USD. Buatkan aplikasi untuk mengonversi antara **USD** dan **IDR**.

### Persyaratan:
- Input nilai dalam **USD** dan tampilkan hasil konversi ke **IDR**.
- Input nilai dalam **IDR** dan tampilkan hasil konversi ke **USD**.
- Gunakan nilai tukar **1 USD = 15,000 IDR** (atau sesuai dengan nilai tukar yang ditentukan).

---

### Kode
```python
import tkinter as tk

# Nilai tukar tetap, Anda bisa menyesuaikan atau menambahkan integrasi API untuk nilai tukar yang dinamis
nilai_tukar_idr_ke_usd = 0.000066  # 1 IDR = 0.000066 USD
nilai_tukar_usd_ke_idr = 15000     # 1 USD = 15000 IDR

# Fungsi untuk konversi IDR ke USD
def idr_ke_usd():
    try:
        # Lengkapi kode berikut
        label_hasil.config(text=f"Rp {idr} = ${usd:.2f} USD")  # Menampilkan hasil
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")  # Error handling

# Fungsi untuk konversi USD ke IDR
def usd_ke_idr():
    try:
        usd = float(entry_usd.get())  # Mengambil nilai dari input USD
        # Lengkapi kode berikut

# Membuat window utama
root = tk.Tk()
# Lengkapi kode berikut

# Membuat label dan masukan untuk input Rupiah
label_idr = tk.Label(root, text="Masukkan jumlah Rupiah (IDR):")
# Lengkapi kode berikut

# Membuat tombol konversi IDR ke USD
button_idr_ke_usd = tk.Button(# Lengkapi kode berikut)
button_idr_ke_usd.pack(pady=10)

# Membuat label dan entry untuk input Dolar AS
# Lengkapi kode berikut

# Membuat tombol konversi USD ke IDR
button_usd_ke_idr = tk.Button(# Lengkapi kode berikut)
button_usd_ke_idr.pack(pady=10)

# Membuat label untuk menampilkan hasil konversi
label_hasil = tk.Label(root, text="Hasil konversi akan muncul di sini.", font=("Arial", 12))
label_hasil.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
```

---
### Petunjuk:
1. Gunakan **Tkinter** untuk antarmuka grafis.
2. Aplikasi harus dapat menerima input dari pengguna (baik angka, teks, atau pilihan).
3. Hasil konversi atau perhitungan harus ditampilkan secara dinamis di antarmuka pengguna.

---

### Format Penyerahan:
1. File kode Python untuk setiap aplikasi di atas.
2. Jelaskan cara penggunaan setiap aplikasi.
3. Jelaskan cara kerja kode.