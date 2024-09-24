# **🚀TAKHOR🚀**

At **Takhor**, we specialize in bringing joy to your daily life with our unique, high-quality squishies. Whether you're looking for a fun stress reliever or a cute addition to your collection, we've got you covered!

### Why Choose Takhor?

- **Soft & Satisfying**: Perfect for squeezing away stress.
- **Variety of Designs**: Cute, quirky, and colorful!
- **Affordable Prices**: Get the best deals for premium squishies.

Curious?🤔 <br />
Check our website [here](http://grace-karina31-takhor.pbp.cs.ui.ac.id) <br />

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
![Bagan](/image-readme/bagan.png)

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

## **Tugas 3 PBP 2024/2025**

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?** <br/>

Data delivery diperlukan untuk memastikan pengelolaan dan distribusi data yang efisien, terutama dalam platform yang mengandalkan penggunaan data dalam jumlah besar dari berbagai sumber. Data delivery juga penting untuk menjaga kecepatan dan latensi rendah, memungkinkan data untuk dikirimkan dengan cepat dan tepat waktu ke komponen atau pengguna yang membutuhkan. Selain itu, data delivery memastikan konsistensi data sehingga seluruh pihak yang terlibat mendapatkan versi data yang akurat.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?** <br/>

JSON (JavaScript Object Notation) lebih baik dibandingkan XML karena lebih sederhana, mudah dibaca, dan lebih efisien dalam hal ukuran data. JSON memiliki struktur yang lebih ringkas dan dapat diintegrasikan langsung dengan JavaScript, menjadikannya ideal untuk diaplikasikan. Selain itu, JSON lebih cepat dalam parsing dan pengiriman data karena tidak membutuhkan tag pembuka dan penutup seperti XML. Walaupun begitu, XML masih bermanfaat dalam data yang lebih kompleks, seperti file konfigurasi dan format yang lebih formal (misalnya, RSS feeds atau SVG).

**3. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?** <br/>

Method `is_valid()` pada form Django berfungsi untuk memvalidasi data yang dikirimkan melalui form. Ketika method ini dipanggil, Django akan memeriksa apakah data yang dimasukkan sesuai dengan aturan validasi yang telah didefinisikan dalam form, seperti tipe data yang benar atau batasan karakter. Jika data valid, `is_valid()` akan mengembalikan nilai `True`, dan data bersih yang sudah divalidasi akan tersedia di atribut `cleaned_data`. Jika tidak valid, method ini mengembalikan `False` dan menyediakan pesan kesalahan.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?** <br/>

Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari **serangan Cross-Site Request Forgery (CSRF)**. CSRF adalah jenis serangan di mana penyerang dapat membuat permintaan tak sah atas nama pengguna yang sah tanpa sepengetahuannya. Dengan menambahkan `csrf_token` pada form, Django memastikan bahwa setiap permintaan POST berasal dari sumber yang sah (pengguna yang valid) karena token unik ini hanya diketahui oleh server dan pengguna.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)** <br/>

### Membuat form

**Langkah 1: Membuat file `forms.py` yang berisi model dari form berisi dengan fields yang lengkap** <br />

```python
class ProductForm(ModelForm):
    class Meta:
        model = ProductakhorModel
        fields = ['name', 'price', 'description', 'image', 'quantity']
```

**Langkah 2: Di dalam `views.py` di direktori main, kita membuat fungsi create_product entry dan menambah import yang diperlukan. Kita menambahkan files karena kita mempunyai fitur image yang akan ditampilkan di website nanti** <br/>

```python
def create_product_entry(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'create_product_entry.html', context)
```

**Langkah 3: Membuat template HTML untuk menampilkan form dan menambahkan di url**

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product_entry, name='create_product_entry'),
]
```

### Membuat format XML dan JSON

**Langkah 1: Membuat view untuk XML, JSON, XML by ID, dan JSON by ID**

```python
def show_xml(request):
    product_entries = ProductakhorModel.objects.all()
    data = serializers.serialize('xml', product_entries)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    product_entries = ProductakhorModel.objects.all()
    data = serializers.serialize('json', product_entries)
    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    product_entries = ProductakhorModel.objects.get(id=id)
    data = serializers.serialize('xml', [product_entries])
    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    product_entries = ProductakhorModel.objects.get(id=id)
    data = serializers.serialize('json', [product_entries])
    return HttpResponse(data, content_type='application/json')
```

**Langkah 2: Membuat Routing URL untuk views dalam format JSON dan XML ke dalam `urls.py`.**

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Hasil akses URL pada Postman

**Hasil dari JSON**
![json](/image-readme/json.png)

**Hasil dari XML**
![xml](/image-readme/xml.png)

**Hasil dari JSON by ID**
![json by ID](/image-readme/json-by-id.png)

**Hasil dari XML by ID**
![XML by ID](/image-readme/xml-by-id.png)


## **Tugas 4 PBP 2024/2025**

**1. Apa perbedaan antara ```HttpResponseRedirect()``` dan ```redirect()```?** <br/>

```HttpResponseRedirect()``` dan ```redirect()``` keduanya digunakan dalam Django untuk mengarahkan pengguna ke URL lain, tetapi ada beberapa perbedaan dalam pemakaiannya. ```HttpResponseRedirect()``` adalah kelas yang secara langsung membuat respons HTTP yang mengarahkan pengguna ke URL yang ditentukan dan pengguna harus secara manual memberikan URL tersebut dalam bentuk string. Sebaliknya, ```redirect()``` adalah fungsi yang lebih fleksibel karena secara otomatis menangani berbagai jenis input, seperti nama URL (dari file   ```urls.py```), objek model, atau URL string biasa. 

**2. Jelaskan cara kerja penghubungan model ```Product``` dengan ```User```!** <br/>

Untuk menghubungkan model ```Product``` dengan model ```User``` di Django, kita menggunakan relasi **ForeignKey** atau **ManyToManyField**, tergantung pada hubungan yang ingin kita buat. Jika setiap produk hanya dimiliki oleh satu pengguna (misalnya, pemilik produk), kita menggunakan **ForeignKey**, yang akan menambahkan kolom pada tabel `Product` untuk menyimpan referensi ke `User`. Sebaliknya, jika produk dapat dimiliki oleh banyak pengguna (seperti pembeli atau pelanggan) dan pengguna bisa memiliki banyak produk, kita menggunakan **ManyToManyField**, yang secara otomatis membuat tabel relasi terpisah untuk mengelola hubungan banyak-ke-banyak. Django memudahkan penghubungan antar model ini, sehingga kita bisa mengakses semua produk milik pengguna dengan query seperti ```user.product_set.all()``` atau mengambil pemilik dari produk tertentu dengan ```product.user```. 


**3. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?** <br/>

Django mengingat pengguna yang telah login melalui mekanisme **sessions** yang menggunakan **cookies**. Ketika pengguna login, Django menyimpan data sesi (termasuk informasi tentang pengguna yang telah diautentikasi) di server dan mengirimkan **cookie sesi** ke browser pengguna. Cookie ini berisi kunci unik (session ID) yang menghubungkan pengguna ke data sesi yang tersimpan di server. Setiap kali pengguna melakukan permintaan ke server, cookie ini dikirim kembali ke server untuk memastikan bahwa pengguna yang sama terus dikenali hingga mereka logout.

Selain untuk login, cookies digunakan untuk berbagai tujuan lain, seperti **melacak preferensi pengguna**, **mengelola keranjang belanja** dalam aplikasi e-commerce, dan **mengumpulkan data analitik** untuk mengetahui perilaku pengguna. Cookies juga bisa digunakan untuk **menyimpan pengaturan** yang dipersonalisasi, seperti tema atau bahasa yang dipilih pengguna.

Namun, tidak semua cookies aman digunakan. **Cookies yang tidak dienkripsi** dapat diambil dan dibaca oleh pihak ketiga (misalnya melalui serangan man-in-the-middle). Ada juga **cookies pihak ketiga**, yang sering digunakan untuk tujuan iklan atau pelacakan lintas situs, dan ini dapat menimbulkan kekhawatiran terkait privasi. Untuk memastikan keamanan, cookie harus diatur dengan opsi seperti **HttpOnly** (hanya bisa diakses oleh server, bukan JavaScript), **Secure** (hanya dikirimkan melalui koneksi HTTPS), dan **SameSite** (mencegah pengiriman cookie lintas situs yang tidak diinginkan).

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** <br/>

**1. Membuat Fungsi dan Form Registrasi**

- Pada ```views.py```, tambahkan import ```UserCreationForm``` dan ```messages```. ```UserCreationForm``` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna tanpa menulis kode dari awal.
- Tambahkan fungsi register pada ```views.py```
  ```python
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
  ```

- Buat template ```register.html``` untuk menampilkan form
- Kemudian, jangan lupa untuk menambahkan di ```urls.py```
  ```python
   urlpatterns = [
     ...
     path('register/', register, name='register'),]
   ```

**2. Membuat Fungsi dan Form Login**

- Buka kembali ```views.py``` yang ada pada subdirektori main. Tambahkan import ```authenticate```, ```login```, dan ```AuthenticationForm``` pada bagian paling atas.
- Tambahkan fungsi ```login-user``` di```views.py```
  ```python
    def login_user(request):
       if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
    
          if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main:show_main')
    
       else:
          form = AuthenticationForm(request)
       context = {'form': form}
       return render(request, 'login.html', context)
    ```
- Buat template ```login.html``` untuk menampilkan form
- Kemudian, jangan lupa untuk menambahkan di ```urls.py```
  ```python
  urlpatterns = [
    ...
    path('login/', login_user, name='login'),]
  ```

**3. Membuat Fungsi logout**

- Buka kembali ```views.py``` yang ada pada subdirektori main. Tambahkan import ```logout``` ini pada bagian paling atas.
- Tambahkan fungsi di bawah ini ke dalam fungsi ```views.py```
  ```python
  def logout_user(request):
    logout(request)
    return redirect('main:login')
  ```
- Bukalah berkas ```main.html``` yang ada pada direktori ```main/templates``` dan tambahkan potongan kode
  ```python
    ...
  <a href="{% url 'main:logout' %}">
    <button>Logout</button>
  </a>
    ...
  ```

- Kemudian, jangan lupa untuk menambahkan di ```urls.py```
  ```python
  urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),]
  ```

**4. Merestriksi Akses Halaman Main**

- import ```login_required``` pada bagian paling atas file ```views.py```
- tambahkan decorator ```@login_required(login_url='/login')``` di atas fungsi ```show_main```
  
  ```python
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
  ```

**5. Menambahkan data last login dan menampilkannya ke halaman main (mengimplementasikan fungsi cookies)**

- Membuka file ```views.py``` dan menambahkan import sesuai kode di bawah.
  ```python
  import datetime
  from django.http import HttpResponseRedirect
  from django.urls import reverse
  ```
- Pada fungsi ```login_user```, kita akan menambahkan fungsionalitas menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login.
  ```python
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
  ```
- Pada fungsi ```show_main```, tambahkan potongan kode ```'last_login': request.COOKIES['last_login']``` ke dalam variabel ```context```
- Ubah fungsi ```logout_user`` dengan potongan kode berikut.
  ```python
    def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
  ```
- Tambahkan ```last_login`` pada ```main.html```

**6. Menghubungkan Model dengan User**

- Pada ```models.py```, import ```User``` dari ```django.contrib.auth.models```
- Kemudian, tambahkan potongan kode ini dalam kelas model
  ```python
     user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
  ```
- Buka kembali ```views.py```, kemudian tambahkan kode ini. Perbedaan takhor dengan tutorial adalah kita juga menambahkan request.FILES untuk menambahkan image.
  ```python
    def create_product_entry(request):
      if request.method == "POST":
          form = ProductForm(request.POST, request.FILES)
          if form.is_valid():
              product_entry = form.save(commit=False)
              product_entry.user = request.user
              product_entry.save()
              return redirect('main:show_main')
      else:
          form = ProductForm()
  ```
- Ubah value dari ```name``` pada context dalam ```show_main``` menjadi ``` 'name': request.user.username,```
  








