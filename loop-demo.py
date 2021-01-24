import random
number = random.randint(0,100)
can = 10
score = 0
print(f"Tahmin Hakkınız: {can}")
tahmin = 1
dy = False

while dy == False:
    tahminInput = int(input(f"{tahmin}. Tahmin: "))
    if tahminInput == 00:
        print("Çıkış Yaptınız")
        break
    if tahminInput == number:
        can += 5
        score += 10
        print(f"**Doğru Tahmin Ettiniz, Tahmin Hakkınız: {can}**")
        print("*===============================*")
        tahmin += 1
        number = random.randint(0,100)        
    else:
        can -= 1
        tahmin += 1
        print(f"Yanlış Tahmin, Tahmin Hakkınız: {can}")
        if can < 1:
            dy = False
            print("*===============================*")
            print (f"Kaybettiniz, tutulan sayı {number}, skorunuz: {score}")
            break
        if tahminInput < number:
            print("*===============================*")
            print("↑Yukarı↑")
        else:
            print("*===============================*")
            print("↓Aşağı↓")









        