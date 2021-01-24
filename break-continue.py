# name = "Gürkan Altunok"

# for letter in name:
#     if letter == "k":
#         continue
#     print(letter)

# x = int(input("Sayı: "))

# z = (x*(x+1))/2
# print(z)

# 0-100 arası tek sayılar toplamı

# x = 0
# result = 0

# while x <= 100:
#     x+=1
#     if x % 2 == 0:
#         continue
#     result += x

# print(result)

x = int(input("Başlangıç Sayısı: "))
y = int(input("Bitiş Sayısı: "))
result = x
baslangic = x
while x < y:
    x+=1
    result += x

print(f"{baslangic} Sayısından, {y} Sayısına Kadar Olan Sayıların Toplamı: {result}")