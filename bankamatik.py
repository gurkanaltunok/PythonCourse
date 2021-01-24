GurkanHesap = {
    "ad": "Gürkan Altunok",
    "hesapNo": "12453729",
    "bakiye": 4000,
    "ekHesap": 3000
}

ErkanHesap = {
    "ad": "Erkan Altunok",
    "hesapNo": "124504429",
    "bakiye": 9000,
    "ekHesap": 5000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı Alabilirsiniz")
        bakiyeSorgula(GurkanHesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesap Kullanılsın Mı ? (Evet/Hayır): ")

            if ekHesapKullanimi == "evet":
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar
                print("Paranızı Alabilirsiniz")
                bakiyeSorgula(GurkanHesap)

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("Üzgünüz Bakiyeniz Yetersiz")
            bakiyeSorgula(GurkanHesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")

bakiyeSorgula(GurkanHesap)
cekilecekMiktar = int(input("Çekmek İstediğiniz Miktar: "))
paraCek(GurkanHesap, cekilecekMiktar)

cekilecekMiktar = int(input("Çekmek İstediğiniz Miktar: "))
paraCek(GurkanHesap, cekilecekMiktar)


