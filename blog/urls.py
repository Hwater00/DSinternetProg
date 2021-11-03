from django.urls import path #url 불러오기
from . import views

urlpatterns = [#서버 IP/blog/

    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>',views.tag_page),
    path('category/<str:slug>',views.category_page),
    path('<int:pk>', views.PostDetail.as_view()),
    path('',views.PostList.as_view())
]

