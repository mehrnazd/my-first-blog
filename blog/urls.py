from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
<<<<<<< HEAD
    path('post/<int:pk>/',views.post_detail,name='post_detail')
=======
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
>>>>>>> 606aa0bcd8e734b91ddba640e91f45ef7e99ed44
]