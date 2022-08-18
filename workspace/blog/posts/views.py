from django.shortcuts import render
from django.http import HttpResponse

def listar_posts(request):
    # return HttpResponse("Olá Mundo")
    return render(request, 'posts/listar_posts.html')
