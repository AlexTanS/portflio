from django.shortcuts import render

def visitka(request):
	context = {"quest": "Ответ 200"}
	return render(request, "visitka.html", context)