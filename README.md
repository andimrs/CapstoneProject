# Perpustakaan Sains Yogya

Sebuah layanan aplikasi menggunakan bahasa pemrograman Python bagi siswa dan guru untuk mencari, menyimpan suatu data selama mereka melakukan kegiatan di dalam perpustakaan, seperti mencari buku yang tersedia, meminjam buku, mengembalikan buku, memperpanjang buku, menambahkan buku, dan menghapus buku

## Installation

To clone from github, run:

mkdir C:\Users\hp\Documents\Project1
cd C:\Users\hp\Documents\Project1
git clone git@github.com:andimrs/CapstoneProject.git

Langkah-langkah untuk mengambil kodingan program di git hub:

## Quickstart Guide

Tampilan awal saat program dijalankan user akan akan diminta menginput nama user sebagai pengunjung perpustakaan yang memiliki NIS/NIP dan menginput NIS/NIP milik user dengan benar (Nomor Induk Siswa bagi siswa atau Nomor Induk Pegawai bagi guru), kemudian user akan diarahkan ke menu utama dengan memanggil fungsi main setelah yakin memasukkan nama dan NIS/NIP dengan benar
Di menu utama user dapat memilih menu-menu yang tersedia dengan memasukkan angka sesuai pilihan yang tersedia dari 1 sampai dengan 10, jika user memasukkan angka selain 1 sampai dengan 10, maka user mendapatkan notifikasi Input yang Anda masukkan tidak valid

Berikut penjelasan mengenai menu-menu yang ada di menu utama:

1. Menu Menambahkan buku (Create Option)
Menu utama yang memiliki fitur create yaitu menu menambahkan buku yang dijalankan oleh fungsi nambah ketika user memasukkan angka 1 di tampilan menu utama, tampilan awal saat memanggil fungsi nambah berupa SubMenu yang berisi 2 pilihan yaitu pilihan 1 lanjut menambahkan buku, pilihan 2 kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:
Jika user memilih pilihan 1 lanjut menambahkan buku dengan memasukkan angka 1, user memasukkan primary key data berupa ISBN buku, lalu akan dicek apakah sudah ada buku di perpustakaan yang memiliki ISBN yang sama dengan ISBN inputan user, dari pengecekan tersebut ada beberapa kemungkinan:
    Jika sama ISBNnya maka user akan mendapatkan notifikasi bahwa buku dengan ISBN tersebut tidak bisa ditambahkan karena sudah terdaftar, kemudian user diarahkan ke tampilan pilihan submenu

    Jika tidak ada buku perpus yang memiliki ISBN yang sama dengan ISBN inputan user maka user mendapatkan notifikasi bahwa Buku dengan ISBN yang Anda input berhasil didaftarkan, kemudian user memasukkan data buku lainnya seperti Judul dan Edisi yang bersesuaian dengan buku yang ditambahkan, lalu user mendapatkan pilihan mengenai kepastian apakah data buku secara keseluruhan jadi ditambahkan atau tidak, dari pilihan kepastian tersebut ada beberapa kemungkinan:
        Jika data buku secara keseluruhan jadi ditambahkan user akan mendapatkan notifikasi bahwa buku yang ditambahkan sedang disimpan dan user sudah berhasil menambah buku tersebut, kemudian user diarahkan ke tampilan pilihan submenu
        Jika data buku secara keseluruhan tidak jadi ditambahkan user akan mendapatkan notifikasi bahwa user tidak jadi menambahkan buku tersebut,kemudian user diarahkan ke tampilan pilihan submenu

Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main

Jika user memasukkan angka selain 1 dan 2 maka user akan diarakan ke tampilan pilihan submenu

2. Menu Menampilkan daftar buku tertentu (Read Option)

Menu utama yang memiliki fitur read yaitu menu menampilkan daftar buku tertentu yang dijalankan oleh fungsi show2 ketika user memasukkan angka 2 di tampilan menu utama, tampilan awal saat memanggil fungsi show2 berupa SubMenu yang berisi 3 pilihan yaitu pilihan 1 Melihat semua daftar buku yang tersedia, pilihan 2 Mencari buku tertentu yang tersedia, pilihan 3 Kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:
Jika user memilih pilihan 1 Melihat semua daftar buku yang tersedia dengan memasukkan angka 1, maka akan dilakukan pengecekan apakah buku dengan status Tersedia ada atau tidak ada, dari pengecekan tersebut ada beberapa kemungkinan:
    Jika terdapat buku dengan status tersedia, maka user akan dapat melihat tampilan berupa detail informasi dari buku-buku dengan status tersedia, kemudian user diarahkan ke tampilan submenu

    Jika tidak ada satupun buku dengan status tersedia, maka user akan mendapatkan notifikasi Maaf tidak ada stok buku yang tersedia, kemudian user diarahkan ke tampilan submenu

Jika user memilih pilihan 2 Mencari buku tertentu yang tersedia dengan memasukkan angka 2, maka akan dilakukan pengecekan apakah buku dengan status Tersedia ada atau tidak ada, dari pengecekan tersebut ada beberapa kemungkinan:
    Jika terdapat buku dengan status tersedia, maka user akan diminta memasukkan primary key berupa ISBN buku yang dicari, kemudian akan dilakukan pengecekan apakah ada atau tidak buku yang tersedia memiliki ISBN yang sama dengan inputan ISBN user, dari pengecekan tersebut ada beberapa kemungkinan:
        Jika ada buku yang tersedia sesuai dengan ISBN yang dicari user, maka user akan dapat melihat tampilan detail informasi dari buku tersebut, kemudian user diarahkan ke tampilan submenu

        Jika tidak ada buku yang tersedia sesuai dengan ISBN yang dicari user, maka user akan mendapatkan notifikasi Maaf buku dengan ISBN tersebut tidak tersedia, kemudian user diarakan ke tampilan submenu

    Jika tidak terdapat buku dengan status tersedia, maka user akan mendapatkan notifikasi Maaf tidak ada stok buku yang tersedia, kemudian user diarahkan ke tampilan submenu

Jika user memilih memilih pilihan 3 kembali ke menu utama dengan memasukkan angka 3, user akan diarahkan ke tampilan menu utama di fungsi main

Jika user memasukkan angka selain 1,2, dan 3 maka user akan diarakan ke tampilan pilihan submenu

3. Mengupdate Tahun Edisi Buku (Update option)

Menu utama yang memiliki fitur create yaitu menu menambahkan buku yang dijalankan oleh fungsi update ketika user memasukkan angka 3 di tampilan menu utama, tampilan awal saat memanggil fungsi nambah berupa SubMenu yang berisi 2 pilihan yaitu pilihan 1 Lanjut mengupdate tahun edisi buku, 2 Kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:

Jika user memilih pilihan 1 Lanjut mengupdate tahun edisi buku dengan memasukkan angka 1, maka user akan diminta memasukkan primary key berupa ISBN buku yang ingin diupdate tahun edisinya, kemudian akan dilakukan pengecekan apakah ada atau tidak buku yang memiliki ISBN sesuai inputan user, dari pengecekan tersebut ada beberapa kemungkinan:
    Jika ada maka user akan melihat tampilan detail informasi dari buku yang memiliki ISBN sesuai inputan user, lalu user mendapatkan pilihan mengenai kepastian apakah buku dengan ISBN tersebut jadi atau tidak untuk dilakukan update tahun edisinya, dari pilihan kepastian tersebut ada beberapa kemungkinan:
        Jika jadi untuk diupdate tahun edisinya maka user akan diminta memasukkan nama kolom yang bersesuaian untuk mengubah tahun edisi buku tersebut, dalam hal ini nama kolomnya EDISI, kemudian user diminta memasukkan tahun edisi terbaru, lalu user mendapatkan pilihan mengenai kepastian apakah jadi atau tidak untuk dilakukan update tahun edisi sesuai tahun edisi terbaru yang sudah dimasukkan, dari pilihan kepastian tersebut ada beberapa kemungkinan:
            Jika jadi untuk mengupdate tahun edisi buku tersebut maka user mendapatkan notifikasi Sedang mengupdate tahun edisi buku, harap menunggu, Anda berhasil mengupdate tahun edisi buku tersebut, lalu user diarahkan ke tampilan submenu

            Jika tidak jadi mengupdate tahun edisi buku tersebut, maka user akan diarahkan ke tampilan submenu
        
        Jika tidak jadi untuk diupdate tahun edisinya maka user akan diarahkan ke tampilan submenu
        
    Jika tidak ada maka user akan mendapatkan notifikasi Buku dengan ISBN yang Anda masukkan tidak ada sehingga tidak bisa dilakukan update, kemudian user diarahkan ke tampilan submenu

Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main

Jika user memasukkan angka selain 1 dan 2 maka user akan diarakan ke tampilan pilihan submenu
        
4. Menghapus buku (Delete Option)
Menu utama yang memiliki fitur create yaitu menu menambahkan buku yang dijalankan oleh fungsi delete1 ketika user memasukkan angka 4 di tampilan menu utama, tampilan awal saat memanggil fungsi nambah berupa SubMenu yang berisi 2 pilihan yaitu pilihan 1 Lanjut menghapus buku, 2 Kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:
Jika user memilih pilihan 1 lanjut menghapus buku dengan memasukkan angka 1, maka user akan diminta memasukkan primary key berupa ISBN buku yang ingin dihapus, kemudian akan dilakukan pengecekan apakah ada atau tidak buku yang memiliki ISBN sesuai inputan user, dari pengecekan tersebut ada beberapa kemungkinan:
    Jika terdapat buku dengan ISBN sesuai inputan user namun statusnya Dipinjam maka user akan mendapatkan notifikasi Terdapat buku dengan ISBN tersebut, namun tidak bisa dihapus karena buku tersebut sedang dipinjam, kemudian user akan diarahkan ke tampilan submenu

    Jika tidak terdapat buku dengan ISBN sesuai inputan user  maka user akan mendapatkan notifikasi Buku dengan ISBN tersebut tidak tersedia, kemudian user akan diarahkan ke tampilan submenu

    Jika terdapat buku dengan ISBN sesuai inputan user dengan statusnya tersedia maka user akan mendapatkan pilihan mengenai kepastian apakah buku dengan ISBN tersebut jadi atau tidak untuk dihapus, dari pilihan kepastian tersebut ada beberapa kemungkinan:
        Jika jadi untuk dihapus maka user akan mendapatkan notifikasi Sedang menghapus buku, harap menunggu, Anda berhasil menghapus buku dengan tersebut, kemudian user diarahkan ke tampilan submenu

        Jika tidak jadi maka user akan diarakan ke tampilan submenu

Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main

Jika user memasukkan angka selain 1 dan 2 maka user akan diarakan ke tampilan pilihan submenu


5. Menu Menampilkan daftar semua buku
Salah satu menu utama yang dijalankan menggunakan fungsi show ketika user memasukkan angka 5 di tampilan menu utama, tampilan pada menu ini menampilkan detail informasi dari buku buku yang statusnya tersedia dan dipinjam, user juga akan mendapatkan pilihan mengenai kepastian apakah ingin kembali ke menu utama atau tidak, dari pilihan kepastian tersebut ada beberapa kemungkinan:
    Jika user memilih kembali ke menu utama dengan memasukkan angka 1, maka user akan diarahkan ke tampilan menu utama
    Jika user memilih untuk tidak kembali ke menu utama dengan memasukkan angka 2, maka user akan kembali diarakan ke tampilan awal menu ini

6. Menu Meminjam buku
Salah satu menu utama yang dijalankan menggunakan fungsi minjam ketika user memasukkan angka 6 di tampilan menu utama, tampilan awal pada menu ini menampilkan submenu yang berisi 2 pilihan yaitu pilihan 1 Lanjut meminjam buku, pilihan 2 Kembali ke menu utama,dari pilihan tersebut ada beberapa kemungkinan:
    Jika user memilih pilihan 1 lanjut meminjam buku dengan memasukkan angka 1, maka akan dilakukan pengecekan batas peminjaman buku dengan melihat banyaknya buku yang sebelumnya user sudah pernah pinjam namun belum dikembalikan, batas maksimum peminjama buku sebanyak 3 buah, dari pengecekan tersebut ada beberapa kemungkinan:
        Jika user baru meminjam kurang dari 3 buku user dapat melihat tampilan daftar buku yang sedang dia pinjam (jika ada), kemudian akan dilakukan pengecekan apakah ada atau tidak buku yang tersedia, dari pengecekan tersebut ada beberapa kemungkinan:
            Jika ada buku yang tersedia, maka user akan dapat melihat detail informasi dari buku-buku yang tersedia, lalu user akan diminta memasukkan ISBN buku yang ingin dipinjam, kemudian akan dilakukan pengecekan apakah ada atau tidak buku yang tersedia yang memiliki ISBN sesuai inputan user, dari pengecekan tersebut ada beberapa kemungkinan:
                Jika ada maka user maka user akan mendapatkan pilihan mengenai kepastian apakah yakin ingin meminjam buku dengan ISBN tersebut, dari pilihan kepastian tersebut ada beberapa kemungkinan:
                    Jika user yakin ingin meminjam buku dengan ISBN tersebut maka user akan diminta memasukkan tanggal pengembalian buku harus dengan format waktu (yyyy-mm-dd), kemudian user akan mendapatkan pilihan mengenai kepastian apakah yakin ingin meminjam buku dengan ISBN tersebut dengan tanggal pengembalian inputan user, dari pilihan kepastian tersebut ada beberapa kemungkinan:
                        Jika jadi maka user akan mendapatkan notifikasi Selamat Anda telah berhasil meminjam buku tersebut, Pastikan Anda tepat waktu untuk mengembalikan buku tersebut paling lambat pada tanggal sesuai inputan user, lalu user akan diarahkan ke tampilan submenu

                        Jika tidak jadi maka user akan mendapatkan notifikasi Anda tidak jadi meminjam buku tersebut, mohon pastikan tanggal pengembalian buku saat meminjam, lalu user akan diarakan ke tampilan submenu

                    Jika user tidak yakin ingin meminjam buku dengan ISBN tersebut maka user akan mendapatkan notifikasi Anda tidak jadi meminjam buku tersebut, lalu user akan diarahkan ke tampilan submenu

                Jika tidak ada buku yang tersedia yang sesuai ISBN inputan user maka user akan mendapatkan notifikasi Tidak ada buku yang tersedia dengan ISBN tersebut, lalu user akan diarahkan ke tampilan submenu

            Jika tidak ada buku yang tersedia, maka user akan mendapatkan notifikasi Maaf tidak ada stok buku yang tersedia, lalu user akan diarahkan ke tampilan submenu
        Jika user sudah meminjam 3 buah buku maka user akan dapat melihat tampilan daftar buku yang sedang dia pinjam, dan user akan mendapatkan notifikasi Anda tidak bisa mmeminjam buku lagi Maksimal buku yang bisa dipinjam per mahasiswa sebanyak 3 buah, kemudian user akan diarahkan ke tampilan meu utama

    Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main

7. Menu Mengembalikan Buku
Salah satu menu utama yang dijalankan menggunakan fungsi kembali ketika user memasukkan angka 7 di tampilan menu utama, tampilan awal pada menu ini menampilkan submenu yang berisi 2 pilihan yaitu pilihan 1 Lanjut mengembalikan buku, pilihan 2 Kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:
    Jika user memilih pilihan 1 lanjut mengembalikan buku dengan memasukkan angka 1, maka akan dilakukan pengecekan apakah ada atau tidak buku yang sedang dipinjam oleh user untuk dikembalikan, dari pengecekan tersebut ada beberapa kemungkinan:
        Jika ada buku yang bisa dikembalikan maka user akan dapat melihat daftar buku yang dipinjam, lalu user diminta memasukkan nomor indeks dari tampilan daftar buku yang ingin dikembalikan, user akan mendapatkan pilihan mengenai kepastian apakah yakin ingin mengembalikan buku sesuai nomor indeks yang diinput user, dari pilihan kepastian tersebut ada beberapa kemungkinan:
            Jika jadi maka user akan mendapatkan notifikasi Anda telah berhasil mengembalikan buku tanpa dikenakan denda atau dikenakan denda, user juga dapat melihat daftar semua buku, lalu user diarahkan ke tampilan submenu
            Jika tidak jadi maka user akan mendapatkan notifikasi Anda tidak jadi mengembalikan buku tersebut, lalu user diarahkan ke tampilan submenu
        Jika tidak ada buku yang bisa dikembalikan dengan kata lain user tidak meminjam buku sebelumnya, maka user akan mendapatkan notifikasi Tidak ada buku yang bisa dikembalikan, Anda belum meminjam buku satupun, lalu user diarahkan ke tampilan submenu

    Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main

8. Menu Memperpanjang buku
Salah satu menu utama yang dijalankan menggunakan fungsi panjang ketika user memasukkan angka 8 di tampilan menu utama, tampilan awal pada menu ini menampilkan submenu yang berisi 2 pilihan yaitu pilihan 1 Lanjut memperpanjang buku, pilihan 2 Kembali ke menu utama, dari pilihan tersebut ada beberapa kemungkinan:
    Jika user memilih pilihan 1 lanjut memperpanjang buku dengan memasukkan angka 1, maka akan dilakukan pengecekan apakah ada atau tidak buku yang sedang dipinjam oleh user untuk diperpanjang, dari pengecekan tersebut ada beberapa kemungkinan:
        Jika ada buku yang dipinjam user sebelumnya maka user dapat melihat tampilan daftar buku yang sedang dia pinjam, kemudian user akan diminta memasukkan nomor indeks dari tampilan daftar buku yang ingin diperpanjang, user akan mendapatkan pilihan mengenai kepastian apakah yakin ingin memperpanjang buku sesuai nomor indeks yang diinput user, dari pilihan kepastian tersebut ada beberapa kemungkinan:        
            Jika user yakin ingin memperpanjang buku tersebut maka user mendapatkan notifikasi terkena denda atau tidak tergantung tanggal pemgembalian yang lama, dan user akan diminta memasukkan tanggal pengembalian buku yang baru harus dengan format waktu (yyyy-mm-dd), kemudian user akan mendapatkan pilihan mengenai kepastian apakah yakin ingin menperpanjang buku sesuai dengan tanggal pengembalian inputan user yang baru, dari pilihan kepastian tersebut ada beberapa kemungkinan:
                Jika jadi maka user akan mendapatkan notifikasi Selamat Anda telah berhasil memperpanjang buku tersebut, Pastikan Anda tepat waktu untuk mengembalikan buku tersebut, lalu user akan diarahkan ke tampilan submenu

                Jika tidak jadi maka user akan mendapatkan notifikasi Anda tidak jadi memperpanjang buku tersebut mohon pastikan tanggal pengembalian buku terbaru saat meminjam, lalu user akan diarakan ke tampilan daftar buku yang tersedia pada fungsi show

            Jika user tidak yakin ingin memperpanjang buku tersebut maka user mendapatkan notifikasi Anda tidak jadi memperpanjang buku tersebut, lalu user akan diarakan ke tampilan submenu

        Jika ada buku yang dipinjam user sebelumnya maka user akan mendapatkan notifikasi Tidak ada buku yang bisa diperpanjang, Anda belum meminjam buku satupun, lalu user akan diarakan ke tampilan submenu

    Jika user memilih memilih pilihan 2 kembali ke menu utama dengan memasukkan angka 2, user akan diarahkan ke tampilan menu utama di fungsi main


9. Menu Log in ulang
Salah satu menu utama yang dijalankan menggunakan fungsi login ketika user memasukkan angka 9 di tampilan menu utama, pada menu ini user akan diminta menginput nama user sebagai pengunjung perpustakaan yang memiliki NIS/NIP dan menginput NIS/NIP milik user (Nomor Induk Siswa atau Nomor Induk Pegawai bagi guru)

10. Exit
Salah satu menu utama yang ketika dijalankan oleh user akan menghentikan aplikasi program 


Khusus pilihan menu "Menambahkan buku" dan "Menghapus buku", sebelum bisa menjalankan ke fungsi yang bisa memanggil keduanya, user akan diminta memasukkan password terlebih dahulu, jika user tidak tau passwordnya maka user bisa memilih untuk kembali ke menu utama mengikuti perintah yang tersedia (Passwordnya:jcds01)

## Contribute

If you'd like to contribute to Perpustakaan Sains Yogya, check out https://github.com/andimrs/CapstoneProject.git

