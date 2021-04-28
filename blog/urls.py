from django.urls import path, include

from .views import blog, profile, BlogLoginView, BlogLogoutView, RegisterUserView, RegisterDoneView
from .views import add_story, page_story, story_done


app_name = "blog"

urlpatterns = [
    path("accounts/register/done/", RegisterDoneView.as_view(), name="register_done"),
    path("accounts/register/", RegisterUserView.as_view(), name="register"),
    path("accounts/logout/", BlogLogoutView.as_view(), name="logout"),  # log out of account
    path("accounts/profile/", profile, name="profile"),
    path("accounts/login/", BlogLoginView.as_view(), name="login"),  # page 'login'
    path("add_story/", add_story, name="add_story"),  # page 'add_story'
    path("page_story/<id_story>", page_story, name="page_story"),  # page "page_story"
    path("story_done", story_done, name="story_done"),  # page "story_done"
    path("", blog, name="blog"),  # home page 'blog'
]
