from django.urls import path #url 불러오기
from . import views

urlpatterns = [#서버 IP/blog/

 #FBA로 URL에서 가져온 pk와 일치하는 post를 가져옴,
 # path('<int:pk>/', views.single_post_page), pk란 값이 들어있는 url이 오면 호출해하

 #FBA,  path('', views.index),
#서버 ip
    path('<int:pk>', views.PostDetail.as_view()),
    path('',views.PostList.as_view())
]

