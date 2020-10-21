
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<int:id>", views.user_profile, name="user_profile"),
    path("follow", views.follow, name="follow"),
    path("following", views.following, name="following"),

    #javascript routes
    path("network/<int:post_id>", views.like_post, name="like_post"),
    path("network/edit/<int:post_id>", views.edit_post, name="edit_post")
]
