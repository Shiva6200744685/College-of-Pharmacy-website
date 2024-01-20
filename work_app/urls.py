from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('course/', views.course_view, name='course'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
