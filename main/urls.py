from django.urls import path
from main.views import main_view, edit_view, new_list_view, delete_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('new_list/', new_list_view, name='new_list')
]
