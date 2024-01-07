import tkinter as tk

def hitung_luas():
    jenis_bangun_datar = var_bangun_datar.get()

    if jenis_bangun_datar == "Persegi Panjang":
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        luas = panjang * lebar
        label_hasil.config(text=f"Luas {jenis_bangun_datar}: {luas}")

    # Tambahkan jenis bangun datar lainnya sesuai kebutuhan

# Membuat GUI
app = tk.Tk()
app.title("Hitung Luas Bangun Datar")

# Pilihan Jenis Bangun Datar
var_bangun_datar = tk.StringVar(app)
var_bangun_datar.set("Persegi Panjang")

label_jenis = tk.Label(app, text="Pilih Jenis Bangun Datar:")
label_jenis.grid(row=0, column=0, padx=10, pady=5, sticky="w")

dropdown_jenis = tk.OptionMenu(app, var_bangun_datar, "Persegi Panjang", "Lingkaran", "Segitiga")
dropdown_jenis.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Input Panjang dan Lebar
label_panjang = tk.Label(app, text="Panjang:")
label_panjang.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_panjang = tk.Entry(app)
entry_panjang.grid(row=1, column=1, padx=10, pady=5)

label_lebar = tk.Label(app, text="Lebar:")
label_lebar.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_lebar = tk.Entry(app)
entry_lebar.grid(row=2, column=1, padx=10, pady=5)

# Tombol Hitung
btn_hitung = tk.Button(app, text="Hitung Luas", command=hitung_luas)
btn_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label Hasil
label_hasil = tk.Label(app, text="")
label_hasil.grid(row=4, column=0, columnspan=2, pady=5)

# Menjalankan GUI
app.mainloop()