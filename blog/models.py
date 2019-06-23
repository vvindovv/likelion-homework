from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    # pk
    title = models.CharField(max_length = 200) #짧은글(title)
    pub_date = models.DateTimeField('date published') #날짜와 시간의 변수
    body = models.TextField() #긴글형식

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #100개를 기준으로 글자를 자른다 = (100개 까지만 보인다.)(class에서 지정한 body를)

class Comment(models.Model):
    #1
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="comments") #ondelete: 글이 사라지면 댓글도 지운다
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.CharField(max_length = 500)
