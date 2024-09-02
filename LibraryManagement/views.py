
from django.http import HttpResponse  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Book, Author    
from django.urls import reverse_lazy
from .forms import BookForm, AuthorForm
from django.db.models import Q
from django.shortcuts import redirect
from django.views import View  


class BookListView(ListView):  
    model = Book  
    template_name = 'list.html'  
    context_object_name = 'books'  

    def get_queryset(self):  
        queryset = super().get_queryset()  
        search_query = self.request.GET.get('search')  
        min_price = self.request.GET.get('min_price')  
        max_price = self.request.GET.get('max_price')  
        pub_date = self.request.GET.get('pub_date')  

        if search_query:  
            queryset = queryset.filter(  
                Q(title__icontains=search_query) | Q(author__name__icontains=search_query)  
            )  

        if min_price:  
            queryset = queryset.filter(price__gte=min_price)  

        if max_price:  
            queryset = queryset.filter(price__lte=max_price)  

        if pub_date:  
            try:  
                queryset = queryset.filter(publication_date=pub_date)  
            except ValueError:  
                queryset = queryset.none()   
        return queryset  
    
    
class BookCreateView(CreateView):  
    model = Book  
    form_class = BookForm  
    template_name = 'add_book.html'  
    success_url = reverse_lazy('show_list')
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context['author_form'] = AuthorForm() 
        return context  

    def form_valid(self, form):  
        author_name = self.request.POST.get('new_author_name')  
        if author_name:  
            author, created = Author.objects.get_or_create(name=author_name)  
            form.instance.author = author  
        return super().form_valid(form)  

class DeleteSelectedBooksView(View):  
    def post(self, request):  
        selected_books = request.POST.getlist('selected_books')  
        Book.objects.filter(id__in=selected_books).delete()  
        return redirect('show_list')  

class BookEditView(UpdateView):  
    model = Book  
    form_class = BookForm  
    template_name = 'edit.html'  
    success_url = reverse_lazy('show_list')  

class BookDeleteView(DeleteView):  
    model = Book  
    template_name = 'delete.html'  
    success_url = reverse_lazy('show_list')  

