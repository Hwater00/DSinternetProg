from django.shortcuts import render
from blog.models import Post
# Create your views here.



def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request,'single_pages/landing.html',
    {
        'recent_posts': recent_posts,
    })

def about_me(request):
    return render(request, 'single_pages/about_me.html')
# return render(request, '앱 이름과 동일하게/about_me.html이라는 내가 만든 템플릿')
