from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post,Category


# Create your views here.
class PostList(ListView) :
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(PostList,self).get_context_data()
        context['categories']= Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    #template_name = 'blog/post_list.html'
    #post_list.html

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(PostDetail,self).get_context_data()
        context['categories']= Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    #post_detail.html
def category_page(request,slug):
    if slug =='no_category':
        category='미분류'
    else:
        category=Category.objects.get(slug=slug)
        post_list =Post.objects.filter(category=category)

    return render(request,'blog/post_list.html',
                  {
                      'post_list':post_list,
                      'categories': Category.objects.all(),
                      'no_category_post_count':Post.objects.filter(category=None).count(),
                      'category':category

                  }
                  )


#def index(request):
#    posts = Post.objects.all().order_by('-pk') 모델명. obects.all()로 가져와 posts에 담는다.-pk로 역순
#
#    return render(request,'blog/post_list.html',
#                  {
#                      'posts': posts
#                  }
#                 )
#
#def single_post_page(request,pk) :
#    post = Post.objects.get(pk=pk)
#    return render(request, 'blog/post_detail.html',
#                  {
#                      'post': post
#                  }
#                  )
