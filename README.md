# Hesap Makinesi

Python ile yapılmış hesap makinesi uygulaması.

## Dosyalar

- `hesap_makinesi.py` - Terminal versiyonu
- `hesap_makinesi_gui.py` - Görsel arayüzlü versiyon (Tkinter, soft renkli, karekök destekli)

## Çalıştırma

### Python ile

```bash
python hesap_makinesi_gui.py
```

### Masaüstü uygulaması olarak (.exe)

PyInstaller ile tek dosyalık bağımsız uygulama oluşturmak için:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Hesap Makinesi" hesap_makinesi_gui.py
```

Sonuç `dist/Hesap Makinesi.exe` olarak çıkar — Python kurulu olmasa bile çalışır.

## Özellikler

- Toplama, çıkarma, çarpma, bölme
- Karekök (√)
- Sıfıra bölme kontrolü
- Soft krem/pastel tema
