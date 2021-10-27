from django.contrib import admin
from .models import Post
# Register your models here.
''' 블로그에 필요한 모델을 등록한다. admin 클래스에서 제공하는 site에 register하겠다. 
()안에는 내가 생성한 모델
모델 연결을 위해서 from .models import 생성한 모델 이름'''
admin.site.register(Post)