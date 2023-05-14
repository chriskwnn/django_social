from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('like_post', views.like_post, name='like-post'),
    path('logout', views.logout, name='logout'),
    path('setting', views.setting, name='setting'),
    path('upload', views.upload, name='upload'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search')
]