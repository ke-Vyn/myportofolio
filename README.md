Nama : Kevin R

NPM : 2506621466

Kelas : PBP C

#Hi from another branch

# 7/9/2026
## A.Weekly Instruction Step :
1. Clone this repository
    git clone https://github.com/ke-Vyn/myportofolio.git
    cd myportofolio
2. Create a virtual environment and activate it
    python -m venv env
    env\Scripts\activate
3. Install Dependencies 
    pip install -r requirements.txt
4. Run server
    python manage.py runserver
5. Open `http://localhost:8000` in any browser

## B. Weekly Updates :
1. Added a new Highlights section containing 3 cards: Skill, Education, Projects 
2. Added a navigation button in the social links area that scrolls to the new section via anchor link (#highlights)
3. CSS styling:
    a. 3 column grid layout (display: grid), collapses into a single column on mobile / smaller screen
    b. Hover effect on each card (lift & shadow)
    c. Short fade-in entrance animation (@keyframes) when the page loads
4. Adjusted the Hero section to fill the full viewport height (min-height: 100vh) so that Highlights stays hidden until the user scrolls
5. Replaced all sample data with my own information

## C. Reflection :
### Assignment 1
1. Yes, i used semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<footer>`) to structure the page based on its content's purpose. I separated the "About Me" content into a `<section class="hero">` and the new content into `<section class="Highlights">`. I also used `<dl>`, `<dt>` and `<dd>` to display NPM and study program since they're a label value pair. This made the structure easier to read from the HTML, and should also make the page look more readable for readers.

2. The main challenge was deciding how elements should reflow when the grid changes from 2 column to 1 column (mobile). On laptop / desktop, the hero section places the photo beside the identity and details using 'grid-template-areas'. If it wasn't reordered, the photo could end up appearing last, even though it's one of more important elements. I addressed this by rearranging 'grid-template'areas' so the order becomes identity > photo > details when stacked vertically on mobile. I also set the photo's maximum width to 220px on mobile so that it wouldn't dominate smaller screen. For the highlights section, i changed the grid from 3 columns to 1 column below 700px, so each card would have enough horizontal space to read comfortably.

3. Static website forces me to write every content directly into the HTML and redeploy it whenever theres changes. This becomes limiting if i want to frequently add new contents. Not only that, it also limits the website's ability to process visitor input. For example, the current "Email" button only uses a mail:to link, which opens the visitor's email client instead of allowing the web to process the message directly. For the next iteration, i'd like to add a database so contents can easily managed through an admin panel without directly editing the index.html file.

## D. AI Disclosure : 
- Tool used: Gemini AI
- How it was used: Discussed suitable CSS styling approaches, such as: grid layout, hover effects and entrance animation, for the highlights section and hero layout, based on a web design i previously created in Figma without implementing JavaScript and relying solely on CSS3

---

# 14/9/2026 - Tugas 2
## A. Weekly Instruction Step :
1. Clone this repository
    git clone https://github.com/ke-Vyn/myportofolio.git
    cd myportofolio
2. Create a virtual environment and activate it
    python -m venv env
    env\Scripts\activate
3. Install Dependencies 
    pip install -r requirements.txt
4. Run server
    python manage.py runserver
5. Open `http://localhost:8000` in any browser

## B. Weekly Updates :
1. Menerapkan Model View Template (MVT) untuk dua section, yaitu Experience dan Projects, masing-masing dengan model, view, dan template Django-nya sendiri
2. Menambahkan routing untuk /experience/ dan /projects/ di main/urls.py dan menghubungkan navigasi antar halaman lewat navbar
3. Mengubah kartu "Projects" di section Highlights menjadi link dinamis menuju GitHub dan halaman Projects yang baru
4. Menambahkan unit test (memastikan URL dapat diakses, template yang digunakan benar dan data model tampil dengan baik)


## C. Reflection :
### Assignment 2
1. Ketika user membuka /projects/, request diterima oleh urls.py project, lalu diteruskan ke urls.py aplikasi main melalui include(). Di main/urls.py, path "projects/" dicocokkan dengan fungsi view show_projects, yang kemudian mengambil seluruh data dari model Project lewat Project.objects.all(), memasukkannya ke dalam context, lalu memanggil render() untuk menggabungkan data tersebut dengan template projects.html. Template mengubah data menjadi HTML, kemudian dikirim sebagai reponse dan ditampilkan di browser

2. Data disimpan di model agar data dan tampilan terpisah sehingga mengubah tampilan cukup dilakukan dengan mengedit template tanpa menyentuh data. Selain itu, mengubah data dapat dilakukan lewat database tanpa mengedit HTML secara manual. Hal ini membuat pengembangan aplikasi lebih mudah karena tidak memerlukan redeploy kode ulang setiap data berubah, data bisa divalidasi secara konsisten oleh Django (misalnya URLField), dan data tersebut dapat difilter / ditampilkan ulang di halaman lain tanpa perlu tulis ulang kode HTML

3. - makemigrations --> membuat file migration berdasarkan perubahan pada `models.py`, tetapi belum menerapkannya ke database.
   - migrate --> menerapkan migration tersebut ke database yang aktif.
     Contoh : Saat menambahkan model `Project` dengan field `title`, `description`, `tech_stack`, dan `project_url`, jalankan `makemigrations` untuk membuat migration, lalu `migrate` untuk membuat tabel `Project` di database.

## D. AI Disclosure : 
- Tool used: Claude.ai
- How it was used: Diskusi mengenai alur MVT untuk section Experience dan Projects, termasuk desain field model, struktur view/context, dan sintaks Django Template Language untuk loop dan empty state. Selain itu, Ai juga digunakan untuk debugging masalah saat deployment di PWS, seperti perbedaan database lokal dan production