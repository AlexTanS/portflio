from django.shortcuts import render

# home page
# [rus] главная страница сайта
def index(request):
    return render(request, "main/index.html")
