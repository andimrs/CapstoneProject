# Aplikasi Perpustakaan Sains

Sebuah layanan aplikasi menggunakan bahasa pemrograman Python yang dapat membantu siswa dan guru untuk mencari, menghapus, mengubah, dan menyimpan suatu data buku selama mereka melakukan kegiatan di dalam perpustakaan. Kegiatan yang dapat mereka lalukan meliputi menampilkan informasi dari suatu buku,  meminjam, mengembalikan, dan memperpanjang buku, memperbarui tahun edisi buku, serta menambahkan dan menghapus data suatu buku.

## Instalasi

Untuk mengkloning dari github, jalankan kode berikut:

    mkdir folder
    cd folder
    git clone git@github.com:nornh/capstone_project.git

Untuk menginstal persyaratan yang dibutuhkan menggunakan pip, jalankan kode berikut:

    pip install -r requirement.txt

## Panduan Cepat


Dalam aplikasi ini terdapat 10 menu utama yang dapat dijalankan oleh user yaitu:
1. Menampilkan Daftar Semua Buku 
2. Menampilkan Daftar Buku Tertentu
3. Meminjam Buku
4. Mengembalikan Buku
5. Memperpanjang Buku
6. Menambahkan Buku
7. Mengupdate Tahun Edisi Buku 
8. Menghapus Buku
9. Log In Kembali
10. Exit

Program yang dibangun dibentuk dari beberapa fungsi berikut:
1. Fungsi login()
    <br>Fungsi login akan dijalankan ketika user baru pertama kali menjalankan program sebelum masuk ke menu utama, atau dengan memilih Menu 9 yaitu "Log In Kembali" di halaman menu utama. Pada menu ini user akan diminta menginputkan nama dan nomor pengenal dalam hal ini siswa atau guru sebagai pengunjung perpustakaan yang memiliki NIS/NIP (Nomor Induk Siswa bagi siswa atau Nomor Induk Pegawai bagi guru).
2. Fungsi main()
    <br>Fungsi main yang akan dijalankan ketika user berhasil memasukkan nama dan NIS/NIP dengan benar pada fungsi login. Fungsi ini juga bisa dijalankan ketika user memilih pilihan "Kembali ke menu utama". Pada Fungsi main menampilkan 10 menu utama yang dapat dipilih oleh user, beberapa menu diantaranya setelah dipilih user akan diminta untuk memasukkan password. Jika user memilih Menu 10 yaitu Exit maka user akan keluar dari aplikasi program yang dijalankan.
3. Fungsi show()
    <br>Fungsi show akan dijalankan ketika user memilih Menu 1 yaitu "Menampilkan daftar semua buku" pada fungsi main. User dapat melihat daftar semua buku berdasarkan urutan tertentu baik yang tersedia maupun yang sedang dipinjam.
4. Fungsi show2()
    <br>Fungsi show2 akan dijalankan ketika user memilih Menu 2 yaitu "Menampilkan Daftar Buku Tertentu" pada fungsi main. User dapat melihat daftar buku daftar buku yang tersedia dan mengecek status ketersediaan buku tertentu.
5. Fungsi minjam()
    <br>Fungsi minjam akan dijalankan ketika user memilih Menu 3 yaitu "Meminjam buku" pada fungsi main. Pada fungsi minjam ini user dapat meminjam buku yang tersedia dengan memasukkan kode ISBN ((International Standard Book Number)) buku yang ingin dipinjam, yang merupakan kode pengidentifikasian buku yang bersifat unik, kemudian user akan diminta untuk mengisi data terkait peminjaman buku.
6. Fungsi batas()
    <br>Fungsi batas akan dijalankan ketika user memilih pilihan "Lanjut Meminjam buku" pada fungsi minjam. Fungsi ini akan menentukan apakah user dapat meminjam buku atau tidak dengan membandingkan antara total buku yang sudah dipinjam oleh user sebelumnya dengan batas maksimal jumlah buku yang bisa dipinjam per user.
7. Fungsi waktu_minjam()
    <br>Fungsi waktu_minjam akan dijalankan ketika user memilih pilihan "Ya" saat menjawab pertanyaan pada "Apakah Anda yakin meminjam buku dengan judul X edisi Y ISBN Z" pada fungsi minjam. Fungsi ini mengatur waktu pengembalian buku sesuai ketentuan, lamanya waktu pinjam terhitung sejak tanggal peminjaman buku.
8. Fungsi kembali()
    <br>Fungsi kembali akan dijalankan ketika user memilih Menu 4 yaitu "Mengembalikan buku" pada fungsi main. Pada fungsi kembali ini user dapat mengembalikan buku yang dipinjam dengan memasukkan no indeks yang sesuai pada daftar buku yang ditampilkan.
9. Fungsi waktu_kembali()
    <br>Fungsi waktu_kembali akan dijalankan ketika user memilih pilihan "Ya" saat menjawab pertanyaan pada "Apakah Anda yakin mengembalikan buku dengan judul X edisi Y ISBN Z hari ini" pada fungsi kembali. Fungsi ini akan menampilkan informasi berupa ada atau tidaknya denda yang dibebankan kepada user dengan melihat tanggal pengembalian yang telah disepakati.
10. Fungsi panjang()
    <br>Fungsi panjang akan dijalankan ketika user memilih Menu 5 yaitu "Memperpanjang buku" pada fungsi main. Pada fungsi panjang ini user dapat memperpanjang buku yang dipinjam dengan memasukkan no indeks yang sesuai pada daftar buku yang ditampilkan.
11. Fungsi waktu_panjang()
    <br>Fungsi waktu_panjang akan dijalankan ketika user memilih pilihan "Ya" saat menjawab pertanyaan pada "Apakah Anda yakin memperpanjang buku dengan judul X edisi Y ISBN Z" pada fungsi kembali. Fungsi ini akan menampilkan informasi berupa ada atau tidaknya denda yang dibebankan kepada user dengan melihat tanggal pengembalian yang telah disepakati, dan juga mengatur waktu pengembalian buku yang baru sesuai ketentuan, lamanya waktu pinjam terhitung sejak tanggal peminjaman buku.
12. Fungsi nambah()
    <br>Fungsi nambah akan dijalankan ketika user memilih Menu 6 yaitu “Menambahkan buku” pada fungsi main. User dapat menambahkan buku ke dalam suatu penyimpanan jika nomor ISBN buku tersebut belum terdaftar dalam penyimpanan buku, selanjutnya user diarahkan untuk mengisi informasi data buku tersebut. 
13. Fungsi update()
    <br>Fungsi update akan dijalankan ketika user memilih Menu 7 yaitu “Mengupdate Tahun Edisi Buku” pada fungsi main. Pada fungsi update ini user dapat mengupdate tahun edisi buku dengan memasukkan kode ISBN buku yang ingin diperbarui tahun edisinya, kemudian user akan diminta untuk mengisi kembali tahun edisi terbaru buku tersebut.
14. Fungsi delete1()
    <br>Fungsi delete1 akan dijalankan ketika user memilih Menu 8 yaitu “Menghapus Buku” pada fungsi main. Pada fungsi delete1 ini user dapat menghapus buku tertentu yang tersedia dengan memasukkan kode ISBN buku yang ingin dihapus dari penyimpanan.

## Catatan

Dalam program ini Anda bisa mengatur:
 1. Banyaknya buku dan informasi terkait data buku tersebut
 2. Tanggal waktu kunjung atau waktu saat program dijalankan
 3. Batas jumlah peminjaman buku
 4. Maksimal dan minimal waktu peminjaman buku
 5. Password untuk mengakses beberapa menu

 Pengaturan Awal Program:
 1. Terdapat 5 buku, 3 buku sudah dipinjam oleh satu orang yang sama dan 2 buku sisanya tersedia 
 2. Tanggal waktu kunjung atau waktu saat program dijalankan yaitu 2023-05-24
 3. Batas jumlah peminjaman buku sebanyak 3 buah per orang dengan kode uniknya NIS/NIK
 4. Maksimal dan minimal waktu peminjaman buku berturut-turut 7 hari dan 1 hari dari tanggal peminjaman buku
 5. Passwordnya jcds01, yang harus dimasukkan saat ingin mengakses menu Menambahkan Buku,Mengupdate Tahun Edisi Buku, dan Menghapus Buku

## Kontribusi

Jika anda ingin berkontribusi untuk mengembangkan Aplikasi Perpustakaan ini, atau ingin memberi komentar berupa saran kritik dan masukan, silahkan Anda kunjungi link berikut:  https://github.com/andimrs/CapstoneProject.git. Terima Kasih.

