from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre, Language
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    num_genres = Genre.objects.all().count()

    num_languages = Language.objects.all().count()

    num_titles_with_the = Book.objects.filter(title__contains='the').count()

    context = {
        'num_books': num_books,
        'num_book_instances': num_book_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_languages': num_languages,
        'num_titles_with_the': num_titles_with_the,
    }
    
    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 15


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15


class AuthorDetailView(generic.DetailView):
    model = Author


