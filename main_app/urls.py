from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name='items_index'),
    path('create/', views.ItemCreate.as_view(), name='items_create'),
    path('<int:item_id>/delete/', views.items_delete, name='items_delete'),
]