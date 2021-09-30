from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Story
from .forms import StoryForm
from .utilites import thousand_characters


#  blog home page - all stories with the paginator
# [rus] главная страница блога - показываются все рассказы с пагинатором
def blog(request):
    # users = User.objects.all()  # get users
    strs = Story.objects.get_queryset().order_by("-id")  # get stories
    paginator = Paginator(strs, 4)  # create paginator

    # Determining the page number for the paginator
    # [rus] Определение номера страницы для пагинатора
    if "page" in request.GET:
        page_number = request.GET["page"]
    else:
        page_number = 1

    page = paginator.get_page(page_number)  # get obj Page
    context = {"page": page, "stories": page.object_list}
    return render(request, 'blog.html', context)


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
def add_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)  # the form accepts post and files requests
        if form.is_valid():
            s = form.save(commit=False)  # saving a form
            s.stories = request.user # adding the "stories" field to the form
            s.text_small = s.text_file.read().decode("utf-8")[:200] + "..."  # adding the "text_small" field to the form
            # s.save()  # saving a record to a database
            return redirect("blog:story_done")  # status=302
        else:
            form = StoryForm(request.POST, request.FILES)  # empty form
    else:
        form = StoryForm()  # empty form
    context = {"form": form}
    return render(request, "story_add.html", context)

# displays a message about the successful addition of the story
# [rus] выводит сообщение об успешном добавлении рассказа
def story_done(request):
    return render(request, "story_done.html")

# Story Page
# [rus] Страница рассказа
def page_story(request, id_story):
    story = Story.objects.get(id=id_story)
    text = story.text_file.read().decode("utf-8")
    context = {"story": story, "text": text}
    return render(request, "page_story.html", context)
