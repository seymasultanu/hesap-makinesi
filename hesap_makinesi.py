print("=== Hesap Makinesi ===")

sayi1 = float(input("Birinci sayıyı gir: "))
islem = input("İşlem seç (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı gir: "))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 == 0:
        sonuc = "Hata: Sıfıra bölünemez!"
    else:
        sonuc = sayi1 / sayi2
else:
    sonuc = "Geçersiz işlem!"

print(f"Sonuç: {sonuc}")
