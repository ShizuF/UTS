suhu = [25.2, 16.8, 23.9, 28, 19.6]

while True:
    print("Pilihan 1: Menampilkan data list suhu")
    print("Pilihan 2: Masukkan kondisi suhu mu saat ini")
    print("Pilihan 3: Exit")
    pilihan = input("Masukan Pilihan mu (1/2/3): ")

    suhu.sort ()

    if pilihan == "1":
        print("List Suhu:", suhu,'\n')
        print(" suhu(28)",'\n')
        print(" suhu(25.2)",'\n')
        print(" suhu(23.9)",'\n')
        print(" suhu(19.6)",'\n')
        print(" suhu(16.8)",'\n')

    elif pilihan == "2":
        suhu_input = float(input("Masukkan kondisi suhu anda = ?:"))

        if suhu_input < 27:
            print("Suhu Dingin")
        elif 27 <= suhu_input <= 33:
            print("Suhu Normal")
        else:
            print("suhu Panas")

    elif pilihan == "3":
        exit = input ("selamat tinggal")
        print(input("selamat tinggal"))

        break
    else:
        print("Pilihan tidak valid. Pilih 1, 2, atau 3.")
