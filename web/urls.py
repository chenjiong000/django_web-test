from django.urls import path

from . import views

# app_name = 'polls' 存在多个应用时设置命名空间，引用路径变为app_name:name

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:movie_id>/',views.detail ,name='detail'),
    path('signup/',views.signUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('recommend/',views.recommend,name='recommend'),

    path('<int:id_com>/', views.detail_com, name='detail'),
    path('down/', views.downpage, name='down'),
    path('com/', views.index_com, name='com'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]