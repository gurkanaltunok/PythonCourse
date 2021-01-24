# name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

result = len(course)
lenght = len(website)

result = website[7:10]

result = website[22:25]
result = website[lenght-3:lenght]

result = course[0:15]
result = course[:15]
result = course[-15:]

result = course[::-1]

# 'Hello world' ifadesinin w harfini 'W' ile değiştirin.
s = "Hello world"
s = s[0:6] + 'W'+ s[-4:]

print(s)

# 'abd' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3
result

print(result)