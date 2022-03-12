# V1
# class Bekorchi:
#     def __init__(self):
#         pass

# V2
# class Oquvchi:
#     def __init__(self):
#         pass

# V3
# class Car:
#     def __init__(self,collor):
#         self.color = collor

# V4
# class Name:
#     def show(self):
#         print("salom")
#
#
# name = Name()
# name.show()

# V5
# class Animals:
#     def __init__(self, num, son):
#         self.num = num
#         self.son = son
#
#
# ayiq = Animals()


# V6
# class Cars:
#     def __init__(self, color, tezlig, narhi, markasi, shina, motor, kuzp ):
#         self.color = color
#         self.tezligi = tezlig
#         self.narhi = narhi
#         self.marka =markasi
#         self.shina = shina
#         self.motor = motor
#         self.kuzov = kuzp
#
#     def colorr(self):
#         print(self.color)
#
#     def tezlig(self):
#         print(self.tezligi)
#
#     def narh(self):
#         print(self.narhi)
#
#     def markasi(self):
#         print(self.marka)
#
#     def shinasi(self):
#         print(self.shina)
#
#
# avto = Cars("yshl", 300, 6500, "BMW", "shiroki", 5, "Temr")
# avto.colorr()
# avto.narh()
# avto.markasi()
# avto.tezlig()
# avto.shinasi()

# V7
# class Cars:
#     def __init__(self, name, year, tezligi):
#         self.name = name
#         self.year = year
#         self.tezligi = tezligi
#
#     def start(self):
#         print(self.tezligi)
#
#     def stop(self):
#         print("stop")
#
#     def turn_right(self):
#         print("o'ngtomonga burilin")
#
#     def turn_back(self):
#         print("buriling")
#
#
# car1 = Cars("BMW", 2022, 300)
# car2 = Cars("BMW", 2022, 300)
# car3 = Cars("BMW", 2022, 300)
# car4 = Cars("BMW", 2022, 300)
# car5 = Cars("BMW", 2022, 300)
# car1.start()

# V8
# class Talaba:
#     def __init__(self, isim, familia, baho):
#         self.isim = isim
#         self.familia = familia
#         self.baho = baho
#
#
# Adham = Talaba("Adham", "sobirov", 5)
# Dilshod = Talaba("Dilshod", "sobirov", 4)
# Donior = Talaba("Donior", "sobirov", 2)
#
# if Adham.baho < Dilshod.baho and Adham.baho < Donior.baho:
#     print(Adham.isim)
# elif Dilshod.baho < Adham.baho and Dilshod.baho < Donior.baho:
#     print(Dilshod.isim)
# else:
#     print(Donior.isim)

# V9
# class Human:
#     def __init__(self, name, age, profession, height, weight, single):
#         self.name = name
#         self.age = age
#         self.professional = profession
#         self.height = height
#         self.weight = weight
#         self.single = single
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_professional(self):
#         return self.professional
#
#     def get_height(self):
#         return self.height
#
#     def get_weight(self):
#         return self.weight
#
#     def get_single(self):
#         return self.single
#
#
# user = Human("Salohiddin", 18, "dasturchi", "salom", "rahmat", "arzimaydi")
# print(user.get_name())
# print(user.get_age())
# print(user.get_professional())
# print(user.get_height())
# print(user.get_weight())
# print(user.get_single())

# V10
# class Bino:
#     def __init__(self, rangi, balandligi):
#         self.rangi = rangi
#         self.balandligi = balandligi
#

# bino1 = Bino("ko'k", 222)
# bino2 = Bino("yashil", 51)
# bino3 = Bino("qizil", 22)
# bino4 = Bino("qora", 20)
# bino5 = Bino("sarq", 10)
#
# if bino1.balandligi > 50:
#     print(bino1.rangi)
# if bino2.balandligi > 50:
#     print(bino2.rangi)
# if bino3.balandligi > 50:
#     print(bino3.rangi)
# if bino4.balandligi > 50:
#     print(bino4.rangi)
# if bino5.balandligi > 50:
#     print(bino5.rangi)


# V11
# class Human:
#     def __init__(self, ferst_name, last_name, age):
#         self.ferst_name = ferst_name
#         self.last_name = last_name
#         self.age =age
#
#     def full_name(self):
#         return f"{self.ferst_name} {self.last_name}"
#
#
# person = Human("salohiddin", "Sayfullayev", 18)
# print(person.full_name())

# V12
# class Notebooc:
#     def __init__(self, firmasi, model, CPU, DDR, price):
#         self.firmasi =firmasi
#         self.model = model
#         self.CPU =CPU
#         self.DDR =DDR
#         self.price =price
#
#     def info_notebook(self):
#         print(f"firma {self.firmasi} madel {self.model} CPU {self.CPU} DDR {self.DDR} price {self.price}")
#
#
# people = Notebooc("Note", "nmadir", "uyamnmadir", "blmiman", "esmda_yo'q")
# people.info_notebook()

# V13
# class List:
#     def __init__(self, list):
#         self.my_list = list
#
#     def delet(self):
#         return self.my_list[:-1]
#
#
# list1 = List([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(str(list1.delet()))

# V14
# class List:
#     def __init__(self, list):
#         self.my_list = list
#
#     def delet(self):
#         return self.my_list[1:]
#
#
# list1 = List([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(str(list1.delet()))

# V15
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#         self.num = input("Mashinani so'rang").strip().capitalize()
#
#     def brand_exists(self):
#         if self.num in self.brand:
#             return True
#         return False
#
#
# car = Car(["Nexia", "Spark", "Matiz"])
# print(car.brand_exists())


# V16
# class Name:
#     def __init__(self):
#         self.num = None
#
#
#     def get_string(self):
#         self.num = input().strip()
#         return self.num
#
#     def update_string(self):
#         return self.num[:-1].title() + self.num[-1].upper()
#
#
# name = Name()
# name.get_string()
# print(name.update_string())

# v17
# class Odam:
#     def __init__(self, name):
#         self.name = name
#
#     def salomlash(self):
#         return f"Salom {self.name}"
#
#
# men = Odam("Abdulloh")
# print(men.salomlash())


# V18
# class Rectangle:
#     def __init__(self, eni, boyi):
#         self.eni = eni
#         self.boyi = boyi
#
#     def get_perimetr(self):
#         return 2 * (self.eni + self.boyi)
#
#     def get_yuzi(self):
#         return self.eni * self.boyi
#
#
# torburchak1 = Rectangle(10, 5)
# print(torburchak1.get_perimetr(), torburchak1.get_yuzi())
# torburchak2 = Rectangle(11, 6)
# print(torburchak2.get_perimetr(), torburchak2.get_yuzi())
# torburchak3 = Rectangle(12, 7)
# print(torburchak3.get_perimetr(), torburchak3.get_yuzi())


# V19
# PI = 3.14
# class Aylana:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def aylana_uzunligi(self):
#         return 2 * PI * self.radius
#
#     def aylana_perimetr(self):
#         return (PI // 2 + 2) + self.radius
#
#
# aylana1 = Aylana(15)
# print(f"Aylana uzunligi {aylana1.aylana_uzunligi()}  Aylana perimetiri{aylana1.aylana_perimetr()}")
# aylana2 = Aylana(14)
# print(f"Aylana uzunligi{aylana2.aylana_uzunligi()}  Aylana perimetiri{aylana2.aylana_perimetr()}")

# V20
# class Odam:
#     def __init__(self, isim):
#         self.isim = isim
#
#     def baqir(self):
#         print(f"{self.isim}E onneni db baqirdi")
#
#
# class Kuchuk:
#     def __init__(self, laqab):
#         self.laqab = laqab
#
#     def tishla(self, tishladi):
#         print(f"Kuchuk tishladi")
#         tishladi.baqir()
#
#
# inson = Odam("jalil")
# kuchuk = Kuchuk("Bo'bik")
# kuchuk.tishla(inson)


# V21
# class Animals:
#     def __init__(self):
#         self.name = "Ot"
#         self.age = 7
#
#     def eat(self):
#         print("eat")
#
# class Bords(Animals):
#     pass
#
#
# owl = Bords()
# owl.eat()

# V22
# class Parametr:
#     def __init__(self, name, num, son, fanilia, yoshi):
#         pass

# V23
# class Properti:
#     def __init__(self):
#         self.num = 15
#         self.name = "Salohiddin"
#         self.age = 18
#
#
# man = Properti()

# V24
# class Name:
#     @staticmethod
#     def show_salom():
#         num = input("So'z kiriting")
#         print(num)
#
# name = Name.show_salom()

# V25
# class Device:
#     def __init__(self):
#         self.brend = input("Brend tanlang")
#         self.color = input("rangini tanlang")
#
#     def och_yon(self):
#         print("o'chdi yondi")
#
#     def dasturlar(self):
#         print("Dasturlar ishga tushdi")
#
#
# class Compiuter(Device):
#     def __init__(self):
#         super().__init__()
#         self.core = input("cori nechi bo'lsin")
#         self.monitor = input("manitor kattaligi qanday bo'lsin")
#
#     def klaviatura(self):
#         print("Klaviatura ulangan")
#
#     def maus(self):
#         print("Maus ishlamoqda")
#
#
# class Phone(Device):
#     def __init__(self):
#         super().__init__()
#         self.kamera = input("kamerasi necha mega piksel bo'lsin")
#         self.fleshka = input("fleshkasi necha GB bolsin")
#
#     def aloqa(self):
#         print("Iltimos hisobingizni to'ldiring")
#
#     def SMS_yoz(self):
#         print("SMS yozasizmi")
#
#
# class Smart_Phone(Phone):
#     def __init__(self):
#         super().__init__()
#         self.sensr = "sensr"
#         self.steklo = input("steclo qanaqa bo'lisin")
#
#     def cibr_game(self):
#         print("O'yin O'yna")
#
#     def zamonavi_saytlar(self):
#         print("Saytlarga kirish")
#
#
# class Table(Smart_Phone):
#     def __init__(self):
#         super().__init__()
#         self.kebord = input("best kebo'rd")
#         self.big_ekran = input("Ekran telefo'nnikidan kotta")
#
#     def pen(self):
#         print("ruchkali ekran")
#
#     def long_energy(self):
#         print("Quvvati ko'p")
#
#
# class Leptop(Compiuter):
#     def __init__(self):
#         super().__init__()
#         self.zaryad = input("zaryadi")
#         self.avlodi = input("Nechinchi avlod ")
#
#     def tapchat(self):
#         print("Tapchat ishlamoqda")
#
#     def xususiati(self):
#         print("Ekran Ochilib yopiladi")
#
#
# class Desctop(Compiuter):
#     def __init__(self):
#         super().__init__()
#         self.big_ram = input("Qancha Ram kere")
#         self.big_ssd = input("Qancha SSD kere")
#
#     def prosessor(self):
#         print("Kotta bollaniki")
#
#     def monitor(self):
#         print("Mnitor prosessorga ulan magan ")
#
#
# hp = Desctop()
# apple = Table()
# samsung = Leptop()
# mi = Smart_Phone()
# desctop = Desctop




# V26
# class Human:
#     def __init__(self, name, age, profession):
#         self.adult_age = age
#
#     def is_adault(self):
#         if self.adult_age >= 18:
#             print("Voyaga yetgan")
#         else:
#             print("Voyaga yetmagan")
#
#
# odam1 = Human("Salohiddin", 18, "Dasturchi")
# odam1.is_adault()
# odam2 = Human("Jasur", 17, "Tadbirkor")
# odam2.is_adault()
# odam3 = Human("Ali", 20, "Usta")
# odam3.is_adault()
# odam4 = Human("Qaxxor", 10, "Sotuvchi")
# odam4.is_adault()


# V27
# class Odam:
#     def __init__(self, raqam):
#         self.raqam = raqam
#
#     def tepish(self, koptok):
#         print(f"{self.raqam} - raqamli o'yinchi to'pni tepdi")
#         koptok.uchsin()
#
#
# class Koptoc:
#     def uchsin(self):
#         print("Koptok uchdi")
#
#
# odam = Odam(15)
# nima = Koptoc()
# odam.tepish(nima)

# V28
# class Players:
#     def __init__(self, name):
#         self.jon = 100
#         self.qurol = "pistolet"
#         self.name = name
#
#     def otish(self, player1):
#         player1.kamayish()
#
#     def kamayish(self):
#         self.jon -= 10
#
#     def qogan_jon(self):
#         print(self.jon)
#
#
# player = Players("Jabbor")
# players1 = Players("Sarvar")
#
# player.otish(players1)
# players1.otish(player)
#
# players1.qogan_jon()
# player.qogan_jon()

# V29
# class Odam:
#     def __init__(self, isim):
#         self.name = isim
#
#     def kuylash(self):
#         print(f"{self.name} kuyladi")
#
#     def eshitish(self, inson):
#         print(f"{self.name} eshitti")
#         inson.gapirish()
#
#     def gapirish(self):
#         print(f"{self.name} Yahshiroq kuyla")
#
#
# Anvar = Odam("Azamat")
# Jasur = Odam("Jasur")
# Anvar.kuylash()
# Jasur.eshitish(Anvar)

# V30
# import time
#
# class Odam:
#     def __init__(self):
#         self.isim = input("Isim kiriting")
#
#     def yugurish(self):
#         print(f"{self.isim} yugur")
#         time.sleep(5)
#         self.yiqilish()
#
#
#     def yiqilish(self):
#         print(f"{self.isim} yiqilding")
#
#
# kimdir = Odam()
# kimdir.yugurish()

num = "Salom"
son = "Enter"
son = son[::-1]
for i in range(len(num)):
    print(f"{num[i]}{son[i]}",end="")
