from django.urls import path

from . import views

urlpatterns = [
    # it is important to use name=, it is used in forms action tag
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view,name='signup'),
    path('me/profile', views.update_profile, name='update_profile'),
]