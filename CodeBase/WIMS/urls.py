from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/donor/', views.donor_signup, name='donor_signup'),
    path('signup/member/', views.member_signup, name='member_signup'),
    path('members/dashboard/', views.member_dashboard, name='member_dashboard'),
    path('members/projects/<int:project_id>', views.project_page, name='project_page'),
]
