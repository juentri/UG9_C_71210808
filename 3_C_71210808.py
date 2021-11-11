aa = float(input("Masukan alas atap: "))
ta = float(input("Masukan tinggi atap: "))
te = float(input("Masukan tinggi tembok: "))

luas = 0.5 * (aa * ta)
persegi = te * te

print("rumah tersebut membutuhkan" ,str((luas + persegi) / 5), "sak semen")