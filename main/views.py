from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    """главная view"""
    user = request.user
    lists = ListModel.objects.filter(
        user=user
    ).order_by('created')

    context = {'lists': lists,
               'user': request.user.username}
    return render(request, 'index.html', context)


def edit_view(request, pk):
    pass


def delete_view(request, pk):
    pass


def new_list_view(request):
    """view создания нового списка"""

    return render(request, 'new_list.html')
