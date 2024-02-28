from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.


class Question(models.Model):
    CHOICES = {
        ('나눔중', '나눔중'),
        ('예약중','예약중'),
        ('완료','완료')
    }
    REGION_CHOICES = {
        ('서울','서울'),
        ('경기','경기'),
        ('인천', '인천'),
        ('대전','대전'),
        ('광주', '광주'),
        ('울산','울산'),
        ('부산','부산'),
        ('대구','대구'),
        ('세종','세종'),
        ('제주','제주'),
        ('강원', '강원'),
        ('전남','전남'),
        ('전북','전북'),
        ('충남','충남'),
        ('충북','충북'),
        ('경북', '경북'),
        ('경남','경남'),
    }

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question', null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    imgfile = models.ImageField(upload_to="", default='static/img/profileimg.jpeg')

    region = models.CharField(max_length=40, choices=REGION_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=100, choices=CHOICES, null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)