# 1. apa kegunaan {% csrf token %} pada elemen <code>form</code>? apa yang terjadi apabila tidak ada potongan <code>form</code>?
    csrf token adalah token random yang unique untuk semua user session yang secure yang digunakan untuk nge-prevent csrf attack
    
    jika tidak ada csrf token maka user dapat mengakses link2 yang sensitive yang restricted bagi umum
---
# 2. apakah kita dapat membuat elemen <code>form</code> secara manual(tanpa menggunakan generator seperti <code>{{ form.as_table }}</code>)? jelaskan secara gambaran besar bagaimana cara membuat <code>form</code> secara manual.
    bisa, caranya dengan membuat form list sendiri menggunakan table/tr/td/input lalu make csrf token untuk ngeverify aithenticated user
# 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
    setelah subimisi, data yang diinput oleh user bisa diakses dengan html method yang dipake. setelah itu data dimasukkan ke database oleh Task.objects.create().
    setelah ada di database data di di akses oleh html di{% for todo in list_todolist %} yang nantinya di show ke client.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. startapp
    2. add url and apps di project_django
    3. membuat class Task
    4. membuat method register/login/create_task dan membuat htmlnya masing2 di templates.
    5. membuat routing di urls.py

---
# TUGAS 5
---
# 1. Apa Perbedaan dari inline, internal, dan external CSS? apa saja pros n cons setiap style?
    inline: langsung add style pada tag html seperti <p style="..."></p>.
    pros(+): gampang dipakai karena langsung add di tag, bagus buat bikin style preview, ga harus ngebuat file .css baru.
    cons(-): time consuming karena harus add di setiap tag, bisa membuat file html berantakan, bisa ngeaffect page size dan download time. 

    internal: add style pada file html yang sama dengan menggunakan tag <style>.
    PROS(+): ga harus upload multiple file, bisa langsung diakses mempakai class dan id selectors.
    CONS(-): file html bisa panjang dan agak susah dibaca.
    
    external: membuat file .css baru yang nanti bisa diakses html.
    PROS(+): file html lebih rapih dan readable, bisa memakai file .css itu buat multiple html.
    CONS(-): ada buffer loading antara html yang raw dan yang udah ada cssnya, bisa menambah download time dari website.

# 2. Jelaskan tag HTML5 yang kamu ketahui  
    1. <HTML>: document
    2. <head>: header//prologue
    3. <body>: body dari html
    4. <title>: title document yang ada di tab atas
    4. <h1/2/3/4/5/6>: text heading
    5. <p>: paragraph
    6. <br>: line break
    7. <hr>: horizontal rule// ngebuat horizontal line
    8. <a href="">: ngemuat link
    9. <img src="">: ngeload image
    10. <table> | <tr> | <td> | <th>: start table | table row | table data | table header
    11. <b> | <i> | <u>: bold | italic | underline
    12. <li> | <ul> | <ol>: list items | unordered list (pake dot) | ordered list (pake nums)
    13. <input>: input
    14. <div>: define division (section)  
    15. <meta>: ngecontain metadata/ doc info
    16. dll
# 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui
    BY CLASS
    1. .class: select semua tags yang ada di dalam <class="...">
    2. .class1.class2: select tags yang ada di class1 dan class2 di attributenya
    3. .class1 .class2: select sub <class2=""> yang ada di main class <class1="">
    BY ID
    1. #id: select semua elemen yang idnya sama
    BY ELEMENT
    1. element: misal element p{} maka select semua tag <p>
    2. element.class: misal p.class1{} maka select semua tag <p> didalam class1
    3. element, element: misal div, p {} maka select semua tag <div> dan <p>
    4. element + element: misal div + p{} maka select <p> paling atas// yang paling deket dengan <div>
    5. dll,

# 4. jelaskan bagaimana cara kamu mengimplementasi checklist di atas
    dengan menggunakan css internal
    2. membuat <style> buat setiap html file dgn load static
    3. utak atik css 
    4. ngeadd documentary media query