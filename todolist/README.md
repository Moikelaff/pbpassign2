# 1. apa kegunaan {% csrf token %} pada elemen <code>form</code>? apa yang terjadi apabila tidak ada potongan <code>form</code>?
    csrf token adalah token random yang unique untuk semua user session yang secure yang digunakan untuk nge-prevent csrf attack
    
    jika tidak ada csrf token maka user dapat mengakses link2 yang sensitive yang restricted bagi umum
---
# 2. apakah kita dapat membuat elemen <code>form</code> secara manual(tanpa menggunaka generator seperti <code>{{ form.as_table }}</code>)? jelaskan secara gambaran besar bagaimana cara membuat <code>form</code> secara manual.
    bisa, caranya dengan membuat
    