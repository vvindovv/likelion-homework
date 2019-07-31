from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
]