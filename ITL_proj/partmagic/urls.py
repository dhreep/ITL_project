from django.urls import path
from . import views

urlpatterns = [
    path('', views.partmagic, name='partmagic'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_pub/', views.add_pub, name='add_pub'),
    path('delete_pub/<int:pub_id>/', views.delete_pub, name='delete_pub'),
    
]