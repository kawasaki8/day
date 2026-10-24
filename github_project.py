mahsulotlar = {
    "non": 3000,
    "sut": 12000,
    "tuxum": 1500,
    "shakar": 14000,
    "yog'": 18000
}

mahsulot = input("Mahsulot nomini kiriting: ").lower()

if mahsulot in mahsulotlar:
    print("Mahsulot narxi:", mahsulotlar[mahsulot], "so'm")
else:
    print("Mahsulot topilmadi")

