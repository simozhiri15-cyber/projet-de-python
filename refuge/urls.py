from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/nouveau/', views.animal_create, name='animal_create'),
    path('animal/<int:pk>/modifier/', views.animal_update, name='animal_update'),
    path('login/', auth_views.LoginView.as_view(template_name='refuge/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
