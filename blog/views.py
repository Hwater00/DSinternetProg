from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request,'blog/index.html',
                  {
                      'posts': posts
                  }
                  )

def single_post_page(request,pk) :
    post = Post.objects.get(pk=pk) # =를 중심으로 왼쪽은 필드에 있는 것

    return render(request, 'blog/single_post_page.html',
                  {
                      'post': post
                  }
                  )