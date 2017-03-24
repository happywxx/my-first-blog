from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
import json

# Create your views here.

def post_mobile_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    response = []
    for post in posts:
        myDict = {
                    "ID":post.pk,
                    "Title":post.title,
                    "Date":timezone.localtime(post.published_date).strftime("%b. %d, %Y, %H:%M %p"),
                    "Content":post.text,
                  }
        response.append(myDict)

    response_dict = {}
    response_dict["Post"] = response

    return HttpResponse(json.dumps(response_dict), content_type="application/json")


def post_mobile_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        blog = json.loads(request.body.decode("utf-8"))
        if blog == "":
            return HttpResponse(json.dumps({'ResponseCode':0}), content_type="application/json")
        post.title = blog['Title']
        post.text =blog['Content']
        # post.published_date = timezone.now()
        post.save()

    return HttpResponse(json.dumps({'ResponseCode':1}), content_type="application/json")

def post_mobile_add(request):
    post = Post()
    if request.method == "POST":
        blog = json.loads(request.body.decode("utf-8"))
        if blog == "":
            return HttpResponse(json.dumps({'ResponseCode':0}), content_type="application/json")
        post.title = blog['Title']
        post.text = blog['Content']
        post.published_date = timezone.now()
        post.author = User.objects.get(username='wxx')
        post.save()
    # else:
    #     if not request.POST:
    #         return HttpResponse(json.dumps({'ResponseCode':0}), content_type="application/json")
    #     post.title = request.POST['Title']
    #     post.text = request.POST['Content']
    #     post.published_date = timezone.now()
    #     post.author = User.objects.get(username='wxx')
    #     post.save()


    return HttpResponse(json.dumps({'ResponseCode':1}), content_type="application/json")




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def mourn(request):
    return render(request, 'blog/mourn.html', {})

def encourage(request):
    return render(request, 'blog/index.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



