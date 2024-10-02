nama = ["Shandy",103,True,["yuyun",145],3.96,[123,"ALVITO",False,3.66],"rehan"]
print(nama[5][0])

matkul = ["APD",
          "APL",
          "WEB",
          "JARKOM",
          "BASDAT",
          "STRUKDAT",
          "PTI",
          "KALKULUS",
          "PROBAS"
]
print(matkul[0])


makanan = ["Bakso","Sate","Soto","Nasi goreng","mie ayam","Cumi goreng"]
print("Sebelum :")
print(makanan)
makanan.append("Nasi goreng")
print("Sesudah :")
makanan.clear(
print(makanan)
)
print(makanan)
makanan.insert(1,"Nasi Goreng")
print(makanan)
data = makanan.pop("5")
print (makanan)
print(data)
makanan[0]= ["Nasi Goreng"]
print(makanan)
del makanan[5]
print(makanan)


minuman = ["susu","jus mangga","jus sirsak"
           ,"es teler","es teh","es buah"]
print("sebelum")
print(minuman)
del minuman[2]
print("sesudah")
print(minuman)
minuman[4] = "air putih"
minuman.insert(0,"jus tomat")
print(minuman)

makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"],["teh","kopi","air"]]
for x in makanan : 
    if isinstance(x, list) :
       for y in x :
        print(y)
    else :
       print(x)

# for x in makanan :
#     for y in x :
# print(x, end="")

akuns = []

while True:
   print("Halo selamat datang di aplikasi catatan")
   print("Silahkan pilih 'Daftar Akun' jika belum buat akun,dab jika sudah memiliki akun silahkan login deks")
   print("1. Daftar akun")
   print("2.Login")
   print("3.Exit")
   print("____________________________")
   opsi = input("pilih opsi :")
   print(" ")

   if opsi == "1":
      print("Halo pengguna baru! yukk buat akun dulu!")
      username = input("Username :")
      akuna = False
      for akun in akuns :
           if akun[0] == username :  #    Memeriksa apakah username ada
              akuna = True
              break
       if akuna:
         print("Nama sudah terpakai untuk registrasi silahkan coba lagi")
       else:
         password = input("password")
         akuns.append({username, password, []})
         print(f"Akun anda berhasil tedaftar dengan ID: {username}")