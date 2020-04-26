from django.shortcuts import render
from list_item.models import Listitem
from main.models import ListModel


# Create your views here.
def list_item_view(request, pk):
    """view для элементов списка"""

    lists = Listitem.objects.filter(list=pk,
                                    ).order_by('created')
    name = ListModel.objects.filter(id=pk).first()
    context = {'lists': lists,
               'user': request.user.username,
               'list': name
               }
    return render(request, 'list.html', context)


def list_item_edit(request, pk):
    pass


def list_item_delete(request, pk):
    pass
