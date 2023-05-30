import sys
import pyinputplus as pypi 
from datetime import datetime

def batas(listBuku,nis):
    print("Berikut daftar buku yang sebelumnya Anda pinjam: ")
    E=listBuku.copy()
    k=1
    l=0
    for value in E.values():
            if E['column']==value:
                print(printFormat.format("", *value))
            else:
                if nis in value: 
                    value[0]=k
                    k+=1
                    l=l+1
                    print(printFormat.format("", *value))
    print("""
    Anda sudah meminjam buku sebanyak {} buah
    """.format(l))                
    if l==3:
        print("""
        Anda tidak bisa mmeminjam buku lagi
        Maksimal buku yang bisa dipinjam per mahasiswa sebanyak 3 buah
        """)
        main()
    else:
        print("Berikut daftar buku yang tersedia: ")
        
def delete1(C,nama):
    while True:           
        print(
                        """

                Silahkan {} masukkan angka dari pilihan berikut:

                1. Lanjut menghapus buku
                2. Kembali ke menu utama
                
            """.format(nama)
                )
        A2=pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
        if A2== 1:
            index = input("Masukkan ISBN buku yang ingin dihapus: ")
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
                            Apakah Anda yakin ingin menghapus buku dengan judul {} Edisi {} dengan ISBN {}?
                            1. Ya
                            2. Tidak
                            """.format(val[1],val[2],val[3]))
                            A=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
                            if A==1:
                                print(len(F)) #6
                                del F[val[0]]
                                print(len(F)) #5
                                listBuku={}
                                listBuku['column']=F[0]
                                for i in range(1,len(F)):
                                    listBuku[f'buku-{i-1}']=F[i]
                                print("""

                                Sedang menghapus buku, harap menunggu
                                
                                Anda berhasil menghapus buku dengan judul {} Edisi {} ISBN {}
                                
                                """.format(val[1],val[2],val[3]))
                                k=1
                                for ValuesD in listBuku.values():
                                    if listBuku['column']!=ValuesD:
                                        ValuesD[0]=k
                                        k=k+1 
                                delete1(listBuku,nama)
                            elif A==2:
                                print("Anda tidak jadi menghapus buku tersebut")
                                delete1(listBuku,nama)
                    else:
                        print('Terdapat buku dengan ISBN {}, namun tidak bisa dihapus karena buku tersebut sedang dipinjam'.format(val[3]))
                        delete1(listBuku,nama)
            if k==0:
                print(f'Buku dengan ISBN {index} tidak tersedia')
                delete1(listBuku,nama)
        elif A2==2:
            main()
          
def show2(Dict, printFormat):
    E=Dict.copy()
    print("""

    Silahkan {} masukkan angka dari pilihan berikut:

    1. Melihat semua daftar buku yang tersedia
    2. Mencari buku tertentu
    3. Kembali ke menu utama

    """.format(nama))
    S1=pypi.inputInt(prompt='', blockRegexes='0', lessThan=4)
    if S1==1:
        k=1 
        l=0 
        for value in E.values():
            if 'Tersedia' in value: 
                l=l+1
        if l!=0:
            print("Berikut daftar buku yang tersedia: ")
            printFormat = "{:<2}" + "{:<19}" * (len(E['column']))
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
            --------------------------------------
            Maaf tidak ada stok buku yang tersedia
            --------------------------------------""")  
            show2(Dict, printFormat) 
    elif S1==2:
        k=1 
        l=0 
        for value in E.values():
            if 'Tersedia' in value: 
                l=l+1  
        if l !=0:
            l2=0
            print("""
            Terdapat {} buku yang tersedia
            Silahkan masukkan ISBN buku yang Anda cari untuk memastikan ketersediaan dari buku tersebut
            """.format(l))
            S2=input("")
            for value in E.values():
                if S2 in value: 
                    l2=l2+1
            if l2!=0:
                for value in E.values():
                    if E['column']==value:
                        print(printFormat.format("", *value)) 
                    else:
                        if S2 in value: 
                            value[0]=k 
                            k+=1
                            l2=l2+1
                            print(printFormat.format("", *value))
                show2(Dict, printFormat) 
            if l2==0:
                print("""
            ---------------------------------------
            Maaf buku dengan ISBN {} tidak tersedia
            ---------------------------------------""".format(S2)) 
                show2(Dict, printFormat) 
        if l==0:
            print("""
            --------------------------------------
            Maaf tidak ada stok buku yang tersedia
            --------------------------------------""") 
            show2(Dict, printFormat) 
    elif S1==3:
        main()
     
def show(listBuku, printFormat, title="\nDaftar Semua Buku di Perpustakaan Sains Yogya\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Semua Buku di Perpustakaan Sains Yogya\n".
    """
    print(title)
    k=1
    for ValuesD in listBuku.values():
        if listBuku['column']!=ValuesD:
            ValuesD[0]=k
            k=k+1    
    for value in listBuku.values():
        print(printFormat.format("", *value))
    print("""
    Apakah Anda ingin kembali ke menu utama?
    1. Ya
    2. Tidak
    """)
    L = pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
    if L==1:
        main()
    elif L==2:
        show(listBuku, printFormat)

def waktu_minjam(W1):
    while True:
        global B_minjam
        B_minjam=input('Masukkan tanggal pengembalian buku terbaru harus dengan format (yyyy-mm-dd): ') #klo format ga sesuai error, harus ikut aturan kalender juga
        # Ubah string menjadi objek tanggal
        tanggal1 = datetime.strptime(W1, "%Y-%m-%d").date()
        tanggal2 = datetime.strptime(B_minjam, "%Y-%m-%d").date()
        # Hitung selisih antara dua tanggal
        selisih = (tanggal2 - tanggal1).days
        if selisih==0:
            print(f'Tanggal pengembalian tidak boleh tanggal hari ini {W1}')
        elif 0<selisih<=7:
            print(f'Anda meminjam buku tersebut selama {selisih} hari')
            break
        elif selisih<0:
            print('Miminimal waktu peminjaman 1 hari dari hari ini')
        else:
            print('Maksimal waktu peminjaman 7 hari dari hari ini')

def minjam(Nama,NIS,listBuku,tgl_skrg):
    while True:
        print(
                        """

                Silahkan {} masukkan angka dari pilihan berikut:

                1. Lanjut meminjam buku
                2. Kembali ke menu utama
                
            """.format(Nama)
                )
        A2=pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
        if A2== 1:
            batas(listBuku,nis)
        elif A2==2:
            main()
        E=listBuku.copy()
        printFormat = "{:<2}" + "{:<19}" * (len(E['column']))
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
        A= input('Masukkan ISBN buku yang ingin dipinjam: ')
        i=0
        for value in E.values():
            if A in value:
                i=1
                print(
                        """
                Apakah Anda yakin meminjam buku dengan judul {} edisi {} ISBN {}?

                1. Ya
                2. Tidak
                
            """.format(value[1],value[2],value[3])
                )
                A1=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
                if A1==1:
                    for valueD in listBuku.values():
                        if value[3] in valueD:
                            waktu_minjam(tgl_skrg)  
                            print(
                                    """
                            Apakah Anda yakin paling lambat mengembalikan buku dengan judul {} edisi {} ISBN {} pada tanggal {}?
                            
                            1. Ya
                            2. Tidak
                            """.format(value[1],value[2],value[3],B_minjam)
                            )
                            A2=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
                            if A2==1:
                                valueD[4]="Dipinjam"
                                valueD[5]=Nama
                                valueD[6]=NIS
                                valueD[7]=tgl_skrg
                                valueD[8]=B_minjam
                                print(
                                    """
                                    Selamat Anda telah berhasil meminjam buku dengan judul {} edisi {} ISBN {}

                                    Pastikan Anda tepat waktu untuk mengembalikan buku tersebut paling lambat pada tanggal {}
                                """.format(value[1],value[2],value[3],B_minjam)
                                )
                            elif A2==2:
                                print('Anda tidak jadi meminjam buku dengan judul {} edisi {} ISBN {}, mohon pastikan tanggal pengembalian buku saat meminjam'.format(value[1],value[2],value[3]))
                elif A1==2:
                    print("Anda tidak jadi meminjam buku dengan judul {} edisi {} ISBN {}".format(value[1],value[2],value[3]))
        if i!=1:
            print(f'Tidak ada buku yang tersedia dengan ISBN {A}')
            
def waktu_kembali(W1,val):
    WD=(datetime.strptime(val, "%Y-%m-%d").date()-datetime.strptime(W1, "%Y-%m-%d").date()).days
    if WD>=0:
        print('Terima kasih sudah mengembalikan buku tepat waktu')
    else:
        print("""
        Anda dikenakan denda karena telat {} hari mengembalikan buku tersebut dari tanggal pengembalian
        Seharusnya paling lambat Anda mengembalikan buku pada tanggal {}
        Untuk info lanjut mengenai denda silahkan temui petugas perpustakaan yang berwenang setelah berhasil mengembalikan buku, Terima kasih
        """.format(abs(WD), val))
    
def kembali(Nama, NIS,listBuku,tgl_skrg):
    while True:
        print(
                        """

                Silahkan {} masukkan angka dari pilihan berikut:

                1. Lanjut mengembalikan buku
                2. Kembali ke menu utama
                
            """.format(Nama)
                )
        A2=pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
        if A2== 1:
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
            A=pypi.inputInt(prompt='Silahkan masukkan nomor indeks sesuai buku yang ingin dikembalikan: ', blockRegexes='0', lessThan=l+1)   
            i=0
            for value in E.values():
                if A in value:
                    print(
                            """
                    Apakah Anda yakin mengembalikan buku dengan judul {} edisi {} ISBN {} hari ini?

                    1. Ya
                    2. Tidak
                    
                """.format(value[1],value[2],value[3])
                    )
                    A1=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
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
                                    Anda telah berhasil mengembalikan buku dengan judul {} edisi {} ISBN {}
                                    
                                """.format(value[1],value[2],value[3])
                                )
                                k=1
                                for ValuesD in listBuku.values():
                                    if listBuku['column']!=ValuesD:
                                        ValuesD[0]=k
                                        k=k+1    
                                for value in listBuku.values():
                                    print(printFormat.format("", *value))
                                break
                        continue
                        
                    elif A1==2:
                        print("Anda tidak jadi mengembalikan buku dengan judul {} edisi {} ISBN {}".format(value[1],value[2],value[3]))
                        continue
        elif A2==2:
            main()
            
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

                    Silahkan {} masukkan angka dari pilihan berikut:

                    1. Lanjut memperpanjang buku
                    2. Kembali ke menu utama
                    
                """.format(Nama)
                    )
            A2=pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
            if A2== 1:
                break
            elif A2==2:
                main()
        E=listBuku.copy()
        printFormat = "{:<2}" + "{:<19}" * (len(E['column']))
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
        A= pypi.inputInt(prompt='Silahkan masukkan nomor indeks sesuai buku yang ingin diperpanjang: ', blockRegexes='0', lessThan=l+1)
        i=0
        for value in E.values():
            if A in value:
                i=1
                while True:
                    print(
                            """
                    Apakah Anda yakin memperpanjang buku dengan judul {} edisi {} ISBN {}?
                    

                    1. Ya
                    2. Tidak
                    
                """.format(value[1],value[2],value[3])
                    )
                    A1=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
                    if A1==1:
                        for valueD in listBuku.values():
                            if value[3] in valueD:
                                waktu_panjang(tgl_skrg,value[8])
                                while True:
                                    print(
                                            """
                                    Apakah Anda yakin paling lambat memperpanjang buku dengan judul {} edisi {} ISBN {} pada tanggal {}?
                                    
                                    Silahkan pilih menu dibawah ini:
                                    1. Ya
                                    2. Tidak
                                    """.format(value[1],value[2],value[3],B_panjang)
                                    )
                                    A3=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
                                    if A3==1:
                                        valueD[7]="2023-05-24"
                                        valueD[8]=B_panjang
                                        print(
                                            """
                                            Selamat Anda telah berhasil memperpanjang buku dengan judul {} edisi {} ISBN {}
                                            Pastikan Anda tepat waktu untuk mengembalikan buku tersebut paling lambat pada tanggal {}
                                        """.format(value[1],value[2],value[3],B_panjang)
                                        )
                                        show(listBuku, printFormat)
                                        break
                                    elif A3==2:
                                        print('Anda tidak jadi memperpanjang buku dengan judul {} edisi {} ISBN {}, mohon pastikan tanggal pengembalian buku terbaru saat meminjam'.format(value[1],value[2],value[3]))
                                        break
                        break
                    elif A1==2:
                        print("Anda tidak jadi memperpanjang buku dengan judul {} edisi {} ISBN {}".format(value[1],value[2],value[3]))
                        break
        if i!=1:
            print(f'Tidak ada buku yang anda pinjam dengan nomor indeks {A}')

def nambah(listBuku,printFormat):
    while True:
        print(
                        """

                Silahkan {} masukkan angka dari pilihan berikut: 

                1. Lanjut menambahkan buku
                2. Kembali ke menu utama
                
            """.format(nama)
                )
        A2 = pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
        if A2== 1:
            NISB_ = input("Masukkan ISBN buku: ")
            l=0 
            for valueD in listBuku.values():
                if NISB_ in valueD:
                    l=l+1
                    print("Buku dengan ISBN tersebut tidak bisa ditambahkan karena sudah terdaftar") 
                    E=listBuku.copy()
                    k=1
                    for value in E.values():
                        if E['column']==value:
                            print('')
                            #print(printFormat.format("", *value))  
                        else:
                            if NISB_ in value: 
                                value[0]=k 
                                k+=1
                                #Menampilkan informasi buku perpus yang memiliki ISBN yang sama dengan ISBN inputan user
                                print(printFormat.format("", *value)) 
                    nambah(listBuku,printFormat)
            if l==0:
                print("""
                Buku dengan ISBN yang Anda input berhasil didaftarkan
                """)
                Judul = input("Silahkan Masukkan judul buku: ")
                Edisi=pypi.inputInt(prompt='Silahkan Masukkan tahun edisi buku: ')
                print("""

                Anda menambahkan buku dengan:
                Judul   :  {}
                Edisi   :  {}
                NISB    :  {}

                Apakah Anda yakin menambahkan buku tersebut?
                1. Ya
                2. Tidak
                
                """.format(Judul,Edisi,NISB_))
                n1=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan tersebut:', blockRegexes='0', lessThan=3)
                if n1==1:
                    Status = 'Tersedia'
                    NIS_=' '
                    Peminjam=' '
                    Tgl_pinjam=' '
                    Tgl_kembali=' '
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
                    print("""
                    Sedang menyimpan buku, harap menunggu 

                    Anda berhasil menambahkan buku tersebut
                    """)
                    nambah(listBuku,printFormat)
                elif n1==2:
                    print("Anda tidak jadi menambahkan buku tersebut")
                       
        elif A2==2:
            main()
     
def update(listBuku,printFormat):
    while True:
        E=listBuku.copy()
        F=listBuku.copy()
        print(
                            """

                    Silahkan {} masukkan angka dari pilihan berikut:

                    1. Lanjut mengupdate tahun edisi buku
                    2. Kembali ke menu utama
                    
                """.format(nama)
                    )
        A2=pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
        if A2==1:
            
            NISB_ = input("Masukkan ISBN buku yang akan diupdate tahun edisinya: ")
                
            l=0
            for valueD in F.values():
                if NISB_ in valueD:
                    print("Terdapat buku dengan ISBN tersebut yang bisa diupdate tahun edisinya")
                    l=l+1
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
                        Apakah Anda ingin lanjut mengupdate tahun edisi dari buku tersebut
                        1. Ya
                        2. Tidak
                        """)
                    U1=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan tersebut:', blockRegexes='0', lessThan=3)
                    if U1==1:
                        Uu=pypi.inputStr(prompt='Silahkan masukkan kata "EDISI" untuk mengubah nilai dari suatu kolom edisi yang ingin diupdate: ' , applyFunc=lambda x: x.capitalize(), blockRegexes='1234567890')
                        U2=pypi.inputInt(prompt='Masukkan tahun edisi terbaru dari buku tersebut: ')
                        print("""
                        Apakah Anda yakin ingin mengubah tahun edisi buku menjadi tahun {} ?
                        1. Ya
                        2. Tidak
                        """.format(U2))
                        U3=pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan tersebut:', blockRegexes='0', lessThan=3)
                        if U3==1:
                            for value in listBuku.values():
                                    if NISB_ in value: 
                                        value[2]=U2
                            print("""

                    Sedang mengupdate tahun edisi buku, harap menunggu 

                    Anda berhasil mengupdate tahun edisi buku tersebut
                    
                    """)
                            update(listBuku,printFormat)

                        elif U3==2:
                            update(listBuku,printFormat)

                    elif U1==2:
                        update(listBuku,printFormat)
            
            if l==0:
                print("""
                Buku dengan ISBN yang Anda masukkan tidak ada sehingga tidak bisa dilakukan update
                """)
                update(listBuku,printFormat) 
        elif A2==2:
            main()

def main():
    print(
            """

Halo, selamat datang {} ({}) di Perpustakaan Universitas Sains Yogyakarta
Waktu Kunjungan Anda: {} 

Silahkan pilih menu dengan memasukkan angka sesuai menu yang ingin dijalankan:

1. Menambahkan buku (Fitur Create)
2. Menampilkan daftar buku tertentu (Fitur Read)
3. Mengupdate Tahun Edisi Buku (Fitur Update)
4. Menghapus buku (Fitur Delete)
5. Menampilkan Daftar Semua Buku
6. Meminjam Buku
7. Mengembalikan Buku
8. Memperpanjang Buku
9. Log in ulang
10. Exit
""".format(nama, nis, waktu_kunjung)
        )
    while True:
        # Input menu yang akan dijalankan
        menuNumber=input('Silahkan masukkan angka dari pilihan yang tersedia: ')
        # Menu untuk menampilkan daftar buku dengan memanggil fungsi show
        if menuNumber == '5':
            show(listBuku, printFormat)
        #Menu untuk menampilkan daftar buku tertentu dengan memanggil fungsi show2
        elif menuNumber =='2':
            show2(listBuku, printFormat)
        # Menu untuk meminjam buku dengan memanggil fungsi minjam
        elif menuNumber == '6':
            minjam(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk mengembalikan buku dengan memanggil fungsi kembali
        elif menuNumber == '7':
            kembali(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk memperpanjang buku dengan memanggil fungsi panjang
        elif menuNumber == '8':
            panjang(nama,nis,listBuku,waktu_kunjung)
        # Menu untuk menambah buku dengan memanggil fungsi nambah
        elif menuNumber == '1':
            print("""
            Perhatian! 
            Menu menambahkan buku hanya bisa diakses oleh Petugas Perpustakaan yang berwenang
            Untuk mengakses menu menambahkan buku Anda harus memasukkan password terlebih dahulu

            Silahkan masukkan angka dari pilihan berikut:
            1. Lanjut memasukkan password
            2. Kembali ke menu utama

            """)
            P = pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
            if P==1:
                while True:
                    Pass=input("Silahkan Masukkan password untuk bisa menambahkan buku, jika Anda lupa password masukkan angka 0 untuk kembali ke menu utama: ")
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
        # Menu untuk menghapus buku dengan memanggil fungsi delete(1)
        elif menuNumber == '4':
            print("""
            Perhatian! 
            Menu menghapus buku hanya bisa diakses oleh Petugas Perpustakaan yang berwenang
            Untuk mengakses menu menghapus buku Anda harus memasukkan password terlebih dahulu

            Silahkan masukkan angka dari pilihan berikut:
            1. Lanjut memasukkan password
            2. Kembali ke menu utama

            """)
            P = pypi.inputInt(prompt='', blockRegexes='0', lessThan=3)
            if P==1:
                while True:
                    Pass=input("Silahkan Masukkan password untuk bisa menghapus buku, jika Anda lupa password masukkan angka 0 untuk kembali ke menu utama: ")
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
        # Menu untuk mengupdate buku
        elif menuNumber == '3':
            update(listBuku,printFormat)
        # Menu untuk login kembali
        elif menuNumber == '9':
            login()
        # Menu untuk menghentikan program
        elif menuNumber == '10':
            sys.exit()
        else:
            print("Input yang Anda masukkan tidak valid")

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
    nama= pypi.inputStr(prompt='Silahkan masukkan nama lengkap Anda: ' , applyFunc=lambda x: x.capitalize(), blockRegexes='1234567890')
    nis1 = pypi.inputInt(prompt='Silahkan masukkan NIS/NIP Anda: ')
    nis=str(nis1)
    print("""

    Nama       : {}
    NIS/NIP    : {}

    Apakah data yang Anda masukkan sudah benar?
    1. Ya
    2. Tidak
    
    """.format(nama,nis))
    L = pypi.inputInt(prompt='Silahkan masukkan angka dari pilihan yang tersedia: ', blockRegexes='0', lessThan=3)
    if L==1:
        main()
    elif L==2:
        login()
            
if __name__ == "__main__":
    #Variabel listBuku berupa Dict didalamnya berupa list
    listBuku = {
        'column': ["No", "Judul Buku", "Edisi Buku", "ISBN", "Status", "Peminjam","NIS/NIK", "Tanggal Pinjam", "Tanggal Pengembalian"],
        'buku-0': [1, "Kimia VII", 2016, "111", "Tersedia", " ", " ", " ", " " ],
        'buku-1': [2, "Fisika VII", 2017, "222", "Dipinjam", "Andi", "10116072", "2023-05-21", "2023-05-23"],
        'buku-2': [3, "Aktuaria VII", 2018, "333", "Tersedia", " ", " "," ", " " ],
        'buku-3': [4, "Matematika VII", 2019, "444", "Dipinjam", "Andi","10116072", "2023-05-14", "2023-05-24"],
        'buku-4' :[5, "Astronomi VII", 2020, "555", "Dipinjam", "Andi","10116072", "2023-05-16", "2023-05-28"]
    }
    # Deklarasi format jarak antar kata di prompt
    printFormat = "{:<2}" + "{:<19}" * (len(listBuku['column']))

# Memanggil fugsi login saat pertama kali program dijalankan
login()
