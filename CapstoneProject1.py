import sys
from datetime import datetime
def delete1(C,nama):
    
    while True:           
        print(
                        """

                Silahkan {} pilih menu dibawah ini :

                1. Lanjut menghapus buku
                2. Kembali ke menu utama
                
            """.format(nama)
                )
        A2=int(input(""))

        if A2== 1:
            
            index = input("Masukkan NISB buku yang ingin dihapus: ")
            F=[]
            i=0
            for v in C.values():
                F.insert(i,v)
                i=i+1
            
            k=0
        
            for j, val in enumerate(F):
                if val[3]==index:
                    k=k+1
                    global listBuku
                    if val[4]=="Tersedia":
                            print("""
                            Apakah Anda yakin ingin menghapus Buku {} Edisi {} dengan NISB {}?
                            1. Ya
                            2. Tidak
                            """.format(val[1],val[2],val[3]))
                            A=int(input("Silahkan masukkan angka sesuai indeks yg tersedia: "))
                            if A==1:
                                del F[val[0]]
                                
                                
                                listBuku={}
                                listBuku['column']=F[0]
                                for i in range(1,len(F)):
                                    listBuku[f'buku-{i}']=F[i]
                                print("""Data dengan judul {} Edisi {} NISB {} berhasil dihapus""".format(val[1],val[2],val[3]))
                                
                                delete1(listBuku,nama)
                            if A==2:
                                print("Anda tidak jadi menghapus buku tersebut")
                                delete1(listBuku,nama)
                    else:
                        print('Buku yang Anda pilih tidak bisa dihapus karena bukunya sedang dipinjam')
                        delete1(listBuku,nama)
            if k==0:
                print(f'Buku dengan NISB {index} tidak tersedia')
                delete1(listBuku,nama)

        elif A2==2:
            main()
            
        else:
            print('Nomor yang anda masukkan salah')


#Fungsi show akan dipanggil saat user memilih menu "Menampilkan daftar buku" pada fungsi main atau
    # dipanggil saat user yakin sudah melakukan perubahan pada variabel listBuku, 
    # dengan cara meminjam;mengembalikan;memperpanjang;menambah;atau menghapus buku
     
def show2(Dict, printFormat):
    E=Dict.copy()
    print("""
    Pilih submenu dibawah ini: 
    1. Melihat semua daftar buku yang tersedia
    2. Mencari buku tertentu yang tersedia
    3. Kembali ke Menu Utama
    """)
    S1=int(input("Silahkan Masukkan angka yang sesuai: "))
    if S1==1:
        k=1 
        l=0 
        for value in E.values():
            if 'Tersedia' in value: 
                l=l+1
        if l!=0:
            print("Berikut daftar buku yang tersedia: ")
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
            show2(Dict, printFormat)            
        if l==0:
            print("""
            ------------------------------------------
            Maaf tidak ada stok buku yang tersedia
            ------------------------------------------""")  
            show2(Dict, printFormat) 
    elif S1==2:
        k=1 #Iterasi pengurutan nilai di list yang bersesuaian dengan nilai "No"
        l=0 #Iterasi untuk memastikan apakah ada buku yang tersedia untuk bisa dipinjam
        for value in E.values():
            if 'Tersedia' in value: 
                l=l+1
                    
        if l !=0:
            l2=0
            print("""
            Terdapat {} buku yang tersedia
            Silahkan masukkan NISB yang Anda cari untuk mencari buku tertentu
            """.format(l))
            S2=input("")
            for value in E.values():
                if S2 in value: 
                    l2=l2+1
            if l2!=0:
                for value in E.values():
                    if E['column']==value:
                        print(printFormat.format("", *value)) #menampikan semua nilai dari value pada key "column" 
                    else:
                        if S2 in value: 
                            # value[0]=k #Perubahan nilai list yang bersesuaian dengan nilai "No", pada value yg memiliki nilai "Tersedia"
                            # k+=1
                            l2=l2+1
                            print(printFormat.format("", *value))
                show2(Dict, printFormat) 
            if l2==0:
                print("""
            ------------------------------------------
            Maaf tidak ada buku dengan NISB {} yang tersedia
            ------------------------------------------""".format(S2)) 
                show2(Dict, printFormat) 
        if l==0:
            print("""
            ------------------------------------------
            Maaf tidak ada stok buku yang tersedia
            ------------------------------------------""") 
            show2(Dict, printFormat) 
    elif S1==3:
        main()
    else:
        print("Input yang Anda masukkan salah, silahkan coba lagi")
        show2(Dict, printFormat) 

            
        

def show(listBuku, printFormat, title="\nDaftar Semua Buku di Perpustakaan Sains Yogya\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Semua Buku di Perpustakaan Sains Yogya\n".
    """
    # Mengurutkan nilai pada kolom "No" sebelum menampilkan listBuku
    print(title)
    k=1
    for ValuesD in listBuku.values():
        if listBuku['column']!=ValuesD:
            ValuesD[0]=k
            k=k+1    

    #Menampilkan listBuku sesuai format jarak antar kata dan 
        # format penulisan yaitu menampilan value(berupa list) untuk masing masing key, sehingga muncul baris per baris
    for value in listBuku.values():
        print(printFormat.format("", *value))

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


# Fungsi minjam akan dipanggil saat user memilih menu "Meminjam buku" pada fungsi main
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



        #Proses untuk menampilkan daftar buku yang BISA DIPINJAM, bisa ada isinya atau kosong (hanya berupa value dari key "column")
            # dimunculkan dari variabel yang baru yaitu E (hasil copy variabel listBuku) yang sudah disesuaikan
        #Cara menyesuaikannya:
        # Jika value (berupa list) dari suatu key memiliki nilai "Tersedia" dalam value,
            # maka ubah nilai di Value (berupa list) pada variabel E yang bersesuaian dengan nilai "No" 
                # (dalam hal ini nilai dengan indeks ke 0) dengan angka 1,2,3 dst (berurutan)
        # Jika value (berupa list) dari suatu key memiliki nilai "Dipinjam" dalam value
            # maka ubah nilai di Value (berupa list) pada variabel E yang bersesuaian dengan nilai "No" 
                # (dalam hal ini nilai dengan indeks ke 0) dengan 0
        
        E=listBuku.copy()
        printFormat = "{:<4}" + "{:<17}" * (len(E['column']))
        k=1 #Iterasi pengurutan nilai di list yang bersesuaian dengan nilai "No"
        l=0 #Iterasi untuk memastikan apakah ada buku yang tersedia untuk bisa dipinjam
        for value in E.values():
            if E['column']==value:
                print(printFormat.format("", *value)) #menampikan semua nilai dari value pada key "column" 
            else:
                if 'Tersedia' in value: 
                    value[0]=k #Perubahan nilai list yang bersesuaian dengan nilai "No", pada value yg memiliki nilai "Tersedia"
                    k+=1
                    l=l+1
                    print(printFormat.format("", *value)) #menampilkan semua nilai dari value yang dicek pada key tertentu. value yang dicek harus memiliki nilai "Tersedia"
                else:
                    value[0]=0
        if l==0:
            print('Maaf tidak ada stok buku yang tersedia')            
            continue           
        
        #User akan memilih indeks yang nilainya bersesuaian dengan nilai "No" sesuai tampilan di promt, 
             #dalam hal ini menggunakan variabel E yang sudah disesuaikan
        A= int(input('Masukkan nomor indeks sesuai buku yang ingin dipinjam: '))
        #Jika kita ingin variabel listBuku ikut terupdate ketika user jadi memilih buku yang bisa dipinjam
            #maka kita harus melakukan link nilai tertentu antara variabel E dengan variabel listBuku 
                #agar semua perubahan yang terjadi di Variabel listBuku sesuai dengan pemilihan indeks keputusan user pada variabel E

        # Variabel E digunakan untuk menampilkan buku yang tersedia, 
            #kemudian user memilih indeks (nilai yang bersesuaian dengan "No")
        # Karena nilai yang bersesuaian dengan nilai "NISB" memiliki nilai yang unik maka akan dilink kan nilai unik tersebut pada variabel E dengan variabel listBuku 
            # dengan ketentuan nilai unik pada variabel E berasal dari value suatu key yang memiliki nilai hasil inputan indeks yang sama (nilai yang bersesuaian dengan No)
        # Pada varibel listbuku setelah terkoneksi dengan value suatu key yang memiliki nilai unik sama dengan varibel E, jika user jadi meminjam buku, 
            # maka kita lakukan perubahan pada nilai yang bersesuaian dengan nilai "Status", dari "Tersedia" menjadi "Dipinjam" tentunya harus 
                # dari nilai tersebut berasal dari value yang sama dengan value suatu key yang memiliki nilai unik sama dengan varibel E
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
            print("""
            Tidak ada buku yang bisa dikembalikan, Anda belum meminjam buku satupun
            """)
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
                                show(listBuku, printFormat)
                          
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
            print("""
            Tidak ada buku yang bisa diperpanjang, Anda belum meminjam buku satupun
            """)
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






def nambah(listBuku,printFormat):
    
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
            
            NISB_ = input("Masukkan NISB buku: ")
         
            l=0
            for valueD in listBuku.values():
                if NISB_ in valueD:
                    l=l+1
                    print("Buku dengan NISB tersebut tidak bisa diinput karena sudah terdaftar")
                    E=listBuku.copy()
                    k=1
                    for value in E.values():
                        if E['column']==value:
                            print(printFormat.format("", *value))  
                        else:
                            if NISB_ in value: 
                                value[0]=k 
                                k+=1
                                print(printFormat.format("", *value)) 
                    nambah(listBuku,printFormat)
                

            if l==0:
                print("""
                Buku dengan NISB yang Anda input berhasil didaftarkan
                """)
                Judul = input("Silahkan Masukkan judul buku: ")
                Edisi = int(input("Silahkan Masukkan tahun edisi buku: "))
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
                        Status = 'Tersedia'
                        NIS_=' '
                        Peminjam=' '
                        Tgl_pinjam=' '
                        Tgl_kembali=' '
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
    
  



def update(listBuku,printFormat):
    while True:
        E=listBuku.copy()
        F=listBuku.copy()
        print(
                            """

                    Silahkan {} pilih menu dibawah ini :

                    1. Lanjut mengupdate tahun edisi buku
                    2. Kembali ke menu utama
                    
                """.format(nama)
                    )
        A2=int(input(""))
        if A2==1:
            
            NISB_ = input("Masukkan NISB buku yang akan diupdate tahun edisinya: ")
                
            l=0
            for valueD in F.values():
                if NISB_ in valueD:
                    print("Terdapat Buku dengan NISB tersebut yang bisa diupdate tahun edisinya")
                    l=l+1
                    E=listBuku.copy()
                    k=1
                    for value in E.values():
                        if E['column']==value:
                            print(printFormat.format("", *value))  
                        else:
                            if NISB_ in value: 
                                value[0]=k 
                                k+=1
                                print(printFormat.format("", *value)) 
                    print("""
                        Apakah Anda ingin lanjut mengupdate tahun edisi buku tersebut
                        1. Ya
                        2. Tidak
                        """)
                    
                    U1=int(input("Masukkan angka: "))
                    
                    if U1==1:
                        input("Tuliskan 'EDISI' untuk memastikan Anda ingin mengupdate tahun edisi buku tersebut : ")
                        U2=input("Masukkan tahun edisi terbaru: ")
                        print(""""
                        Apakah Anda yakin ingin mengubah tahun edisi buku menjadi tahun {}
                        1. Ya
                        2. Tidak
                        """.format(U2))
                        U3=int(input(" "))
                        if U3==1:
                            for value in listBuku.values():
                                    if NISB_ in value: 
                                        value[2]=U2
                            print("Selamat tahun edisi buku sudah diupdate")
                            update(listBuku,printFormat)

                        elif U3==2:
                            update(listBuku,printFormat)

                    elif U1==2:
                        update(listBuku,printFormat)
            
            if l==0:
                print("""
                Buku dengan NISB yang Anda input tidak ada sehingga tidak bisa dilakukan update
                """)
                update(listBuku,printFormat) 
        elif A2==2:
            main()
        else:
            print('Nomor yang anda masukkan salah')

    
#Fungsi main yang akan dipanggil ketika user sudah berhasil memasukkan nama dan nis dengan benar pada fungsi login
    # atau dipanggil ketika ada pilihan "kembali ke menu utama" yang dijalankan oleh user
#Fungsi main menampilkan tampilan menu utama program, terdapat 9 menu utama yaitu:
# 1. Menampilkan semua daftar buku 
# 2. Menampilkan daftar buku tertentu
# 3. Meminjam buku
# 4. Mengembalikan buku
# 5. Memperpanjang buku
# 6. Menambah buku
# 7. Menghapus buku
# 8. Mengupdate tahun edisi buku
# 9. Log in ulang
# 10. Exit
#Khusus pilihan menu "Menambahkan buku" dan "Menghapus buku", sebelum bisa menjalankan ke fungsi yang bisa memanggil keduanya,
    # user akan diminta memasukkan password terlebih dahulu, jika user tidak tau passwordnya maka user bisa memilih 
    # untuk kembali ke menu utama sesuai perintah yang ada
def main():
    while True:
        print(
            """

Halo, selamat datang {} ({}) di Perpustakaan Universitas Sains Yogyakarta
Waktu Kunjungan Anda: {} 

Silahkan pilih menu yang ingin dijalankan dengan memasukkan angka sesuai menu:

1. Menampilkan semua daftar buku 
2. Menampilkan daftar buku tertentu
3. Meminjam buku
4. Mengembalikan buku
5. Memperpanjang buku
6. Menambah buku
7. Menghapus buku
8. Mengupdate tahun edisi buku
9. Log in ulang
10. Exit
""".format(nama, nis, waktu_kunjung)
        )
        # Input menu yang akan dijalankan
        menuNumber = input(" ")
        # Menu untuk menampilkan daftar buku dengan memanggil fungsi show
        if menuNumber == str(1):
            show(listBuku, printFormat)
        #Menu untuk menampilkan daftar buku tertentu dengan memanggil fungsi show2
        elif menuNumber ==str(2):
            show2(listBuku, printFormat)
        # Menu untuk meminjam buku dengan memanggil fungsi minjam
        elif menuNumber == str(3):
            minjam(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk mengembalikan buku dengan memanggil fungsi kembali
        elif menuNumber == str(4):
            kembali(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk memperpanjang buku dengan memanggil fungsi panjang
        elif menuNumber == str(5):
            panjang(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk menambah buku dengan memanggil fungsi nambah
        elif menuNumber == str(6):
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
                        nambah(listBuku,printFormat)
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
        # Menu untuk menghapus buku dengan memanggil fungsi delete(1)
        elif menuNumber == str(7):
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
        # Menu untuk mengupdate buku
        elif menuNumber == str(8):
            update(listBuku,printFormat)
        # Menu untuk login kembali
        elif menuNumber == str(9):
            login()
        # Menu untuk menghentikan program
        elif menuNumber == str(10):
            sys.exit()
        # Pilihan lainnya ketika user tidak menginput angka selain 1,2,3,4,5,6,7,8 akan kembali diminta input menu yang benar
        else:
            print("""
Tidak ada pilihan {} pada menu
Silahkan coba kembali
""".format(menuNumber))


if __name__ == "__main__":

    # Deklarasi variabel listBuku berupa list dalam dict
    #Dalam variabel listBuku Terdapat 9 kolom utama yang bisa ditampilkan pada prompt yaitu "No" ... "Tanggal Pengembalian"
    #Kolom unik yang ditampilkan di prompt yang berisi nilai unik juga yaitu "No", "NISB", "NIS/NIK"
    # Key berupa column, buku-01,...,buku-3
    # Value berupa list yang berisi nilai-nilai, contoh
        #pada key column berisi value berupa list yaitu
        #["No", "Judul Buku", "Edisi Buku", "NISB", "Status", "Peminjam","NIS/NIK", "Tanggal Pinjam", "Tanggal Pengembalian"]
        # dalam list tersebut berisi nilai-nilai yaitu No,Judul buku,...
        #pada key buku-01 berisi value berupa list yaitu
        #[1, "Buku Kimia", 2016, "K01", "Tersedia", " ", " ", " ", " " ]
        #dalam list tersebut berisi nilai-nilai yaitu 1, Buku Kimia,...
    #Dapat dikatakan nilai "Tersedia" pada value dari key "buku-0" atau dari "buku-2" bersesuaian dengan nilai "Status" pada value dari key "column"
        #saat ditampilkan pada prompt
    listBuku = {
        'column': ["No", "Judul Buku", "Edisi Buku", "NISB", "Status", "Peminjam","NIS/NIK", "Tanggal Pinjam", "Tanggal Pengembalian"],
        'buku-0': [1, "Buku Kimia IA", 2016, "K01", "Tersedia", " ", " ", " ", " " ],
        'buku-1': [2, "Buku Fisika IA", 2017, "F01", "Dipinjam", "Andi", "10116072", "2023-05-21", "2023-05-23"],
        'buku-2': [3, "Buku Aktuaria IA", 2018, "AK01", "Tersedia", " ", " "," ", " " ],
        'buku-3': [4, "Buku Matematika IA", 2019, "M01", "Dipinjam", "Andi","10116072", "2023-05-14", "2023-05-24"],
        'buku-4' :[5, "Buku Astronomi IA", 2020, "AS01", "Dipinjam", "Andi","10116072", "2023-05-16", "2023-05-28"],
    }

    # Deklarasi format jarak antar kata di prompt
    printFormat = "{:<2}" + "{:<19}" * (len(listBuku['column']))

#Fungsi login yang akan dipanggil pada saat program pertama kali dijalankan atau 
    # dipanggil menggunakan pilihan "log in ulang" pada menu utama
#User akan diminta menginputkan nama dan nis, untuk waktu kunjung diisi manual dengan 
    # mengupdate tanggal ketika user menjalankan program
def login():
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

# Memanggil fugsi login saat pertama kali program dijalankan
login()

#FITUR CREATE   ADA DI MENU       6. MENAMBAHKAN BUKU
#FITUR READ     ADA DI MENU       2. MENAMPILKAN DAFTAR BUKU TERTENTU
#FITUR UPDATE   ADA DI MENU       8. MENGUPDATE TAHUN EDISI BUKU
#FITUR DELETE   ADA DI MENU       7. MENGHAPUS BUKU

