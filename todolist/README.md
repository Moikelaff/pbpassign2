# 1. apa kegunaan {% csrf token %} pada elemen <code>form</code>? apa yang terjadi apabila tidak ada potongan <code>form</code>?
    csrf token adalah token random yang unique untuk semua user session yang secure yang digunakan untuk nge-prevent csrf attack
    
    jika tidak ada csrf token maka user dapat mengakses link2 yang sensitive yang restricted bagi umum
---
# 2. apakah kita dapat membuat elemen <code>form</code> secara manual(tanpa menggunakan generator seperti <code>{{ form.as_table }}</code>)? jelaskan secara gambaran besar bagaimana cara membuat <code>form</code> secara manual.
    bisa, caranya dengan membuat form list sendiri menggunakan table/tr/td/input lalu make csrf token untuk ngegive authorization

# 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
    setelah subimisi, data yang diinput oleh user bisa diakses dengan html method yang dipake. setelah itu data dimasukkan ke database oleh <code>Task.objects.create()</code>, setelah ada di database data di di akses oleh html di <code>{% for todo in list_todolist %} </code> yang nantinya di show ke client.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. startapp
    2. add url and apps di project_django
    3. membuat class Task
    4. membuat method register/login/create_task dan membuat htmlnya masing2 di templates.
    5. membuat routing di urls.py

    