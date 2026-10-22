
summa = float(input("Xarid summasini kiriting: "))
vip = input("VIP mijozmisiz? (ha/yo'q): ").lower()
if summa <= 100000:
    chegirma = 0
elif summa <= 500000:
    chegirma = 5
else:
    chegirma = 10
if vip == "ha":
    chegirma += 5
tolov = summa - (summa * chegirma / 100)

print(f"Chegirma: {chegirma}%.")
print(f"To'lanadigan summa: {tolov} so'm.")
