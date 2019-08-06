from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
from django.utils import timezone
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
