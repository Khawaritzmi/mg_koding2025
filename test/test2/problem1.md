# Soal Evaluasi Pemrograman Python

Lengkapi setiap bagian kode dari soal berikut ini:

## 1. Kalkulator Sederhana
Buatlah aplikasi kalkulator sederhana dengan **9 tombol angka** (0-9), **4 tombol operasi matematika** (penjumlahan, pengurangan, perkalian, pembagian), dan **tombol sama dengan**. Kalkulator ini harus dapat melakukan operasi matematika dasar berdasarkan input dari pengguna.

### Persyaratan:
- Tombol angka (0-9).
- Tombol operasi: **+**, **-**, **×**, **÷**.
- Tombol **=** untuk menghitung hasil.
- Input dan hasil dihitung secara dinamis berdasarkan tombol yang ditekan.

---

### Kode
```python
import tkinter as tk

# Fungsi untuk menambah angka ke layar kalkulator
def tekan_angka(angka):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(angka))

# Fungsi untuk melakukan perhitungan berdasarkan operator yang dipilih
def hitung():
    try:
        # Ambil ekspresi dari Entry
        expression = entry.get()

        # Tentukan operator dan pisahkan angka
        if '+' in expression:
            num1, num2 = expression.split('+')
            result = float(num1) + float(num2)
        elif '-' in expression:
            # Lengkapi kode berikut
        elif '*' in expression:
            # Lengkapi kode berikut
        elif '/' in expression:
            num1, num2 = expression.split('/')
            if float(num2) != 0:
                result = float(num1) / float(num2)
            else:
                result = "Error (division by zero)"
        else:
            result = "Error (invalid operator)"

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk menghapus angka di layar kalkulator
def clear():
    entry.delete(0, tk.END)

# Membuat window utama
root = tk.Tk()
# Lengkapi kode berikut

# Membuat entry untuk menampilkan angka yang dimasukkan
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Tombol angka 0-9 dan operasi dasar
# Lengkapi kode berikut

button_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 18), command=lambda: tekan_angka(0))
button_0.grid(row=4, column=1, padx=5, pady=5)

# Tombol operasi matematika
button_plus = tk.Button(root, text="+", width=5, height=2, font=("Arial", 18), command=lambda: tekan_angka("+"))
button_plus.grid(row=1, column=3, padx=5, pady=5)

# Tombol Clear dan Hasil
button_clear = tk.Button(# Lengkapi kode berikut)
button_clear.grid(row=4, column=0, padx=5, pady=5)

button_equal = tk.Button(# Lengkapi kode berikut)
button_equal.grid(row=4, column=2, padx=5, pady=5)

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