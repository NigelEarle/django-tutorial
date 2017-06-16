from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
  form = PostForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)
    print form.cleaned_data.get("title")
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())

  # if request.method == "POST":
  #   print request.POST.get("title")
  #   print request.POST.get("content")


  context = {
    "form" : form,
  }
  return render(request, "post_form.html", context);
  # return HttpResponse("<h1>Create</h1>")

def post_detail(request, id=None):
  instance = get_object_or_404(Post, id=id)
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

def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=instance)

  if form.is_valid():
    instance = form.save(commit=False)
    print form.cleaned_data.get("title")
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
    
  context = {
    "instance": instance,
    "form": form,
    "title" : "Detail"
  }
  return render(request, "post_form.html", context)
  # return HttpResponse("<h1>Update</h1>")

def post_delete(request):
  return HttpResponse("<h1>Delete</h1>")

