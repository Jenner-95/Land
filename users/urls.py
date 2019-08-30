from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_user_form, name='register'),
    path('login/', views.login_user_form, name='login'),
]