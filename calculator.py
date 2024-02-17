from cs50 import get_string
from cs50 import get_int
from cs50 import get_float

sayac = get_int("Hesap Makinesini Çalıştırmak İçin \nBaşlat = 1\nKapat = 2\nİşlemi Seçiniz : ")

def toplama(a,b):
    return  a+b

def cikarma(a,b):
    return a-b

def bölme(a,b):
    return a/b

def carpma(a,b):
    return a*b
while  sayac == 1:
    print("Merhaba Hesap Makinesine Hoşgeldiniz.")

    x = get_int("1. Sayı Giriniz : ")

    y = get_int("2. Sayı Giriniz : ")
    islem = get_string("Yapabilceğiniz işlemler bunlardır\nToplama = '+'\nÇıkarma = '-'\nÇarpma = '*'\nBölme = '/'\nYapmak istediğiniz işlemi seçiniz: ")
    üst_cizgi = 50*'-'
    alt_cizgi = 50*'_'
    
    if islem == '+':
        print(f"{üst_cizgi}\nİşlem Sonucunuz = {toplama(x,y)}\n{alt_cizgi}")
        sayac = get_int("işleme devam etmek istiyorsanız.\nDevam et = 1\nKapat = 2\n\nİşlemi Seçiniz : ")
    elif islem == '-':
        print(f"{üst_cizgi}\nİşlem Sonucunuz = {cikarma(x,y)}\n{alt_cizgi}")
        sayac = get_int("işleme devam etmek istiyorsanız.\nDevam et = 1\nKapat = 2\n\nİşlemi Seçiniz :")
    elif islem == '/':
     print(f"{üst_cizgi}\nİşlem Sonucunuz = {bölme(x,y)}\n{alt_cizgi}")
     sayac = get_int("işleme devam etmek istiyorsanız.\nDevam et = 1\nKapat = 2\n\nİşlemi Seçiniz : ")
    elif islem =='*':
        print(f"{üst_cizgi}\nİşlem Sonucunuz = {carpma(x,y)}\n{alt_cizgi}")
        sayac = get_int("işleme devam etmek istiyorsanız.\nDevam et = 1\nKapat = 2\n\nİşlemi Seçiniz : ")
    else:
        sayac = get_int("Yapmak İstediğiniz İşlemi Anlayamadım.\nUygulamayı Tekrar Başlatın.\nBaşlat = 1\nKapat = 2\nİşlemi Seçiniz :")
    