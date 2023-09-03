from item import views
from django.urls import path

app_name = 'item'

urlpatterns = [
    path('', views.search_item, name='search_item'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]