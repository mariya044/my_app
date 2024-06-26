from django.contrib.auth.views import LogoutView
from django.urls import path, include
from user.views import SignUpView, LoginView
from . import views


urlpatterns = [
    path('', views.posts, name="posts"),
    # path('posts/<int:post_id>/', views.posts_view, name="post_list"),
    path("create/", views.create, name="create"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("<int:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
]
