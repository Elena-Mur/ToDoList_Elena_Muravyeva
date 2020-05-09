from django.urls import path
from list_item.views import list_item_view, list_item_delete, list_item_edit, create_item_view,done_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_item_view, name='list_item'),
    path('edit/<int:pk>', list_item_edit, name='edit'),
    path('delete/<int:pk>', list_item_delete, name='delete'),
    path('create/<int:pk>', create_item_view, name='create'),
    path('done/', done_view, name='done')

]
