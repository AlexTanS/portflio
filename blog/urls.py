from django.urls import path, include

from .views import blog, profile, BlogLoginView, BlogLogoutView

app_name = "blog"

urlpatterns = [
    path("accounts/logout/", BlogLogoutView.as_view(), name="logout"),  # log out of account
    path("accounts/profile/", profile, name="profile"),  # page 'my_story'
    path("accounts/login/", BlogLoginView.as_view(), name="login"),  # page 'login'
    path("", blog, name="blog"),  # home page 'blog'
]
