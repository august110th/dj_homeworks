from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    list_books = Book.objects.all()
    context = {'books': list_books}
    return render(request, template, context=context)


def books_page(request):
    template = 'books/books_page.html'
    content = list(Book.objects.all())
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(content, 1)
    page = paginator.get_page(current_page)
    page_content = page.object_list

    context = {'page': page}

    return render(request, template, context=context)
