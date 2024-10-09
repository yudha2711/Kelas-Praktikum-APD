# # contoh 1
# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# # contoh 2
# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"

# print(daftar_buku)

# # contoh 3
# musik = {
#     "judul" : "All we Know",
#     "judu2" : "Something Just Like This"
# }

# print(musik["judul"])
# print(musik["judu2"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }


# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})

# #Setelah Ditambah
# print(Film)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Setelah diubah
# print(Film)
# print("Jumlag Film =", len(Film))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(Nilai)

# Nilai.update({"Matematika" : 90})
# print(Nilai)

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)


matkul = {
    "Matematika" : 90,
    "Fisika" : 80,
    "Biologi" : 80,
    "Kimia" : 70
}

# total = sum(matkul.values())
# print("Nilai total : ", total)
# rata = total / len(matkul)
# print("Nilai rata-rata : ", rata)

total = 0
for nilai in matkul.values :
    total += nilai
print(f"Total keseluruhan adalah {total}")
print(f"rata rata nilai adalah {total/4}")

# Biodata = {
#      "Nama" : "Aldy Ramadhan Syahputra",
#      "NIM" : 2109106079,
#      "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#      "Mahasiswa_Aktif" :True,
#      "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "Izanami#6848",
#         "Email" : "Apalahkocak@gmail.com"
#      }
# }
# # print(Biodata["KRS"][0])
# print(Biodata ["Social Media"]["Email"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS",
# valorant = {"Nama" : {123 : "Informatika"}})
# print(games['valorant']['Nama'][123])

# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legends",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "Strategy"
#     }      
# }

# print((Games.get('Game3')).get('genre'))


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for mapel in Nilai:
#     print(mapel)
# print("")
# #menggunakan items
# for mapel, nilai in Nilai.items():
#     print(f"Nilai {mapel} anda adalah {nilai}")

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# key = "apel","sirsak","wortel"
# value = 1,2,3
# buah = dict.fromkeys (value,key)
# print(buah)

# Nilai = {
#      "Matematika" : 80,
#      "B. Indonesia" : 90,
#      "B. Inggris" : 81,
#      "Kimia" : 78,
#     "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)

# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)


# Musik = {
#    "Ariana Grande" : ["Thank U,next", "One Last Time"],
#    "Billie Eillish" : ["Bad Guy", "Birds of a Feather"],
#    "SZA" : ["Saturn", "Kill Bill"]
# }
# for i, j in Musik.items():
#    print(f"Musik milik {i} adalah : ")
#    for song in j:
#        print(song)
# print("")


# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for nama, umur in mahasiswa.items():
#     print("ID Mahasiswa : ",nama)
#     for nama, umur in umur.items():
#         print (nama, " : ", umur)
# print("")