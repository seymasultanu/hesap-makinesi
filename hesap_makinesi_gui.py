import tkinter as tk
import math

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("340x460")
pencere.configure(bg="#faf3e9")

ekran = tk.Entry(
    pencere,
    font=("Segoe UI", 28),
    justify="right",
    bd=0,
    bg="#fffaf2",
    fg="#5c5470",
    relief="flat",
    highlightthickness=2,
    highlightbackground="#e8dcc8",
    highlightcolor="#d4c4a8"
)
ekran.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=10, ipady=8)


def buton_tiklandi(deger):
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(tk.END, mevcut + deger)


def hesapla():
    try:
        sonuc = eval(ekran.get())
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, str(sonuc))
    except Exception:
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "Hata")


def temizle():
    ekran.delete(0, tk.END)


def karakok():
    try:
        sayi = float(ekran.get())
        if sayi < 0:
            ekran.delete(0, tk.END)
            ekran.insert(tk.END, "Hata")
            return
        sonuc = math.sqrt(sayi)
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, str(sonuc))
    except Exception:
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "Hata")


RENK_SAYI = "#f5ebd9"
RENK_SAYI_YAZI = "#5c5470"
RENK_ISLEM = "#f5cba7"
RENK_ISLEM_YAZI = "#7d4e2d"
RENK_ESITTIR = "#aed6b8"
RENK_ESITTIR_YAZI = "#2d5a3d"
RENK_TEMIZLE = "#f5b7b1"
RENK_TEMIZLE_YAZI = "#7d2d2d"
RENK_KAREKOK = "#c8a8d4"
RENK_KAREKOK_YAZI = "#4a2d5a"

butonlar = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (metin, satir, sutun) in butonlar:
    if metin == "=":
        btn = tk.Button(
            pencere, text=metin, font=("Segoe UI", 18, "bold"),
            bg=RENK_ESITTIR, fg=RENK_ESITTIR_YAZI,
            bd=0, relief="flat", activebackground="#9bc7a6",
            command=hesapla
        )
    elif metin in ("+", "-", "*", "/"):
        btn = tk.Button(
            pencere, text=metin, font=("Segoe UI", 18, "bold"),
            bg=RENK_ISLEM, fg=RENK_ISLEM_YAZI,
            bd=0, relief="flat", activebackground="#e8b893",
            command=lambda d=metin: buton_tiklandi(d)
        )
    else:
        btn = tk.Button(
            pencere, text=metin, font=("Segoe UI", 18),
            bg=RENK_SAYI, fg=RENK_SAYI_YAZI,
            bd=0, relief="flat", activebackground="#ebdfc5",
            command=lambda d=metin: buton_tiklandi(d)
        )
    btn.grid(row=satir, column=sutun, sticky="nsew", padx=4, pady=4)

temizle_btn = tk.Button(
    pencere, text="C", font=("Segoe UI", 16, "bold"),
    bg=RENK_TEMIZLE, fg=RENK_TEMIZLE_YAZI,
    bd=0, relief="flat", activebackground="#e8a39c",
    command=temizle
)
temizle_btn.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)

karakok_btn = tk.Button(
    pencere, text="√", font=("Segoe UI", 18, "bold"),
    bg=RENK_KAREKOK, fg=RENK_KAREKOK_YAZI,
    bd=0, relief="flat", activebackground="#b393c2",
    command=karakok
)
karakok_btn.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=4, pady=4)

for i in range(6):
    pencere.grid_rowconfigure(i, weight=1)
for i in range(4):
    pencere.grid_columnconfigure(i, weight=1)

pencere.mainloop()
