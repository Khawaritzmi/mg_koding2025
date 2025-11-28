# Soal Evaluasi Pemrograman Python

Lengkapi setiap bagian kode dari soal berikut ini:

## 4. Konversi Satuan Panjang
Buatkan aplikasi untuk mengonversi panjang dari **meter** ke **yard**, **kilometer**, dan **centimeter**.

### Cerita:
Andi ingin mengukur panjang lapangan sepak bola yang panjangnya 100 meter. Namun, pelatihnya meminta untuk mengetahui panjang lapangan dalam satuan **yard** dan **kilometer**. Buatkan aplikasi yang memungkinkan Andi untuk mengonversi panjang lapangan dari **meter** ke **yard**, **kilometer**, dan **centimeter**.

### Persyaratan:
- Input panjang dalam **meter** dan tampilkan hasil konversi ke **yard**, **kilometer**, dan **centimeter**.
- Rumus konversi:
  - **1 meter = 1.09361 yard**
  - **1 meter = 0.001 kilometer**
  - **1 meter = 100 centimeter**

---

### Kode
```python
import tkinter as tk

# Fungsi untuk menghitung konversi satuan panjang
def konversi():
    try:
        # Mengambil nilai panjang dalam meter dari entry
        meter = float(entry_meter.get())

        # Melakukan konversi
        #Lengkapi kode berikut

        # Menampilkan hasil konversi
        label_yard.config(text=f"{yard:.2f} yard")
        #Lengkapi kode berikut
    except ValueError:
        label_yard.config(text="Masukkan angka yang valid")
        label_kilometer.config(text="")
        label_centimeter.config(text="")

# Membuat window utama
root = tk.Tk()
#Lengkapi kode berikut

# Membuat label dan entry untuk input panjang dalam meter
label_meter = tk.Label(#Lengkapi kode berikut)
label_meter.pack(pady=10)

entry_meter = tk.Entry(#Lengkapi kode berikut)
entry_meter.pack(pady=10)

# Tombol untuk melakukan konversi
button_konversi = tk.Button(#Lengkapi kode berikut)
button_konversi.pack(pady=20)

# Label untuk menampilkan hasil konversi
#Lengkapi kode berikut

label_centimeter = tk.Label(root, text="Hasil konversi ke centimeter:", font=("Arial", 12))
label_centimeter.pack()

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