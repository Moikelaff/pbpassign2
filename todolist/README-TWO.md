[deployment link](https://pbpapp-dylan.herokuapp.com/todolist/)

# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    - async berupa multi-threaded berarti busa me run berbagai programs secara parallel jadi lebih cepat, sync hanya bisa 1 per satu jadi lebih lambat tetapi lebih mudah di code 
    - async bisa mengirim banyak requests, sync hanya bisa 1 per satu hingga requestnya di handle
    - async jauh lebih complex dan memudahkan code untuk meng-encounter bugs

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    event driving programming adalah suatu paradigma yang membuat flow dari program berjalan berdasarkan event yang direquest oleh client, contohnya adalah ketika diinput mouse event seperti click, geser, dll. setiap event tersebut akan dihandle oleh sebuah matching function yang akan jalankan sesuai dengan event tersebut
    

# Jelaskan penerapan asynchronous programming pada AJAX.
    pada ajax, ketika ada perubahan data kita tidak harus mereload website. ajax akan mengcontain requests yang akan di-run lalu dikirim ke server untuk diubah menjadi async. lalu ada juga ajax get dan post yang akan ke-trigger jika html mengirim method get & post, data yang didapat akan di send ke server tanpa harus browser reload

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. membuat show_ajax pada views.py
    2. routing url
    3. menghapus for loop code pada html
    4. import jquery
    5. membuat document.ready function untuk initial interface
    6. add script and css mereference: darihttps://hartdev-ctzyoepto-hudadamar21.vercel.app/source-code/tailwindcss-components/modal-with-animation/
    7. add ajax scripting buat get dan post
    8. membuat add_ajax di views untuk mengambil POST data dengan POST.get
    9.