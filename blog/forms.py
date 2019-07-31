from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('title', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control-file','type':'file','id': 'exampleFormControlFile1', 'placeholder': 'Enter a title'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder':'in Dragon'})
        } #bootstarp 사용가능
        
        ''' #bootstarp이 안먹음
        def __init__(self, *args, **kwargs):
            super(BlogPost, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'form-control-file','type':'file','id': 'exampleFormControlFile1', 'placeholder': 'Enter a title'}),
            self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder':'in Dragon'})
            # type="file" class="form-control-file" id="exampleFormControlFile1"
            '''

class BlogEdit(forms.ModelForm):

    class Meta:
        model = Blog
        fields = {'title','body'}
