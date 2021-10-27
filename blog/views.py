from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class PostList(ListView) :
    model = Post
    ordering = '-pk'
    #template_name = 'blog/post_list.html' 클래스에 templeate이름 인식없이 자동
    #post_list.html

class PostDetail(DetailView):
    model = Post
    #post_detail.html

#def index(request):
#    posts = Post.objects.all().order_by('-pk') 모델명. obects.all()로 가져와 posts에 담는다.-pk로 역순
#
#    return render(request,'blog/post_list.html',
#                  {
#                      'posts': posts -FBA일 때 이거 없음
#                  }
#                 )
#
#def single_post_page(request,pk) :
#    post = Post.objects.get(pk=pk) # =를 중심으로 왼쪽은 필드에 있는 것
#
#    return render(request, 'blog/post_detail.html',
#                  {
#                      'post': post
#                  }
#                  )
