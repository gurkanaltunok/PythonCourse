def sayHello(name = "User"):
    return "Hello "+ name

msg = sayHello("Gürkan")
msg = sayHello("Altunok")

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

yas = yasHesapla(2001)
print(yas)

def EmekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} Yıl Kaldı.")
    else:
        print("Zaten Emekli Oldunuz")

EmekliligeKacYilKaldi(2001, "Gürkan")

print(help(EmekliligeKacYilKaldi))
