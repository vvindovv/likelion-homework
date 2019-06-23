from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog, Comment #모델 안에 있는 클래스를 읽어와라
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
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
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+str(blog.id))
    return render(request, 'edit.html', {'blog' : blog})    

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