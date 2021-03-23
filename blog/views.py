from django.shortcuts import render,HttpResponseRedirect
from .models import Post,Author,Books
from.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html',{"posts":posts})
def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        
    else:
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else: 
                    messages.error(request, 'Ваш аккаунт заблокирован')
            else:
                messages.error(request, 'неправильный ввод данных')

    return render(request,'blog/login.html',{'login_form': form})

def post_list(request):
    posts = Post.objects.filter(author__id =2)
    return render(request, 'blog/post_list.html',{"posts":posts})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html',{"authors":authors})

def books_list(request):
    books = Books.objects.all()
    return render(request,'blog/books_list.html',{"books":books})