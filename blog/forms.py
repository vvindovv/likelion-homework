from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('title', 'body')

class BlogEdit(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body')
