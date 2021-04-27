from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Story
from .forms import StoryForm


#  blog home page
# [rus] главная страница блога
def blog(request):
    return render(request, 'blog.html')


# the page controller 'login'
# [rus] контроллер страницы 'входа'
class BlogLoginView(LoginView):
    template_name = "login.html"


# the page controller 'exit'
# [rus] контроллер страницы 'выхода'
class BlogLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"


# profile for the user who logged in: shows his stories
# [rus] профиль для пользователя (выполневшего вход): показывает его рассказы
@login_required
def profile(request):
    return render(request, "profile.html")


# controller-class that registers the user
# [rus] контроллер-класс регистрирующий пользователя
class RegisterUserView(CreateView):
    model = User
    template_name = "register_user.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("blog:register_done")


# displays a message about successful registration
# [rus] выводит сообщение об удачной регистрации
class RegisterDoneView(TemplateView):
    template_name = "register_done.html"

# Adding a new story
# [rus] Добавление нового рассказа
# @login_required
def add_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)  # the form accepts post and files requests
        if form.is_valid():
            s = form.save(commit=False)  # saving a form
            s.stories = request.user # adding the "stories" field to the form
            s.save()  # saving a record to a database
            return redirect("blog:blog")
        else:
            form = StoryForm()  # empty form
    else:
        form = StoryForm()  # empty form
    return render(request, "story_add.html", {"form": form})


# def add_story(request):
#     if request.method == "POST":
#         form = StoryForm(request.POST, request.FILES)
#         if form.is_valid():
#             print("+++")
#             # form.save()
#         else:
#             print("НЕВАЛИДНО")
#             print(form.errors)
#             print(form.cleaned_data)
#     else:
#         form = StoryForm()
#     context = {"form": form}
#     return render(request, "story_add.html", context)
