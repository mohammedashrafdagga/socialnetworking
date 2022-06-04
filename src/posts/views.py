from django.shortcuts import render
from pydantic import Json
from .models import Post
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.


def home_page(request):
    qs = Post.objects.all()
    context = {'qs': qs}
    return render(request, 'posts/home.html', context)


def post_view_json(request):
    qs = Post.objects.all()
    data = serialize('json', qs)
    return JsonResponse({'data': data})
