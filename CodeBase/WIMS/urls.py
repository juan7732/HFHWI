from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/donor/', views.donor_signup, name='donor_signup'),
    path('signup/member/', views.member_signup, name='member_signup'),
    path('members/dashboard/all/', views.member_dashboard_all, name='member_dashboard_all'),
    path('members/dashboard/active/', views.member_dashboard_active, name='member_dashboard_active'),
    path('members/dashboard/proposed/', views.member_dashboard_proposed, name='member_dashboard_proposed'),
    path('members/dashboard/completed/', views.member_dashboard_completed, name='member_dashboard_completed'),
    path('members/dashboard/search/<str:searchString>/', views.member_dashboard_search, name='member_dashboard_search'),
    path('members/projects/<int:project_id>/', views.project_page, name='project_page'),
    path('donors/dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('donors/makedonation/', views.make_donation, name='make_donation'),
    path('donors/finalizedonation/', views.make_donation_two, name='finalize_donation'),
]
