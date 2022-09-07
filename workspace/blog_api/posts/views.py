from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from posts.models.category import Category
from posts.serializers.category_serializer import CategorySerializer

def listar_posts(request):
    # return HttpResponse("Olá Mundo")
    categorias = Category.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'posts/listar_posts.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'posts/listar_posts.html'
    context_object_name = 'categorias'


@api_view(['GET', 'POST'])
def api_listar_categorias(request):
    if request.method == 'GET':
        categorias = Category.objects.all()
        categoria_serializer = CategorySerializer(categorias, many=True)

        return Response(
            categoria_serializer.data,
            status=status.HTTP_200_OK
        )