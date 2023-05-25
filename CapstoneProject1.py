import sys
from datetime import datetime

def waktu_minjam(W1):
    while True:
        global B_minjam
        B_minjam=input('Masukkan tanggal pengembalian buku terbaru dengan format (yyyy-mm-dd): ') #klo format ga sesuai error, harus ikut aturan kalender juga
        
        # Ubah string menjadi objek tanggal
        tanggal1 = datetime.strptime(W1, "%Y-%m-%d").date()
        tanggal2 = datetime.strptime(B_minjam, "%Y-%m-%d").date()

        # Hitung selisih antara dua tanggal
        selisih = (tanggal2 - tanggal1).days
        if selisih==0:
            print(f'Tanggal pengembalian tidak boleh tanggal hari ini {W1}')
        elif 0<selisih<=7:
            print(f'Anda memperpanjang buku perpus selama {selisih} hari')
            break
        elif selisih<0:
            print('Miminimal waktu peminjaman 1 hari dari hari ini')
        else:
            print('Maksimal waktu peminjaman 7 hari dari hari ini')



def minjam(Nama,NIS,listBuku,tgl_skrg):
    while True:
        
        while True:
            print(
                            """

                    Silahkan {} pilih menu dibawah ini :

                    1. Lanjut meminjam buku
                    2. Kembali ke menu utama
                    
                """.format(Nama)
                    )
            A2=int(input(""))
            if A2== 1:
                break
            elif A2==2:
                main()
            else:
                print('Nomor yang anda masukkan salah')




        E=listBuku.copy()
        printFormat = "{:<4}" + "{:<17}" * (len(E['column']))
        k=1
        l=0
        for value in E.values():
            if E['column']==value:
                print(printFormat.format("", *value))
            else:
                if 'Tersedia' in value: 
                    value[0]=k
                    k+=1
                    l=l+1
                    print(printFormat.format("", *value))
                else:
                    value[0]=0
        if l==0:
            print('Maaf tidak ada stok buku yang tersedia')            
            continue           
        

        A= int(input('Masukkan nomor indeks sesuai buku yang ingin dipinjam: '))
        
        i=0
        for value in E.values():
            if A in value:
                i=1
                while True:
                    print(
                            """
                    Apakah Anda yakin meminjam buku dengan judul {} NISB {}?
                    Silahkan pilih menu dibawah ini :

                    1. Ya
                    2. Tidak
                    
                """.format(value[1],value[3])
                    )
                    A1=int(input('Silahkan pilih menu: '))
                    
                    if A1==1:
                        for valueD in listBuku.values():
                            
                            if value[3] in valueD:
                                #B=input('Masukkan tanggal pengembalian buku dengan format (yyyy-mm-dd): ')
                                waktu_minjam(tgl_skrg)
                                while True:
                                    # B=input('Masukkan tanggal pengembalian buku dengan format dd-mm-yyyy: ')
                                    print(
                                            """
                                    Apakah Anda yakin paling lambat mengembalikan buku dengan judul {} NISB {} pada tanggal {}?
                                    Perhatikan format tanggalnya (yyyy-mm-dd)")
                                    Silahkan pilih menu dibawah ini:
                                    1. Ya
                                    2. Tidak
                                    """.format(value[1],value[3],B_minjam)
                                    )
                                    A2=int(input('Silahkan pilih menu: '))
                                    if A2==1:
                                        valueD[4]="Dipinjam"
                                        valueD[5]=Nama
                                        valueD[6]=NIS
                                        valueD[7]=tgl_skrg
                                        valueD[8]=B_minjam
                                        print(
                                            """
                                            Selamat Anda telah berhasil meminjam buku dengan judul {} NISB {}
                                            Pastikan Anda tepat waktu untuk mengembalikan buku tersebut paling lambat pada tanggal {}
                                        """.format(value[1],value[3],B_minjam)
                                        )
                                        show(listBuku, printFormat)
                                        break
                                    elif A2==2:
                                        print('Anda tidak jadi meminjam buku dengan judul {} NISB {}, mohon pastikan tanggal pengembalian buku saat meminjam'.format(value[1],value[3]))
                                        break
                                    else:
                                        print('Nomor yang anda masukkan salah')

                                    
                        
                        
                        break

                    elif A1==2:
                        print("Anda tidak jadi meminjam buku dengan judul {} NISB {}".format(value[1],value[3]))
                        break

                    else:
                        print('Nomor yang anda masukkan salah')



        if i!=1:
            print(f'Tidak ada buku yang tersedia dengan nomor indeks {A}')
            
    

def waktu_kembali(W1,val):
    
    WD=(datetime.strptime(val, "%Y-%m-%d").date()-datetime.strptime(W1, "%Y-%m-%d").date()).days
    if WD>=0:
        print('Terima kasih sudah mengembalikan buku tepat waktu')
    else:
        print(f'Anda dikenakan denda karena telat {abs(WD)} hari dari tanggal pengembalian, seharusnya paling lambat Anda mengembalikan buku pada tanggal {val}, untuk info lanjut mengenai denda silahkan temui petugas perpustakaan yang berwenang setelah berhasil mengembalikan buku')
    
def kembali(Nama, NIS,listBuku,tgl_skrg):
    while True:
        while True:
            print(
                            """

                    Silahkan {} pilih menu dibawah ini :

                    1. Lanjut mengembalikan buku
                    2. Kembali ke menu utama
                    
                """.format(Nama)
                    )
            A2=int(input(""))
            if A2== 1:
                break
            elif A2==2:
                main()
            else:
                print('Nomor yang anda masukkan salah')


        E=listBuku.copy()
        printFormat = "{:<4}" + "{:<17}" * (len(E['column']))
        k=1
        l=0
        for value in E.values():
            if E['column']==value:
                print(printFormat.format("", *value))
            else:
                if NIS in value: 
                    value[0]=k
                    k+=1
                    l=l+1
                    print(printFormat.format("", *value))
                else:
                    value[0]=0
        if l==0:
            print('Tidak ada buku yang bisa dikemnbalikan, Anda belum meminjam buku satupun')
            continue

        
                    
        A= int(input('Masukkan nomor indeks sesuai buku yang ingin dikembalikan: '))
        
        i=0
        for value in E.values():
            if A in value:
                i=1
                while True:
                    print(
                            """
                    Apakah Anda yakin mengembalikan buku dengan judul {} NISB {} hari ini?
                    Silahkan pilih menu dibawah ini :

                    1. Ya
                    2. Tidak
                    
                """.format(value[1],value[3])
                    )
                    A1=int(input('Silahkan pilih menu: '))
                    
                    if A1==1:
                        for valueD in listBuku.values():
                            
                            if value[3] in valueD:
                                
                                waktu_kembali(tgl_skrg,value[8])
                                
                                valueD[4]="Tersedia"
                                valueD[5]=" "
                                valueD[6]=" "
                                valueD[7]=" "
                                valueD[8]=" "
                                print(
                                    """
                                    Selamat Anda telah berhasil mengembalikan buku dengan judul {} NISB {}
                                    
                                    
                                """.format(value[1],value[3])
                                )
                          
                        break

                    elif A1==2:
                        print("Anda tidak jadi mengembalikan buku dengan judul {} NISB {}".format(value[1],value[3]))
                        break

                    else:
                        print('Nomor yang anda masukkan salah')



        if i!=1:
            print(f'Tidak ada buku yang anda pinjam dengan nomor indeks {A}')
        



def waktu_panjang(W1,val):
    
    WD=(datetime.strptime(val, "%Y-%m-%d").date()-datetime.strptime(W1, "%Y-%m-%d").date()).days
    if WD>=0:
        print('Anda dapat memperpanjang buku tanpa dikenakan denda')
    else:
        print(f'Anda dikenakan denda karena telat selama {abs(WD)} dari tanggal pengembalian sebelumnya, untuk info lanjut mengenai denda silahkan temui petugas perpustakaan yang berwenang setelah berhasil meminjam buku')
    while True:
        
        global B_panjang
        B_panjang=input('Masukkan tanggal pengembalian buku terbaru dengan format (yyyy-mm-dd): ') #klo format ga sesuai error, harus ikut aturan kalender juga
        
        # Ubah string menjadi objek tanggal
        tanggal1 = datetime.strptime(W1, "%Y-%m-%d").date()
        tanggal2 = datetime.strptime(B_panjang, "%Y-%m-%d").date()

        # Hitung selisih antara dua tanggal
        selisih = (tanggal2 - tanggal1).days
        if selisih==0:
            print(f'Tanggal pengembalian tidak boleh tanggal hari ini {W1}')
        elif 0<selisih<=7:
            print(f'Anda memperpanjang buku perpus selama {selisih} hari')
            break
        elif selisih<0:
            print('Miminimal waktu peminjaman 1 hari dari hari ini')
        else:
            print('Maksimal waktu peminjaman 7 hari dari hari ini')


def panjang(Nama,NIS,listBuku,tgl_skrg):
    while True:
        while True:
            print(
                            """

                    Silahkan {} pilih menu dibawah ini :

                    1. Lanjut memperpanjang buku
                    2. Kembali ke menu utama
                    
                """.format(Nama)
                    )
            A2=int(input(""))
            if A2== 1:
                break
            elif A2==2:
                main()
            else:
                print('Nomor yang anda masukkan salah')


        E=listBuku.copy()
        printFormat = "{:<4}" + "{:<17}" * (len(E['column']))
        k=1
        l=0
        for value in E.values():
            if E['column']==value:
                print(printFormat.format("", *value))
            else:
                if NIS in value: 
                    value[0]=k
                    k+=1
                    l=l+1
                    print(printFormat.format("", *value))
                else:
                    value[0]=0
        if l==0:
            print('Anda belum meminjam buku satupun')
            continue
            
                    
        A= int(input('Masukkan nomor indeks sesuai buku yang ingin diperpanjang: '))
        
        i=0
        for value in E.values():
            if A in value:
                i=1
                while True:
                    print(
                            """
                    Apakah Anda yakin memperpanjang buku dengan judul {} NISB {}?
                    Silahkan pilih menu dibawah ini :

                    1. Ya
                    2. Tidak
                    
                """.format(value[1],value[3])
                    )
                    A1=int(input('Silahkan pilih menu: '))
                    
                    if A1==1:
                        for valueD in listBuku.values():
                            
                            if value[3] in valueD:
                                
                                waktu_panjang(tgl_skrg,value[8])
                                #B=input('Masukkan tanggal pengembalian buku terbaru dengan format (yyyy-mm-dd): ')
                                while True:
                                    # B=input('Masukkan tanggal pengembalian buku dengan format dd-mm-yyyy: ')
                                    print(
                                            """
                                    Apakah Anda yakin paling lambat mengembalikan buku dengan judul {} NISB {} pada tanggal {}?
                                    
                                    Silahkan pilih menu dibawah ini:
                                    1. Ya
                                    2. Tidak
                                    """.format(value[1],value[3],B_panjang)
                                    )
                                    A3=int(input('Silahkan pilih menu: '))
                                    if A3==1:
                                        valueD[7]="2023-05-24"
                                        valueD[8]=B_panjang
                                        print(
                                            """
                                            Selamat Anda telah berhasil memperpanjang buku dengan judul {} NISB {}
                                            Pastikan Anda tepat waktu untuk mengembalikan buku tersebut paling lambat pada tanggal {}
                                        """.format(value[1],value[3],B_panjang)
                                        )
                                        show(listBuku, printFormat)
                                        break
                                    elif A3==2:
                                        print('Anda tidak jadi memperpanjang buku dengan judul {} NISB {}, mohon pastikan tanggal pengembalian buku terbaru saat meminjam'.format(value[1],value[3]))
                                        break
                                    else:
                                        print('Nomor yang anda masukkan salah')

                                    
                        
                        
                        break

                    elif A1==2:
                        print("Anda tidak jadi memperpanjang buku dengan judul {} NISB {}".format(value[1],value[3]))
                        break

                    else:
                        print('Nomor yang anda masukkan salah')



        if i!=1:
            print(f'Tidak ada buku yang anda pinjam dengan nomor indeks {A}')




def show(Dict, printFormat, title="\nDaftar Semua Buku\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Buah yang Tersedia\n".
    """
    # Menampilkan judul
    print(title)
    k=1
    for ValuesD in listBuku.values():
        if listBuku['column']!=ValuesD:
            ValuesD[0]=k
            k=k+1    
    # Loop item di dalam listFruit
    for value in Dict.values():
        # Menampilkan item berdasarkan format
        print(printFormat.format("", *value))

def nambah():
    
    while True:
        print(
                        """

                Silahkan {} pilih menu dibawah ini :

                1. Lanjut menambahkan buku
                2. Kembali ke menu utama
                
            """.format(nama)
                )
        A2=int(input(""))
        if A2== 1:
            
            Judul = input("Masukkan judul buku: ").capitalize()
            Edisi = int(input("Masukkan tahun edisi buku: "))
            NISB_ = input("Masukkan NISB buku: ")
            Status = 'Tersedia'
            NIS_=' '
            Peminjam=' '
            Tgl_pinjam=' '
            Tgl_kembali=' '
            # # Loop item di dalam listFruit
            # for key, value in listFruit.items():
            #     # Apabila buah sudah ada di dalam daftar
            #     if Judul in value:
            #         listFruit[key][2] += Edisi
            #         listFruit[key][3] = Kode
            #         break
            # # Apabila buah tidak ada di dalam daftar
            # else:
            while True:
                print("""

                    Anda menambahkan buku dengan:
                    Judul   :  {}
                    Edisi   :  {}
                    NISB    :  {}

                    Apakah Anda yakin menambahkan buku tersebut?
                    Silahkan pilih menu dibawah ini :
                    1. Ya
                    2. Tidak
                    
                """.format(Judul,Edisi,NISB_))
                n1=int(input('Silahkan pilih menu: '))
                if n1==1:
                    print("Anda berhasil menambahkan buku tersebut")
                    index = len(listBuku) - 1
                    listBuku.update({
                                    f'buku-{index}': [
                                        index, 
                                        Judul,
                                        Edisi,
                                        NISB_,
                                        Status,
                                        Peminjam,
                                        NIS_,
                                        Tgl_pinjam,
                                        Tgl_kembali
                                    ]
                                    }
                                )
                    show(listBuku, printFormat)
                    break

                elif n1==2:
                    print("Anda tidak jadi menambahkan buku tersebut")
                    break

                else:
                    print('Nomor yang anda masukkan salah')


        elif A2==2:
            main()
        else:
            print('Nomor yang anda masukkan salah')
            continue
    
  
def delete(B):
    while True:
        printFormat1 = "{:<4}" + "{:<17}" * (len(B['column']))   
        for value in B.values():
                    # Menampilkan item berdasarkan format
            print(printFormat1.format("", *value))

        index = int(input("Masukkan indeks buku yang ingin dihapus: "))
        F=[]
        i=0
        for v in B.values():
            F.insert(i,v)
            i=i+1

        
        for j, val in enumerate(F):
            if j==index:
                global listBuku
                if val[4]=="Tersedia":
                    while True:
                        print("""
                        Apakah Anda yakin ingin menghapus Buku {} dengan NISB {}?
                        1. Ya
                        2. Tidak
                        """.format(val[1],val[3]))
                        A=int(input("Silahkan masukkan angka sesuai indeks yg tersedia: "))
                        if A==1:
                            del F[index]
                            # print(len(F))
                            
                            listBuku={}
                            listBuku['column']=F[0]
                            for i in range(1,len(F)):
                                listBuku[f'buku-{i}']=F[i]
                            break
                        if A==2:
                            print("Anda tidak jadi menghapus buku tersebut")
                            break
                        else:
                            print("Silahkan masukkan angka kembali")
                    continue
                else:
                    print('Buku yang Anda pilih tidak bisa dihapus karena bukunya sedang dipinjam')
                    
                    listBuku=B
                
        break
                    


def delete1(C,N):
    
    while True:
            print(
                            """

                    Silahkan {} pilih menu dibawah ini :

                    1. Lanjut menghapus buku
                    2. Kembali ke menu utama
                    
                """.format(N)
                    )
            A2=int(input(""))
            if A2== 1:
                delete(C)
                k=1
                
                for ValuesD in listBuku.values():
                    if listBuku['column']!=ValuesD:
                        ValuesD[0]=k
                        k=k+1    

                printFormat1 = "{:<4}" + "{:<17}" * (len(listBuku['column']))   
                for value in listBuku.values():
                            # Menampilkan item berdasarkan format
                    print(printFormat1.format("", *value))
                C=listBuku

            elif A2==2:
                main()
                break
            else:
                print('Nomor yang anda masukkan salah')




    
    
def main():
    while True:
        # Menampilkan tampilan utama program
        print(
            """

Halo, selamat datang {} di Perpustakaan Universitas Sains Yogyakarta
Waktu Kunjungan Anda: {} 

Silahkan pilih menu yang ingin dijalankan dengan memasukkan angka sesuai menu:

1. Menampilkan daftar buku 
2. Meminjam buku
3. Mengembalikan buku
4. Memperpanjang buku
5. Menambah buku
6. Menghapus buku
7. Log in ulang
8. Exit
""".format(nama, waktu_kunjung)
        )
        # Input fitur yang akan dijalankan
        menuNumber = input(" ")
        
        # Fitur menampilkan daftar buku
        if menuNumber == str(1):
            show(listBuku, printFormat)
        # Fitur meminjam buku
        elif menuNumber == str(2):
            minjam(nama,nis,listBuku,waktu_kunjung)
        # Fitur mengembalikan buku
        elif menuNumber == str(3):
            kembali(nama,nis,listBuku,waktu_kunjung)
        # Fitur memperpanjang buku
        elif menuNumber == str(4):
            panjang(nama,nis,listBuku,waktu_kunjung)
        # Fitur menambah buku
        elif menuNumber == str(5):
            while True:
                print("""
                Untuk mengakses menu menambahkan buku Anda harus memasukkan password
                Pilih menu berikut
                1. Lanjut memasukkan password
                2. Kembali ke menu utama
                """)
                P=int(input(""))
                if P==1:
                    Pass=input("Silahkan Masukkan password untuk bisa menambahkan buku, jika lupa password klik 0 untuk kembali ke menu utama: ")
                    if Pass=="jcds01":
                        print("""
                Password yang Anda masukkan benar
                """)
                        nambah()
                    elif Pass=='0':
                        main()
                    else:
                        print("""
                Password yang Anda masukkan salah
                Silahkan coba lagi
                """)
                elif P==2:
                    main()

                else:
                    print("""
                Tidak ada pilihan {} pada menu
                Silahkan coba kembali
                """.format(P))
                    
        
                
                
            
        # Fitur menghapus buku
        elif menuNumber == str(6):
            while True:
                print("""
                Untuk mengakses menu menghapus buku Anda harus memasukkan password
                Pilih menu berikut
                1. Lanjut memasukkan password
                2. Kembali ke menu utama
                """)
                P=int(input(""))
                if P==1:
                    Pass=input("Silahkan Masukkan password untuk bisa menghapus buku, jika lupa password klik 0 untuk kembali ke menu utama: ")
                    if Pass=="jcds01":
                        print("""
                Password yang Anda masukkan benar
                """)
                        delete1(listBuku,nama)
                    elif Pass=='0':
                        main()
                    else:
                        print("""
                Password yang Anda masukkan salah
                Silahkan coba lagi
                """)
                elif P==2:
                    main()

                else:
                    print("""
                Tidak ada pilihan {} pada menu
                Silahkan coba kembali
                """.format(P))
            
        elif menuNumber == str(7):
            login()
        elif menuNumber == str(8):
            sys.exit()
        else:
            print("""
Tidak ada pilihan {} pada menu
Silahkan coba kembali
""".format(menuNumber))


if __name__ == "__main__":
    # Deklrasi variabel 'listBuku'
    
    listBuku = {
        'column': ["No", "Judul Buku", "Edisi Buku", "NISB", "Status", "Peminjam","NIS", "Tanggal Pinjam", "Tanggal Pengembalian"],
        'buku-0': [1, "Buku Kimia", 2016, "K01", "Tersedia", " ", " ", " ", " " ],
        'buku-1': [2, "Buku Fisika", 2017, "F01", "Dipinjam", "Andi", "1234", "2023-05-21", "2023-05-23"],
        'buku-2': [3, "Buku Sejarah", 2018, "S01", "Tersedia", " ", " "," ", " " ],
        'buku-3': [4, "Buku Matematika", 2019, "M01", "Dipinjam", "Andi","1234", "2023-05-14", "2023-05-24"],
    }

  
    # Deklarasi format tampilan di prompt
    printFormat = "{:<4}" + "{:<16}" * (len(listBuku['column']))
def login():
    
    #Memasukkan data dan tanggal kunjungan
    print("""
    ##########################################
    SELAMAT DATANG DI PERPUSTAKAAN SAINS YOGYA
    ##########################################
    """)
    global nama
    global nis
    global waktu_kunjung
    waktu_kunjung='2023-05-24' 
    nama=input("Silahkan Masukkan nama Anda sesuai NIS/NIK: ")
    nis=input('Silahkan Masukkan NIS/NIK Anda: ')
    while True:
        print("""

        Nama : {}
        NIS  : {}

        Apakah data yang Anda masukkan benar?
        1. Ya
        2. Tidak
        
        """.format(nama,nis))
        L=int(input(""))
        if L==1:
            main()
        elif L==2:
            login()
        else:
            print("""
        Tidak ada pilihan {} pada menu
        Silahkan coba kembali
        """.format(L))
    
    

    # Menjalankan fungsi utama main()

login()
    