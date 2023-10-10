from django.urls import path


from . import views

app_name='blog'
urlpatterns = [
    path('',views.home, name='blog_home'),
    path('about/',views.about, name='about'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail, name='post_detail'),
    path('post/<post_id>/comment', views.post_comment,name='post_comment')

]
          