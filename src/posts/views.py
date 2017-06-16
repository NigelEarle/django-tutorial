from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
  form = PostForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)
    print form.cleaned_data.get("title")
    instance.save()
    messages.success(request, "Successfully Created")
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    "form" : form,
  }
  return render(request, "post_form.html", context);

def post_detail(request, id=None):
  instance = get_object_or_404(Post, id=id)
  context = {
    "instance": instance,
    "title" : "Detail"
  }
  return render(request, "post_detail.html", context)

def post_list(request):
  queryset = Post.objects.all()

  context = {
    "object_list" : queryset,
    "title": "List"
  }
  return render(request, "post_list.html", context)

def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=instance)

  if form.is_valid():
    instance = form.save(commit=False)
    print form.cleaned_data.get("title")
    instance.save()
    messages.success(request, "Item Updated", extra_tags="some-tag")
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    "instance": instance,
    "form": form,
    "title" : "Detail"
  }
  return render(request, "post_form.html", context)
  # return HttpResponse("<h1>Update</h1>")

def post_delete(request, id=None):
  instance = get_object_or_404(Post, id=id)
  instance.delete()
  messages.success(request, "Successfully Deleted")
  return redirect("posts:list")


