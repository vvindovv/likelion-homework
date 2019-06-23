from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog, Comment #모델 안에 있는 클래스를 읽어와라
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import BlogPost
from .forms import BlogEdit

# Create your views here.
def home(request):
    blogs = Blog.objects #우리가 admin에서 봤던 글 목록을 blogs라고 칭함
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3) #blog_list라는 object를 3개로 쪼갠다.py
    page = request.GET.get('page') #request된것은 page라고 칭함
    posts = paginator.get_page(page) #그 page가 뭔지 posts로 
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts}) #blogs라는 value값을 blogs라는 key값으로 사용하겠다.

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id) #pk는 자동적으로 작성됨
    return render(request, 'detail.html', {'detail': details}) #blogs의 목록을 가져오는데 못가져오면 404라는 에러를 보여줌

def new(request): #new.html띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    if request.method == "POST": #post가 들어온 경우 요청을 실행
        form = BlogPost(request.POST)
        if form.is_valid(): #form을 제대로 입력했는가?
            post = form.save(commit=False) #모델객체를 반환 그러나 저장 x
            post.pub_date = timezone.now()
            post.save()
            return redirect('home', pk=blog_id)
    else: #get이 들어온경우 빈페이지 보여줌
        form = BlogPost()
    return render(request, 'new.html', {'form': form})

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        form =  BlogEdit(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogEdit(instance = blog)
    return render(request, 'edit.html', {'form' : form})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')

@login_required
def comment_add(request, blog_id):
    if  request.method == "POST": #post로 접근했는지 확인
            post = Blog.objects.get(pk=blog_id)
            comment = Comment()
            comment.user = request.user
            comment.body = request.POST['body']
            comment.post = post
            comment.save()
            return redirect('/blog/' +str(blog_id))
    else:
        return HttpResponse('잘못된 접근입니다.')

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        if request.method == "POST":
            comment.body = request.POST['body']
            comment.save()
            return redirect('/blog/' + str(comment.post.id))
        elif request.method == "GET":
            context = {
                'comment' : comment
            }
    return render(request, 'comment_edit.html', context)

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        if request.method == "POST":
            post_id = comment.post.id
            comment.delete()
            return redirect('/blog/' + str(post_id))
    return HttpResponse('잘못된 접근입니다.') #잘못된경우 사용해서 보내줘야함


def blogpost(request):
    if request.method == "POST": #post가 들어온 경우 요청을 실행
        form = BlogPost(request.POST)
        if form.is_valid(): #form을 제대로 입력했는가?
            post = form.save(commit=False) #모델객체를 반환 그러나 저장 x
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else: #get이 들어온경우 빈페이지 보여줌
        form = BlogPost()
    return render(request, 'new.html', {'form': form})

def blogedit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form =  BlogEdit(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogEdit(instance = blog)
    return render(request, 'edit.html', {'form' : form})

