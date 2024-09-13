# **🚀TAKHOR🚀**

At **Takhor**, we specialize in bringing joy to your daily life with our unique, high-quality squishies. Whether you're looking for a fun stress reliever or a cute addition to your collection, we've got you covered!

### Why Choose Takhor?

- **Soft & Satisfying**: Perfect for squeezing away stress.
- **Variety of Designs**: Cute, quirky, and colorful!
- **Affordable Prices**: Get the best deals for premium squishies.

Curious?🤔 <br />
Check our website [here](http://grace-karina31-takhor.pbp.cs.ui.ac.id) <br />
Last updated deployment link: Rabu, 11 September 2024 (10.18) [Status: not working]


## **Tugas 2 PBP 2024/2025**

**Nama**: Grace Karina <br />
**Kelas**: PBP F <br />
**NPM**: 2306275834

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?**

- **Membuat Proyek Django** <br />
  Setelah, direktori bernama Takhor dibuat, kita menginstall dependencies yang kita butuhkan. Django merupakan salah satunya.
  Kemudian, jalankan perintah `django-admin startproject [nama project] .`
- **Membuat aplikasi dengan nama main pada proyek tersebut.** <br />
  Untuk membuat direktori main, kita harus menjalankan kode `python manage.py startapp main`. Django akan membuat sebuah folder baru dengan nama main (nama aplikasi yang kamu berikan)
  yang berisi beberapa file dan struktur dasar aplikasi Django
- **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.** <br />
  Untuk membuat routing, di dalam direktori main, kita membuat `urls.py` dan menaruh URL yang diinginkan
- **Membuat model pada aplikasi main** <br />
  Menambah Model sesuai dengan atribut yang diinginkan di `models.py`. Setiap field memiliki tipe data yang sesuai seperti `CharField`, `DateField`, `IntegerField`, dan `TextField`.
  Kemudian, jangan lupa untuk memigrasikan model agar setiap perubahan dapat dilacak.
- **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.** <br />
  Di dalam views, fungsi mengambil parameter request dan mengembalikan `request`, `"file_kalian.html"`, `context`. Hal ini untuk mengembalikan tampilan yang diinginkan pengguna
- **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.** <br />
  Membuat file `urls.py` di `main` dan menambahkan url yang diinginkan. File ini berfungsi untuk menentukan rute URL (URL routing) yang menghubungkan URL yang diminta pengguna dengan fungsi atau tampilan (view) yang akan diproses oleh Django.
- **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.** <br />
  Akses halaman [pws](https://pbp.cs.ui.ac.id.) dan register jika belum memiliki akun. Kemudian, login dengan akun masing-masing dan tekan `Create New Project`.
  Pada settings.py di proyek Django yang sudah dibuat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`. Kemudiaan isi credentials yang sudah diberikan.

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![Bagan](/bagan.png)

Alur permintaan pada aplikasi web Django dimulai saat klien mengirim permintaan HTTP ke server. `urls.py` menerima permintaan dan mengarahkannya ke fungsi yang sesuai di `views.py`. Views memproses permintaan dan bekerja dengan `models.py` jika perlu untuk read/write data. Setelah pemrosesan, view merender template HTML dengan data yang telah diolah. Hasilnya dikembalikan sebagai respons HTTP ke klien melalui server Django.

**3. Jelaskan fungsi git dalam pengembangan perangkat lunak!** <br />

&nbsp;&nbsp;&nbsp;**Fungsi git:**

- Git memungkinkan pengguna untuk melacak perubahan kode secara berkelanjutan. Setiap perubahan yang dilakukan dapat disimpan sebagai versi baru tanpa menghapus versi
  sebelumnya.
- Git mendukung kolaborasi antara banyak pengguna. Fitur branching (percabangan) memungkinkan tim bekerja pada berbagai fitur atau perbaikan bug secara bersamaan tanpa
  mengganggu kerja orang lain.
- Git dapat dijadikan backup
- Git mempermudah untuk menerima kontribusi dari luar melalui pull request dan forking, sekaligus memberikan kendali penuh pada pemilik proyek untuk memilih apa yang akan
  dimasukkan ke dalam proyek utama.
- Git memberikan jejak audit yang jelas yang berguna untuk melacak asal-usul bug atau masalah di masa depan.

**4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?** <br />

Django dirancang dengan pendekatan yang sangat terstruktur, yang secara alami mendorong pengguna untuk mengikuti **praktik terbaik (best practices)** dalam pengembangan perangkat lunak. Salah satu contohnya adalah penggunaan arsitektur **Model-View-Template (MVT)**, yang memisahkan logika bisnis (Model), tampilan (Template), dan kontrol alur data (View). Dengan pendekatan ini, pengelolaan kode menjadi lebih terorganisir, mudah dipahami, serta lebih efisien. Ditambah lagi, Django sangat ramah bagi pemula karena menyediakan banyak fitur bawaan yang memudahkan developer baru untuk memulai tanpa harus mempelajari terlalu banyak konfigurasi.

**5. Mengapa model pada Django disebut sebagai ORM?** <br />

Model pada Django disebut ORM karena memberikan lapisan abstraksi yang memetakan objek-objek Python ke dalam tabel database relasional sehingga memungkinkan pengguna untuk bekerja dengan database menggunakan kode Python tanpa harus menulis SQL secara langsung.
