from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books, Genre
from .forms import BooksForm

class BooksList(ListView):
    model = Books
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    queryset = Books.objects.order_by('-id')

class BooksDetail(DetailView):
    model = Books
    template_name = 'books/books_detail.html'
    context_object_name = 'books_detail'

class BooksCreate(CreateView):
    template_name = 'books/books_create.html'
    form_class = BooksForm
    success_url = '/books/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BooksForm
        return context
    
class BooksUpdate(UpdateView):
    template_name = 'books/books_create.html'
    form_class = BooksForm
    success_url = '/books/'
    queryset = Books.objects.all()

class BooksDelete(DeleteView):
    template_name = 'books/books_delete.html'
    queryset = Books.objects.all()
    success_url = '/books/'
