a = {}
x = 0
no = x
while True:
    x = 1
    tanya = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
    if (tanya == "k"):
        break
    if (tanya == "l"):
        print("Daftar Nilai")
        print("=====================================================================")
        print("| No |   NIM   |\tNama\t|  Tugas  |  UTS  |  UAS   |  Akhir |")
        print("=====================================================================")
        print("|                           TIDAK ADA DATA                           |")
        print("=====================================================================")
    if (tanya == "t"):
        for i in range(x):
            no = i + 1
            a = {
                'NIM' : int(input("NIM: ")),
                'Nama' : input("Nama: "),
                'UTS' : int(input("Nilai UTS: ")),
                'UAS' : int(input("Nilai UAS: ")),
                'Tugas' : int(input("Nilai Tugas: "))
            }
        for i in range (x):
            akhir = a['UTS'] * 35/100 + a['UAS'] * 35/100 + a['Tugas'] * 30/100
        tanya = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
        if tanya == "l":
            print("Daftar Nilai")
            print("=====================================================================")
            print("| No |   NIM   |\tNama\t|  Tugas  |  UTS  |   UAS  |  Akhir |")
            print("=====================================================================")
            print("|",no," |  ",a['NIM']," |\t",a['Nama'],"\t|   ",a['Tugas'],"  |  ",a['UTS']," |  ",a['UAS'],"  | {:.2f}  |".format(akhir))
            print("=====================================================================")
    if (tanya == "u"):
        a['NIM'] = int(input("Ubah NIM: "))
        a['Nama'] = input("Ubah Nama: ")
        a['UTS'] = int(input("Ubah UTS: "))
        a['UAS'] = int(input("Ubah UAS: "))
        a['Tugas'] = int(input("Ubah Tugas: "))
        akhir = a['UTS'] * 35/100 + a['UAS'] * 35/100 + a['Tugas'] * 30/100
        tanya = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
        if tanya == "l": 
            print("Daftar Nilai")
            print("=====================================================================")
            print("| No |   NIM   |\tNama\t|  Tugas  |  UTS  |  UAS   |  Akhir |")
            print("=====================================================================")
            print("|",no," |  ",a['NIM']," |\t",a['Nama'],"\t|   ",a['Tugas'],"  |  ",a['UTS']," |  ",a['UAS'],"  | {:.2f}  |".format(akhir))
            print("=====================================================================")
    if tanya == "c":
        cari = int(input("Cari NIM: "))
        if cari == a['NIM']:
            print("Nama:",a.get('Nama'))
            print("Nilai Tugas:",a.get('Tugas'))
            print("Nilai UTS:",a.get('UTS'))
            print("Nilai UAS:",a.get('UAS'))
            print("Nilai Akhir:",akhir)
    if (tanya == "h"):
        a.clear()
        print("Daftar Nilai")
        print("=====================================================================")
        print("| No |   NIM   |\tNama\t|  Tugas  |  UTS  |  UAS   |  Akhir |")
        print("=====================================================================")
        print("|                           TIDAK ADA DATA                           |")
        print("=====================================================================")