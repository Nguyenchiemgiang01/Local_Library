from django.shortcuts import render

# Create your views here.
from .models import Book,Author,BookInstance,Genre

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.all().count()
    num_genres=Genre.objects.all().count()

    def find_book_by_keyword(keyword):
        books=Book.objects.filter(title__icontains=keyword)
        if books.exists():
            book=books.first()
            return book.title
        else:
            return None
    
    book_contain_keyword=find_book_by_keyword('haha')

    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_genres':num_genres,
        'book_contain_keyword':book_contain_keyword,
    }

    return render(request,'index.html',context=context)
