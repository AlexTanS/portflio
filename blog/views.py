from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

