import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# NAMA FILE PENYIMPANAN
# =========================
FILE_TRANSAKSI = "data_transaksi.csv"


# =========================
# FUNGSI BANTUAN
# =========================
def inisialisasi_file():
    """Buat file CSV kalau belum ada, sekaligus tulis header."""
    if not os.path.exists(FILE_TRANSAKSI):
        with open(FILE_TRANSAKSI, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["waktu", "nama_barang", "jumlah", "harga_satuan", "total_per_item"])


def simpan_transaksi_ke_file(data_keranjang):
    """Simpan semua item di keranjang ke file CSV."""
    if not data_keranjang:
        messagebox.showwarning("Peringatan", "Keranjang masih kosong!")
        return

    with open(FILE_TRANSAKSI, mode="a", newline="") as file:
        writer = csv.writer(file)
        for item in data_keranjang:
            # item = (nama_barang, jumlah, harga, total_per_item)
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([waktu, item[0], item[1], item[2], item[3]])

    messagebox.showinfo("Sukses", "Transaksi berhasil disimpan ke file.")
    # setelah simpan kosongkan keranjang
    bersihkan_keranjang()


def hitung_total_semua():
    """Hitung total semua item di keranjang dan tampilkan di label total."""
    total = 0
    for child in tree.get_children():
        total += float(tree.item(child, "values")[3])
    label_total_var.set(f"Total: Rp {total:,.0f}")


def tambah_ke_keranjang():
    """Ambil input, validasi, lalu masukkan ke Treeview."""
    nama = entry_nama.get().strip()
    harga = entry_harga.get().strip()
    jumlah = entry_jumlah.get().strip()

    if not nama or not harga or not jumlah:
        messagebox.showwarning("Peringatan", "Nama barang, harga, dan jumlah harus diisi.")
        return

    # validasi angka
    try:
        harga = float(harga)
        jumlah = int(jumlah)
    except ValueError:
        messagebox.showerror("Error", "Harga harus angka dan jumlah harus bilangan bulat.")
        return

    total_per_item = harga * jumlah

    # masukkan ke Treeview
    tree.insert("", tk.END, values=(nama, jumlah, harga, total_per_item))

    # kosongkan input
    entry_nama.delete(0, tk.END)
    entry_harga.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)

    # update total
    hitung_total_semua()


def bersihkan_keranjang():
    """Hapus semua baris di treeview."""
    for child in tree.get_children():
        tree.delete(child)
    hitung_total_semua()


def ambil_data_keranjang():
    """Ambil semua data dari Treeview dalam bentuk list tuple."""
    data = []
    for child in tree.get_children():
        vals = tree.item(child, "values")
        # urutan: nama, jumlah, harga, total
        nama_barang = vals[0]
        jumlah = int(vals[1])
        harga_satuan = float(vals[2])
        total_per_item = float(vals[3])
        data.append((nama_barang, jumlah, harga_satuan, total_per_item))
    return data


def lihat_file_transaksi():
    """Baca isi CSV dan tampilkan di window baru."""
    if not os.path.exists(FILE_TRANSAKSI):
        messagebox.showinfo("Info", "Belum ada file transaksi.")
        return

    top = tk.Toplevel(root)
    top.title("Riwayat Transaksi (CSV)")
    top.geometry("700x400")

    tree_csv = ttk.Treeview(top, columns=("waktu", "nama", "jumlah", "harga", "total"), show="headings")
    tree_csv.heading("waktu", text="Waktu")
    tree_csv.heading("nama", text="Nama Barang")
    tree_csv.heading("jumlah", text="Jumlah")
    tree_csv.heading("harga", text="Harga")
    tree_csv.heading("total", text="Total")
    tree_csv.pack(fill=tk.BOTH, expand=True)

    with open(FILE_TRANSAKSI, mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            tree_csv.insert("", tk.END, values=row)


# =========================
# INISIALISASI APLIKASI
# =========================
root = tk.Tk()
root.title("Aplikasi Kasir Sederhana - File Based (CSV)")
root.geometry("750x500")

inisialisasi_file()

# =========================
# FRAME INPUT
# =========================
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(fill=tk.X)

tk.Label(frame_input, text="Nama Barang").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(frame_input, width=25)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Harga (Rp)").grid(row=1, column=0, sticky="w")
entry_harga = tk.Entry(frame_input, width=25)
entry_harga.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Jumlah").grid(row=2, column=0, sticky="w")
entry_jumlah = tk.Entry(frame_input, width=25)
entry_jumlah.grid(row=2, column=1, padx=5, pady=5)

btn_tambah = tk.Button(frame_input, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
btn_tambah.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

# =========================
# FRAME TABEL
# =========================
frame_tabel = tk.Frame(root, padx=10, pady=10)
frame_tabel.pack(fill=tk.BOTH, expand=True)

columns = ("nama", "jumlah", "harga", "total")
tree = ttk.Treeview(frame_tabel, columns=columns, show="headings")
tree.heading("nama", text="Nama Barang")
tree.heading("jumlah", text="Jumlah")
tree.heading("harga", text="Harga Satuan")
tree.heading("total", text="Total")

tree.column("nama", width=200)
tree.column("jumlah", width=80, anchor="e")
tree.column("harga", width=100, anchor="e")
tree.column("total", width=120, anchor="e")

tree.pack(fill=tk.BOTH, expand=True)

# =========================
# FRAME BAWAH (AKSI)
# =========================
frame_bawah = tk.Frame(root, padx=10, pady=10)
frame_bawah.pack(fill=tk.X)

label_total_var = tk.StringVar()
label_total_var.set("Total: Rp 0")
label_total = tk.Label(frame_bawah, textvariable=label_total_var, font=("Arial", 12, "bold"))
label_total.pack(side=tk.LEFT)

btn_simpan = tk.Button(frame_bawah, text="Simpan Transaksi (CSV)",
                       command=lambda: simpan_transaksi_ke_file(ambil_data_keranjang()))
btn_simpan.pack(side=tk.RIGHT, padx=5)

btn_bersih = tk.Button(frame_bawah, text="Bersihkan Keranjang", command=bersihkan_keranjang)
btn_bersih.pack(side=tk.RIGHT, padx=5)

btn_lihat = tk.Button(frame_bawah, text="Lihat Riwayat (CSV)", command=lihat_file_transaksi)
btn_lihat.pack(side=tk.RIGHT, padx=5)

# =========================
# JALANKAN APLIKASI
# =========================
root.mainloop()
