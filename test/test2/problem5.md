# Soal Evaluasi Pemrograman Python

Lengkapi setiap bagian kode dari soal berikut ini:

## 5. Kalkulator Bangun Datar
Buatkan aplikasi kalkulator yang dapat menghitung **luas** dan **keliling** dari **persegi**, **persegi panjang**, dan **lingkaran**.

### Persyaratan:
- Input nilai untuk **persegi** (sisi), **persegi panjang** (panjang dan lebar), dan **lingkaran** (jari-jari).
- Hitung dan tampilkan **luas** dan **keliling** berdasarkan bangun datar yang dipilih.
- Rumus konversi:
  - **Persegi**:  
    - Luas = sisi × sisi  
    - Keliling = 4 × sisi  
  - **Persegi Panjang**:  
    - Luas = panjang × lebar  
    - Keliling = 2 × (panjang + lebar)  
  - **Lingkaran**:  
    - Luas = π × jari-jari²  
    - Keliling = 2 × π × jari-jari  
    (Gunakan **π = 3.14** untuk lingkaran)

---

### Kode
```python
import tkinter as tk

# Fungsi untuk menghitung luas dan keliling
def hitung():
    try:
        if bangun_var.get() == "Persegi":
            sisi = float(entry_input.get())  # Mengambil nilai sisi dari entry
            #Lengkapi kode berikut
        elif bangun_var.get() == "Persegi Panjang":
            panjang = float(entry_input.get())  # Mengambil nilai panjang dari entry
            lebar = float(entry_input2.get())  # Mengambil nilai lebar dari entry
            luas = #Lengkapi kode berikut
            keliling = #Lengkapi kode berikut
            label_hasil.config(text=f"Luas: {luas} | Keliling: {keliling}")
        elif bangun_var.get() == "Lingkaran":
            #Lengkapi kode berikut 
            luas = 3.14 * jari_jari * jari_jari  # Menghitung luas lingkaran (π * r²)
            keliling = 2 * 3.14 * jari_jari  # Menghitung keliling lingkaran (2 * π * r)
            label_hasil.config(text=f"Luas: {luas:.2f} | Keliling: {keliling:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Membuat window utama
root = tk.Tk()
#Lengkapi kode berikut

# Membuat label untuk memilih bangun datar
label_bangun = tk.Label(#Lengkapi kode berikut)
label_bangun.pack(pady=10)

# Opsi untuk memilih bangun datar
bangun_var = tk.StringVar()
bangun_var.set("Persegi")  # Default pilihan

radio_persegi = tk.Radiobutton(root, text="Persegi", variable=bangun_var, value="Persegi", font=("Arial", 12), command=lambda: update_form())
radio_persegi.pack()

radio_persegi_panjang = tk.Radiobutton(#Lengkapi kode berikut)
radio_persegi_panjang.pack()

radio_lingkaran = tk.Radiobutton(r#Lengkapi kode berikut))
radio_lingkaran.pack()

# Label dan entry untuk input sesuai dengan pilihan
label_input = tk.Label(#Lengkapi kode berikut)
label_input.pack(pady=5)

entry_input = tk.Entry(#Lengkapi kode berikut)
entry_input.pack(pady=5)

# Entry untuk input kedua (hanya tampil jika pilih Persegi Panjang)
label_input2 = tk.Label(root, text="Masukkan lebar (untuk Persegi Panjang):", font=("Arial", 10))
entry_input2 = tk.Entry(#Lengkapi kode berikut)

# Fungsi untuk mengupdate form input sesuai dengan bangun yang dipilih
def update_form():
    if bangun_var.get() == "Persegi":
        label_input.config(text="Masukkan sisi (untuk Persegi):")
        label_input2.pack_forget()
        entry_input2.pack_forget()
    elif bangun_var.get() == "Persegi Panjang":
        label_input.config(text="Masukkan panjang (untuk Persegi Panjang):")
        label_input2.config(text="Masukkan lebar (untuk Persegi Panjang):")
        label_input2.pack(pady=5)
        entry_input2.pack(pady=5)
    elif bangun_var.get() == "Lingkaran":
        label_input.config(text="Masukkan jari-jari (untuk Lingkaran):")
        label_input2.pack_forget()
        entry_input2.pack_forget()

update_form()  # Memperbarui form input sesuai pilihan awal

# Tombol untuk menghitung
button_hitung = tk.Button(#Lengkapi kode berikut, command=hitung)
button_hitung.pack(pady=20)

# Label untuk menampilkan hasil perhitungan
label_hasil = tk.Label(#Lengkapi kode berikut)
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