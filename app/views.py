# coding=utf-8
from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def post_list(request):
    m = Post.objects.all()
    m = reversed(m)
    return render(request, 'app/post_list.html', {'mensajes':m})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(author=form.cleaned_data['author'],
                        title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        created_date=timezone.now(),
                        published_date=timezone.now())
            post.save()
            return redirect('post_list')
    else:
        form = PostForm
    return render(request, 'app/crear_post.html', {'form':form})


def login(request):
    # Creamos el formulario de autenticacion vacio
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Veo si el formulario es valido
        if form.is_valid():
            # Recupero las credenciales ingresadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verifico esas credenciales
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña...
            if user is not None:
                do_login(request, user)
                return redirect('post_list')
    # Si llegamos al final renderizamos el formulario
    return render(request, "app/login.html",{'form': form})