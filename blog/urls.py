from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name="detail"), #장고가 알아서 게시물에 id를 부여해줌
    path('new/', blog.views.new, name='new'),
    path('create', blog.views.create, name="create"), #path('어떤 url이 들어오면', (어디에있는)어떤 함수를 실행시켜라)
    path('edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('delete/<int:blog_id>', blog.views.delete, name="delete"),

    path('comment_add/<int:blog_id>', blog.views.comment_add, name='comment_add'),
    path('comment_edit/<int:comment_id>', blog.views.comment_edit, name='comment_edit'),
    path('comment_delete/<int:comment_id>', blog.views.comment_delete, name='comment_delete'),
]