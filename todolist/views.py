from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_todo' : data_todolist,
        'username' : request.user.username,
    }  
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created')
            return redirect('todolist:login')
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'username atau password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('todo')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        return response
    return render(request, "create.html")

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    json_data = serializers.serialize('json', data_todolist)
    return HttpResponse(json_data, content_type='application/json')

@login_required(login_url='/todolist/login/')
def is_ajax(request):
    if request.is_ajax():
        data_todolist = Task.objects.filter(user=request.user)
        json_data = serializers.serialize('json', data_todolist)
        return JsonResponse(json_data, safe=False)
    return HttpResponse("Not Ajax")

@login_required(login_url='/todolist/login/')
def main_json(request):
    if request.is_ajax():
        return render(request,"ajax.html")

@login_required(login_url='/todolist/login/')
def add_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('todo')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

@csrf_exempt
def delete(request,pk):
    if request.method == 'DELETE':
        data = Task.objects.get(id=pk)
        data.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

def change(request,pk):
    data = Task.objects.get(id=pk)
    data.status = not(data.status)
    data.save()
    return redirect('todolist:show_todolist')