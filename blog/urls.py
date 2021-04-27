from django.urls import path, include

from .views import blog, profile, BlogLoginView, BlogLogoutView, RegisterUserView, RegisterDoneView
from .views import add_story


app_name = "blog"

urlpatterns = [
    path("accounts/register/done/", RegisterDoneView.as_view(), name="register_done"),
    path("accounts/register/", RegisterUserView.as_view(), name="register"),
    path("accounts/logout/", BlogLogoutView.as_view(), name="logout"),  # log out of account
    path("accounts/profile/", profile, name="profile"),  # page 'my_story'
    path("accounts/login/", BlogLoginView.as_view(), name="login"),  # page 'login'
    path("add_story/", add_story, name="add_story"),  # page 'add_story'
    path("", blog, name="blog"),  # home page 'blog'
]
