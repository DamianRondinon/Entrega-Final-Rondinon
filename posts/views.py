from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def about(request):
    return render(request, 'about.html')

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)

def post(request, pk):
    postObj = Post.objects.get(id=pk)
    return render(request, 'posts/single-post.html', {'post': postObj})


def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
    context = {'form': form}
    return render(request, "posts/post_form.html", context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)  
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
    context = {'form': form}
    return render(request, "posts/post_form.html", context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts') 
    context = {'object': post}
    return render(request, 'posts/delete_template.html', context)