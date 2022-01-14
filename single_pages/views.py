from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from shopping.models import Post
# Create your views here.
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'recent_posts':recent_posts,})

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )
class informaction( LoginRequiredMixin, UserPassesTestMixin):

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticatedand(current_user.is_staff or current_user.is_superuser):
            #form.instance.author = current_user
            return super(informaction, self).form_valid(form)
            #super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/shopping/')

def my_information(request):
    return render(
        request,
        'single_pages/my_information.html',
    )

