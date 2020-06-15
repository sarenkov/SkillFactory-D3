from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from django.template import loader
from p_library.models import Book, Publisher, Author
from p_library.forms import AuthorForm, BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from django.forms import formset_factory
from django.http.response import HttpResponseRedirect


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    number_list = [x for x in range(1, 101)]
    biblio_data = {
        'title': 'Мою библиотеку',
        'books': books,
        'numbers': number_list
    }

    return HttpResponse(template.render(biblio_data, request))


def publishers(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    data = {
        'publishers': publishers,
        'books': books
    }
    return HttpResponse(template.render(data, request))


@csrf_protect
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']

        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('index/')
            else:
                book.copy_count += 1
                book.save()
            return redirect('/index/')
    else:
        return redirect('/index/')


@csrf_protect
def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('index/')
            else:
                book.copy_count -= 1
                book.save()
            return redirect('/index/')
    else:
        return redirect('/index/')


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    template_name = 'author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


@csrf_protect
def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


@csrf_protect
def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset,
        }
    )
