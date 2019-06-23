from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', accounts.views.signup, name='signup'),
    path('accounts/', accounts.views.login, name='login'),
    path('accounts/', accounts.views.logout, name='logout'),
]