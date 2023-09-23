# Game Manajerial Candi

## Deskripsi 
Project ini merupakan program Manejerial Candi yang didasarkan pada kisah 
Candi Prambanan, dengan tokoh utama Bandung Bondowoso dan Roro Jonggrang. Bandung mempunyai
kekuasaan untuk memanggil jin dan membangun candi sedangkan Roro mempunyai kekuasaan untuk
menghancurkan candi dan menyelesaikan permainan saat matahari muncul.

## Cara Memainkan
untuk memulai, silahkan jalankan "python main.py {nama folder}", nama folder disini
merupakan folder save (24-09-2023) yang digunakan untuk menyimpan data berupa 3 file excel yang
akan dibaca nantinya untuk menjalankan game ini
Secara default, terdapat data login untuk Bandung Bondowoso dan Roro Jonggrang yang dapat
diakses melalui user.csv di save/24-09-2023.
Setelah login dengan salah satu role utama yang ada, pemain dapat memainkan sesuai peran yang
dipilih, peran yang ada adalah sebagai Bandung, Roro, ataupun Jin. Pengguna dapat melakukan command
help untuk mengetahui apa saja yang dapat dilakukan oleh tiap role yang sedang dipilih.
Secara singkat, Bandung dapat mensummon jin, menghapus jin, mengubah jin, melalukan batch,
dan menerima laporan jin dan candi sedangkan Roro dapat menghancurkan candi dan melakukan command
ayamberkokok yang dapat menyelesaikan permainan yang sedang berjalan.
Jin yang telah di summon dapat kita gunakan dengan login sebagai jin tersebut,
(harap logout dahulu sebelum login dengan user baru yang ada) terdapat 2 jin yaitu
jin pengumpul dan jin pembangun. Jin pembangun akan membangun jika bahan yang dikumpulkan oleh
jin pengumpul cukup. Namun, terdapat opsi batch juga yang dapat langsung mengumpulkan bahan atau
membangun candis secara sekaligus berdasarkan jumlah jin yang ada. Jin juga dapat di hapus oleh
Bandung jika berkenan.
Permainan akan selesai jika Bandung berhasil membangun 100 candi atau Roro melaksanakan command
ayamberkokok sebelum 100 candi berhasil di bangun.

## Spesifikasi
Program ini menggunakan Python yang membaca dan menggunakan data .csv sebagai database permainan.
Data .csv dapat di akses dan di edit sebagaimana permainan ini berjalan sebagai data user, data candi,
dan bahan bangunan. 


