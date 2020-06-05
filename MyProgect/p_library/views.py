from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from django.template import loader
from p_library.models import Book, Publisher


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
    data = {
        'publishers': publishers
    }
    return HttpResponse(template.render(data, request))

@csrf_protect
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']

        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id = book_id).first()
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
            return  redirect('/index/')
        else:
            book = Book.objects.filter(id = book_id).first()
            if not book:
                return redirect('index/')
            else:
                book.copy_count -= 1
                book.save()
            return redirect('/index/')
    else:
        return redirect('/index/')
