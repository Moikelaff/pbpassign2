from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
data_mywatchlist = MywatchlistItem.objects.all()
def show_mywatchlist(request):
    watched = 0
    not_watched = 0
    result = ""
    for i in data_mywatchlist:
        if i.watched == "watched":
            watched +=1
        else:
            not_watched +=1
            
    if watched > not_watched:
        result = "Selamat, kamu sudah banyak menonton!"
    elif watched == not_watched:
        result = "wah, kamu masih sedikit menonton!"
    else:
        result = "jumlah film yang kamu nonton sama dengan film yang kamu tidak tonton"

    context = {
        'list_watchlist' : data_mywatchlist,
        'nama' : 'dylan adiprawira',
        'student_id' : '2106750446',
        'result' : result,
        'watched' : watched,
        'not_watched' : not_watched,
    }
    return render(request, "main.html", context)

def show_html(request):
    context = {
        'list_watchlist' : data_mywatchlist,
        'nama' : 'dylan adiprawira',
        'student_id' : '2106750446',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")