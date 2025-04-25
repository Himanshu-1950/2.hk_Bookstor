from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),   # ✅ Login route
    path(
   'logout/',
  auth_views.LogoutView.as_view(template_name='books/logout.html'),
  name='logout'
),

]
