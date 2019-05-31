from django.shortcuts import render, HttpResponse
from .models import Book, Author

# Create your views here.

def home(request):
    book_obj=Book.objects.create(name='hlm',publish_date='1998-09-21')
    bendan=Author.objects.get(name='bendan')
    book_obj.author.add(bendan)
    return HttpResponse('This is home page')

