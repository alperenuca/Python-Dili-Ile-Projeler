sinav1= int(input("Birinci sınav notunu giriniz :"))
sinav2= int(input("İkinci sınav notunu giriniz :"))
ortalama= (sinav1+sinav2)/2

print("Yıl sonu ortalamanız",ortalama)

if(ortalama < 50):
    print("Dersten Kaldınız")
else : 
    print("Tebrikler dersi geçtiniz")