from django.shortcuts import render
from .models import Post,Author,Books
# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html',{"posts":posts})
def login(request):
    if request.method == 'GET':
        return render(request,'blog/login.html')
    else:
        pass

def post_list(request):
    posts = Post.objects.filter(author__id =2)
    return render(request, 'blog/post_list.html',{"posts":posts})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html',{"authors":authors})

def books_list(request):
    books = Books.objects.all()
    return render(request,'blog/books_list.html',{"books":books})