from cs50 import get_string
from cs50 import get_int

def sayac():
    return get_int("Hesap Makinesini Çalıştırmak İçin \nBaşlat = 1\nKapat = 2\nİşlemi Seçiniz : ")

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def bolme(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme"
    return a / b

def carpma(a, b):
    return a * b

while True:
    karar = sayac()
    if karar == 1:
        print("Merhaba Hesap Makinesine Hoşgeldiniz.")

        x = get_int("Birinci sayıyı giriniz: ")
        y = get_int("İkinci sayıyı giriniz: ")
        
        while True:
            islem = get_string("Yapabileceğiniz işlemler bunlardır\nToplama = '+'\nÇıkarma = '-'\nÇarpma = '*'\nBölme = '/'\nYapmak istediğiniz işlemi seçiniz: ")

            üst_cizgi = 50 * '-'
            alt_cizgi = 50 * '_'

            if islem == '+':
                print(f"{üst_cizgi}\nİşlem Sonucunuz = {toplama(x, y)}\n{alt_cizgi}")
                break
            elif islem == '-':
                print(f"{üst_cizgi}\nİşlem Sonucunuz = {cikarma(x, y)}\n{alt_cizgi}")
                break
            elif islem == '/':
                print(f"{üst_cizgi}\nİşlem Sonucunuz = {bolme(x, y)}\n{alt_cizgi}")
                break
            elif islem == '*':
                print(f"{üst_cizgi}\nİşlem Sonucunuz = {carpma(x, y)}\n{alt_cizgi}")
                break
            else:
                print("Geçersiz işlem. Lütfen geçerli bir işlem seçiniz.")
    elif karar == 2:
        print("Hesap Makinesi kapatılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 giriniz.")
