from django.urls import path

from . import views

app_name = 'expense'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:expense_id>/', views.detail, name='detail'),
]