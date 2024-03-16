import random

class Çekiliş:
    def __init__(self):
        self.katilimcilar = []

    def kazanan_sec(self):
        if len(self.katilimcilar) == 0:
            return "Katılımcı yok."
        else:
            kazanan = random.choice(self.katilimcilar)
            return kazanan

    def katilimci_ekle(self, katilimci):
        self.katilimcilar.append(katilimci)
    def katilimci_listesi(self):
        return self.katilimcilar

rnd = Çekiliş()

while True:
    print("Çekiliş Programı")
    print("1. Yeni Kişi Ekle")
    print("2. Çekilişi Yap")
    print("3. Kişileri Gör")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        katilimci = input("İsim Giriniz: ")
        rnd.katilimci_ekle(katilimci)
        print(f"{katilimci}, İsmi çekilişe eklendi :) ")
    elif secim == "2":
        print("Kazanan:", rnd.kazanan_sec())
    elif secim == "3":
        print("Katılımcılar:", rnd.katilimci_listesi())
    elif secim == "4":
        print("Çıkış yapılıyor")
        break
    else:
        print("Geçersiz İşlem")
