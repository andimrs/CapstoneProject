# Perpustakaan Sains Yogya

Aplikasi Perpustakaan merupakan aplikasi sederhana yang dibuat menggunakan bahasa pemrograman Python yang bertujuan untuk melayani siswa atau guru dalam mencari, mengubah, menghapus, dan menyimpan suatu data selama mereka berkegiatan di dalam perpustakaan. Kegiatan perpustakaan meliputi menampilkan daftar buku tertentu, mengubah tahun edisi buku, menambah buku, menghapus buku, meminjam buku, memperpanjang buku, mengembalikan buku, dsb.

Aplikasi ini dibuat dengan beberapa fungsi dalam python. Selain untuk mengefisiensikan program yang dijalankan, penerapan fungsi juga memudahkan kita menjelaskan alur dari program yang dijalankan beserta fitur yang digunakan sehingga aplikasi yang dibuat terintegrasi. 

## Installation


## Fitur CRUD 

Fitur Create, Read, Update, dan Delete (CRUD) merupakan fitur standar yang harus ada jika kita ingin membuat suatu aplikasi menggunakan Python. Fungsi dari fitur tersebut memungkinkan kita untuk melakukan manipulasi data, dalam hal ini berupa data di dalam collection data type melalui aplikasi yang dibuat. 
Fitur Create (Menambahkan Data) adalah proses untuk menambahkan data ke dalam collection data type yang digunakan berdasarkan user input.
Fitur Read (Menampilkan Data) adalah proses untuk menampilkan seluruh data dari data collection yang ada maupun menampilkan data tertentu sesuai pilihan user.
Fitur Update (Mengubah  Data) adalah proses mengubah value dari kolom items data collection yang dipilih oleh user.
Fitur Delete (Menghapus Data) adalah proses menghapus data dari data collection berdasarkan user input.


## Quickstart Guide
•	Collection Data Type

Collection Data Type yang digunakan dalam aplikasi ini berupa dictionary dengan value dari masing-masing key berupa list. Variabel yang memuat collection data type didefinisikan sebagai listBuku.

•	Fungsi login

Fungsi login akan dipanggil ketika user baru pertama kali menjalankan program sebelum masuk ke menu utama, atau dengan memilih Menu 9 yaitu "Log in ulang" pada fungsi main. Pada menu ini user akan diminta menginput nama user sebagai pengunjung perpustakaan yang memiliki NIS/NIP dan menginput NIS/NIP milik user (Nomor Induk Siswa atau Nomor Induk Pegawai bagi guru).


•	Fungsi main

Fungsi main yang akan dipanggil ketika user berhasil memasukkan nama dan NIS/NIP dengan benar pada fungsi login. Fungsi ini juga bisa dipanggil ketika ada pilihan ‘Kembali ke menu utama’ yang dijalankan oleh user. Fungsi main menampilkan 10 menu yang dapat dipilih oleh user. Jika user memilih Menu 10 yaitu Exit maka user akan keluar dari aplikasi program yang dijalankan.

•	Fungsi nambah

Fungsi nambah akan dipanggil saat user memilih Menu 1 yaitu “Menambahkan buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Menambahkan buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Create dalam menu ini, dengan menambahkan data buku ke dalam collection data type yang digunakan jika user berhasil untuk menambahkan buku sesuai ketentuan. 

Terdapat 4 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 3 output dari Pilihan 1 dan 1 output dari Pilihan 2. Pertama, user tidak dapat menambahkan buku karena ISBN yang diinput sudah terdaftar, artinya ada duplikat buku, kemudian user diarahkan ke pilihan submenu. Kedua, user tidak jadi menambahkan buku setelah menginput ISBN yang belum terdaftar, judul, dan tahun edisi, kemudian user diarahkan ke pilihan submenu. Ketiga, user jadi untuk menambahkan buku setelah menginput ISBN yang belum terdaftar, judul, dan tahun edisi, kemudian user diarahkan ke pilihan submenu. Keempat, user kembali ke menu utama karena memilih pilihan 2.

•	Fungsi show2

Fungsi show2 akan dipanggil saat user memilih Menu 2 yaitu “Menampilkan daftar buku tertentu” pada fungsi main. Terdapat 3 pilihan di submenu pada Menu 2 yang dapat dipilih user, yaitu Pilihan 1 Melihat semua daftar buku yang tersedia, Pilihan 2 Mencari buku tertentu yang tersedia, dan Pilihan 3 Kembali ke Menu Utama. Terdapat juga Fitur Read dalam menu ini, dengan menampilkan seluruh buku yang tersedia maupun menampilkan buku tersedia dengan ISBN tertentu dari data collection sesuai pilihan user.

Terdapat 6 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 2 output dari Pilihan 1, 3 output dari Pilihan 2, dan 1 output dari Pilihan 3. Pertama, user mendapatkan notifikasi bahwa tidak ada buku yang tersedia di perpustakaan saat memilih Pilihan 1, kemudian user diarahkan ke pilihan submenu. Kedua, user dapat melihat semua daftar buku yang tersedia, kemudian user diarahkan ke pilihan submenu. Ketiga, user mendapatkan notifikasi bahwa tidak ada buku yang tersedia di perpustakaan saat memilih Pilihan 2, kemudian user diarahkan ke pilihan submenu. Keempat, user mendapatkan notifikasi bahwa tidak ada buku yang tersedia yang memiliki ISBN sesuai inputan user, kemudian user diarahkan ke pilihan submenu. Kelima, user dapat melihat buku yang tersedia yang memiliki ISBN sesuai inputan user, kemudian user diarahkan ke pilihan submenu. Keenam, user kembali ke menu utama karena memilih pilihan 3.  

•	Fungsi update

Fungsi update akan dipanggil saat user memilih Menu 3 yaitu “Mengupdate tahun edisi buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Mengupdate tahun edisi buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Update dalam menu ini, dengan mengubah value dari kolom edisi data collection berdasarkan ISBN buku yang dipilih oleh user.

Terdapat 5 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 4 output dari Pilihan 1 dan 1 output dari Pilihan 2. Pertama, user mendapatkan notifikasi bahwa tidak bisa dilakukan update karena buku dengan ISBN inputan user tidak ada di perpustakaan, kemudian user diarahkan ke pilihan submenu. Kedua, user tidak jadi mengupdate tahun edisi buku dengan ISBN sesuai inputan user, kemudian user diarahkan ke pilihan submenu. Ketiga, user tidak jadi mengupdate tahun edisi buku dengan ISBN sesuai inputan user setelah menginput tahun edisi buku terbaru,  kemudian user diarahkan ke pilihan submenu. Keempat, user berhasil mengupdate mengupdate tahun edisi buku menjadi tahun terbaru dengan ISBN buku sesuai inputan user, kemudian user diarahkan ke pilihan submenu. Kelima, user kembali ke menu utama karena memilih pilihan 2.    

•	Fungsi Delete

Fungsi delete akan dipanggil saat user memilih Menu 4 yaitu “Menghapus buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Menghapus buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Delete dalam menu ini, dengan menghapus data buku dari data collection berdasarkan ISBN buku yang user input.

Terdapat 5 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 4 output dari Pilihan 1 dan 1 output dari Pilihan 2. Pertama, user mendapatkan notifikasi bahwa tidak bisa menghapus buku karena buku dengan ISBN inputan user tidak ada di perpustakaan, kemudian user diarahkan ke pilihan submenu. Kedua, user mendapatkan notifikasi bahwa ada buku dengan ISBN tersebut namun tidak bisa dihapus karena sedang dipinjam, kemudian user diarahkan ke pilihan submenu. Ketiga, user tidak jadi menghapus buku dengan ISBN sesuai inputan user,  kemudian user diarahkan ke pilihan submenu. Keempat, user berhasil menghapus buku dengan ISBN buku sesuai inputan user, kemudian user diarahkan ke pilihan submenu. Kelima, user kembali ke menu utama karena memilih pilihan 2.    

•	Fungsi show1

Fungsi show1 akan dipanggil saat user memilih Menu 5 yaitu “Menampilkan daftar semua buku” pada fungsi main. User akan melihat daftar semua buku baik yang tersedia maupun yang dipinjam. User dapat memilih pilihan untuk kembali ke menu utama jika dirasa user sudah cukup untuk melihat semua daftar buku. Terdapat Fitur Read dalam menu ini, dengan menampilkan seluruh buku yang tersedia. 

•	Fungsi minjam

Fungsi minjam akan dipanggil saat user memilih Menu 6 yaitu “Meminjam buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Meminjam buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Read dan Fitur Update dalam menu ini, dengan menampilkan daftar buku yang sebelumnya dipinjam dan daftar buku yang tersedia untuk dipinjam, serta jika user jadi untuk meminjam buku tertentu maka kolom status, peminjam, NIS/NIP, tanggal pinjam, dan tanggal pengembalian akan berubah.

Terdapat 7 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 5 output dari Pilihan 1 dan 1 output dari Pilihan 2. Pertama, user mendapatkan notifikasi bahwa tidak bisa meminjam buku karena user sudah meminjam 3 buah buku, kemudian user diarahkan ke menu utama. Kedua, user mendapatkan notifikasi bahwa tidak ada buku yang tersedia sehingga tidak ada buku yang bisa dipinjam, kemudian user diarahkan ke pilihan submenu. Ketiga, user mendapatkan notifikasi bahwa tidak ada buku yang bisa dipinjam dengan ISBN buku sesuai inputan user,  kemudian user diarahkan ke pilihan submenu. Keempat, user tidak jadi meminjam buku dengan ISBN inputan user, kemudian user diarahkan ke pilihan submenu. Kelima, user tidak jadi meminjam buku dengan ISBN inputan user setelah memasukkan tanggal pengembalian, kemudian user diarahkan ke pilihan submenu. Keenam, user mendapatkan notifikasi bahwa buku berhasil dipinjam, kemudian user diarahkan ke pilihan submenu. Ketujuh, user kembali ke menu utama karena memilih pilihan 2.    

•	Fungsi kembali

Fungsi kembali akan dipanggil saat user memilih Menu 7 yaitu “Mengembalikan buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Mengembalikan buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Read dan Fitur Update dalam menu ini, dengan menampilkan daftar buku yang sebelumnya dipinjam untuk dikembalikan, serta jika user jadi untuk mengembalikan buku tertentu maka kolom status, peminjam, NIS/NIP, tanggal pinjam, dan tanggal pengembalian akan berubah.

Terdapat 4 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 3 output dari Pilihan 1 dan 1 output dari Pilihan 2.Pertama, user mendapatkan notifikasi bahwa tidak ada buku yang bisa dikembalikan, kemudian user diarahkan ke pilihan submenu. Kedua, user tidak jadi mengembalikan buku yang sebelumnya dipinjam oleh user, kemudian user diarahkan ke pilihan submenu. Ketiga, user mendapatkan notifikasi bahwa buku berhasil dikembalikan, kemudian user diarahkan ke pilihan submenu. Keempat, user kembali ke menu utama karena memilih pilihan 2.    

•	Fungsi panjang

Fungsi panjang akan dipanggil saat user memilih Menu 8 yaitu “Memperpanjang buku” pada fungsi main. Terdapat 2 pilihan di submenu pada Menu 1 yang dapat dipilih user, yaitu Pilihan 1 Lanjut Memperpanjang buku dan Pilihan 2 Kembali ke Menu Utama. Terdapat juga Fitur Read dan Fitur Update dalam menu ini, dengan menampilkan daftar buku yang sebelumnya dipinjam untuk diperpanjang, serta jika user jadi untuk memperpanjang buku tertentu maka kolom peminjam, tanggal pinjam, dan tanggal pengembalian akan berubah.

Terdapat 5 kemungkinan output yang bisa user dapatkan jika memanggil fungsi ini, 4 output dari Pilihan 1 dan 1 output dari Pilihan 2.Pertama, user mendapatkan notifikasi bahwa tidak ada buku yang bisa diperpanjang, kemudian user diarahkan ke pilihan submenu. Kedua, user tidak jadi memperpanjang buku yang dipinjam oleh user, kemudian user diarahkan ke pilihan submenu. Ketiga, user tidak jadi memperpanjang buku setelah memasukkan tanggal pengembalian, kemudian user diarahkan ke pilihan submenu. Keempat, user mendapatkan notifikasi bahwa buku berhasil diperpanjang, kemudian user diarahkan ke pilihan submenu. Kelima, user kembali ke menu utama karena memilih pilihan 2.    


•	Catatan

Khusus pilihan Menu 1 "Menambahkan buku" dan Menu 4 "Menghapus buku", sebelum bisa menjalankan ke fungsi yang bisa memanggil keduanya, user akan diminta memasukkan password terlebih dahulu, jika user tidak mengetahui passwordnya maka user bisa memilih untuk kembali ke menu utama mengikuti perintah yang tersedia (Password:jcds01)

## Contribute

If you'd like to contribute to Perpustakaan Sains Yogya, check out https://github.com/andimrs/CapstoneProject.git, thank you

