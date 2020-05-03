from django.shortcuts import render
from list_item.models import Listitem
from main.models import ListModel
from list_item.forms import ListitemForm
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def list_item_view(request, pk):
    """view для элементов списка"""
    user = request.user
    lists = Listitem.objects.filter(list=pk
                                    ).order_by('created')
    list_name = ListModel.objects.filter(id=pk).first()

    context = {'lists': lists,
               'user': user.username,
               'list_name': list_name
               }

    return render(request, 'list.html', context)


def list_item_edit(request, pk):
    pass


def list_item_delete(request, pk):
    pass


def create_item_view(request, pk):
    form = ListitemForm()
    if request.method == 'POST':
        name = request.POST['name']
        expire_date = request.POST['expire_date']

        form = ListitemForm({
            'name': name,
            'expire_date': expire_date,
            'list': pk
        })
        success_url = reverse('list_item:list_item',kwargs={'pk': pk})
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, 'new_list_item.html', {'form': form})
