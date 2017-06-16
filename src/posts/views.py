from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_create(request):
  return HttpResponse("<h1>Create</h1>")

def post_detail(request):
  instance = get_object_or_404(Post, id=3)
  context = {
    "instance": instance,
    "title" : "Detail"
  }
  return render(request, "post_detail.html", context)
  # return HttpResponse("<h1>Detail</h1>")

def post_list(request):
  queryset = Post.objects.all()
  # if request.user.is_authenticated(): => checks if users is authenticated
  #   context = {
  #     "title": "My User List"
  #   }
  # else:
  #   context = {
  #     "title": "List"
  #   }

  context = {
    "object_list" : queryset,
    "title": "List"
  }
  return render(request, "index.html", context)
  # return HttpResponse("<h1>List</h1>")

def post_update(request):
  return HttpResponse("<h1>Update</h1>")

def post_delete(request):
  return HttpResponse("<h1>Delete</h1>")

