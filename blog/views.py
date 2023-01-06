from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
#vista blog
def Blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {'posts':posts})

#vista categorias
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "categories.html", {'category': category})


