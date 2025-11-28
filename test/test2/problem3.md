# Soal Evaluasi Pemrograman Python

Lengkapi setiap bagian kode dari soal berikut ini:

## 3. Konversi Celcius ke Fahrenheit dan Sebaliknya
Buatkan aplikasi untuk mengonversi suhu dari **Celcius** ke **Fahrenheit** dan sebaliknya.

### Cerita:
Sarah adalah seorang warga negara Amerika yang berlibur ke Indonesia. Di Indonesia, suhu sering diukur dalam **Celcius**, tetapi di Amerika suhu diukur dalam **Fahrenheit**. Suatu hari, Sarah merasa penasaran dan ingin tahu berapa suhu 25°C dalam Fahrenheit. Buatkan aplikasi yang memungkinkan Sarah mengonversi suhu dari **Celcius** ke **Fahrenheit** dan sebaliknya.

### Persyaratan:
- Input suhu dalam **Celcius** dan tampilkan hasil konversi ke **Fahrenheit**.
- Input suhu dalam **Fahrenheit** dan tampilkan hasil konversi ke **Celcius**.
- Rumus konversi:
  - **Fahrenheit = (Celcius × 9/5) + 32**
  - **Celcius = (Fahrenheit - 32) × 5/9**

---

### Kode
```python
import tkinter as tk

# Fungsi untuk konversi suhu Celcius ke Fahrenheit
def celcius_ke_fahrenheit():
    try:
        celcius = float(entry_celcius.get())  # Mengambil nilai dari input celcius
        #Lengkapi kode berikut

# Fungsi untuk konversi suhu Fahrenheit ke Celcius
def fahrenheit_ke_celcius():
    try:
        #Lengkapi kode berikut
        label_hasil.config(text=f"{fahrenheit}°F = {celcius}°C")  # Menampilkan hasil
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")  # Error handling

# Membuat window utama
root = tk.Tk()
#Lengkapi kode berikut

# Membuat label dan entry untuk input suhu Celcius
label_celcius = tk.Label(root, text="Masukkan suhu dalam Celcius:")
#Lengkapi kode berikut

# Membuat tombol konversi Celcius ke Fahrenheit
button_celcius_ke_fahrenheit = tk.Button(#Lengkapi kode berikut)
button_celcius_ke_fahrenheit.pack(pady=10)

# Membuat label dan entry untuk input suhu Fahrenheit
#Lengkapi kode berikut
entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.pack(pady=5)

# Membuat tombol konversi Fahrenheit ke Celcius
button_fahrenheit_ke_celcius = tk.Button(#Lengkapi kode berikut)
button_fahrenheit_ke_celcius.pack(pady=10)

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