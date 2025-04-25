from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth import logout

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'books/register.html'  # Updated path
    success_url = reverse_lazy('login')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Updated path
    context_object_name = 'books'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'price', 'stock', 'description']
    template_name = 'books/book_form.html'  # Updated path
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user.is_staff

def home(request):
    return redirect('book_list')

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page