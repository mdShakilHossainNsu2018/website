from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'auth'

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),

    path('login/', LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

]