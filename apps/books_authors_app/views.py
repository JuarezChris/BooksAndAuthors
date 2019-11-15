from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/index.html", context)

def process(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect("/")

def books(request, num):
    context = {
        "book": Book.objects.get(id=num)
    }
    return render(request,"books_authors_app/books.html", context)

def authors(request):
        context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def addAuthor(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes = request.POST["notes"])
    return redirect("/authors")