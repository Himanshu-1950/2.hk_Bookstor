# books/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, BookListView, BookCreateView, home
from .views import custom_logout

urlpatterns = [
    # Home (redirects to book list)
    path('', home, name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='books/login.html'
    ), name='login'),
    path('logout/', custom_logout, name='logout'), 

    # Registration
    path('register/', RegisterView.as_view(), name='register'),

    # Book views
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='book_create'),
]
