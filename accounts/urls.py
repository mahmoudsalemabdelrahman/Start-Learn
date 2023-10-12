from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('logout', views.logout_view, name='logout'),


]
