simpan = [12,"Udin petot",14.5,True,'A',"102"]
for i in simpan [2:5]:
    print(i)

for i in range (1,4) :
    for j in range (1,4) :
        print(f"{i} x {j} = {i * j}")
    print()

minuman = ["mie","sop","bakso"]
makanan = ["es teh" , "air putih", "es jeruk"]

for i in makanan :
    for j in minuman :
        print(f"{i} & {j}")
 
print("menu rumah makan informatika 2024 :")
simpan = ["Nasi Goreng","Mie Goreng","Mie Ayam","Bakso","Soto"]
for i in simpan :
    print(i)

print("menu rumah makan informatika 2024 :")
simpan = ["Nasi Goreng","Mie Goreng","Mie Ayam","Bakso","Soto"]
for i, menu in enumerate(simpan,start=1) :
    print(f"{i}.{menu}")
    
print("menu rumah makan informatika 2024 :")
simpan = ["Nasi Goreng","Mie Goreng","Mie Ayam","Bakso","Soto"]
for i in range (len(simpan)) :
    print(f"{i+1}. {simpan [i]}")

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")

jawab = 'ya'
hitung = 0
while(True):
    hitung += 1
    jawab = input("Balikkan lagi tidak? ")
    if jawab == "ga" or jawab == "engga" or jawab == "G":
        print(f"Total perulangan: {hitung}")
    else :
          break

print("Daftar bilangan prima dari 1-10")
for i in range(10):
    if i % 1  == 0:
        continue
    print(i)
    
hitung = 0
angka = 0
while(True) :
    hitung += 1
    angka = input("Angka Berapa? : ")
    if angka >= 0 :
        print("angka berhasil di input")
    else :
          break 