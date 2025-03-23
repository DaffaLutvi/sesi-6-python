nama = "Nugraha ", "john    ","Jane    ","Doe     "
tahun_sekarang = 2025
tahun_lahir =  tahun_sekarang - 1989,tahun_sekarang - 1990,tahun_sekarang - 1992,tahun_sekarang - 1994
print('No     | Nama      | Age |')
for i, (x,y) in enumerate(zip(nama,tahun_lahir)):
    print(i+1,"     |",x," |",y," |")