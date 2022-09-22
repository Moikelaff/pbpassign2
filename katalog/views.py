from django.shortcuts import render
from katalog.models import CatalogItem


# ini katalog
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_katalog,
        'nama' : 'dylan adiprawira',
        'student_id' : '2106750446'
    }

    return render(request, 'katalog.html', context)
