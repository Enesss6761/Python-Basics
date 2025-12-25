# Matematiksel Operatörler
sayi1 = 50
sayi2 = 15
print(f"Toplam: {sayi1 + sayi2}, Fark: {sayi1 - sayi2}, Çarpım: {sayi1 * sayi2}, Bölüm: {sayi1 / sayi2}")

# Karşılaştırma Operatörleri
sayi = int(input("Bir sayı girin: "))
print(f"100'den büyük mü? {sayi > 100}")
print(f"100'e eşit mi? {sayi == 100}")
print(f"100'den küçük mü? {sayi < 100}")

# Mantıksal Operatörler (Giriş Sistemi)
kullanici = "admin"
sifre = "12345"
giris_kontrol = (kullanici == "admin") and (sifre == "12345")
print(f"Sisteme giriş izni: {giris_kontrol}")
