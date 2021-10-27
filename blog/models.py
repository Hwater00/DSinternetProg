from django.db import models
import os
# Create your models here.
""" Post라는 테이블의 title이라는 필드와 content라는 포스트로
타이틀을 텍스트 필드로  제작
시간 맟추기로 created_at =models.DateTimeField() settingf에서 INSTALLED_APPS
python manage.py makemigrations
python manage.py migrat해서 Post 모델을 데이터베이스를 반영
"""
class Post (models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100,  blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    #author
    ''' 포스트의 값과 포스트 타이틀을 한글로 def __str__(self)'''
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]