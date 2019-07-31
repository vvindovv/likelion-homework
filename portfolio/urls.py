from django.contrib import admin
from django.urls import path, include
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', portfolio.views.portfolio, name="portfolio"),
]