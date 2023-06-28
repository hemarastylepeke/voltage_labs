from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # path to homepage
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'), # path to individual blog post page
    path('blogs/', views.blogs_page, name='blogs_list'),
    path('projects/', views.case_study_page, name='case_study'),
    path('success/', views.success_url, name='success_url'), # Success url page
    path('terms_and_conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
