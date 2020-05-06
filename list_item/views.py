from list_item.models import Listitem
from main.models import ListModel
from list_item.forms import ListitemForm
from main.forms import ListForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.http import HttpResponseRedirect

PAGE_COUNT = 6


# Create your views here.
def list_item_view(request, pk):
    """view для элементов списка"""

    user = request.user
    list_name = get_object_or_404(ListModel, id=pk, user_id=request.user.id)
    lists = Listitem.objects.filter(list=pk
                                    ).order_by('-created')

    paginator = Paginator(lists, PAGE_COUNT)
    list_item_page = request.GET.get('list_item_page')

    try:
        list_item_page = paginator.page(list_item_page)
    except PageNotAnInteger:
        list_item_page = paginator.page(1)
    except EmptyPage:
        list_item_page = paginator.page(paginator.num_pages)

    context = {'lists': list_item_page,
               'user': user.username,
               'list_name': list_name,
               'list_pages': list(paginator.page_range),
               'pk': pk

               }

    return render(request, 'list.html', context)


def list_item_edit(request, pk):
    # obj = Listitem.objects.filter(id=pk).first()
    # form = ListitemForm(instance=obj)
    # if request.method == "POST":
    #     obj.name = request.POST.get("name")
    #     obj.expire_date = request.POST.get("expire_date")
    #     form = ListitemForm({
    #         'name': obj.name,
    #         'expire_date': obj.expire_date
    #     }, instance=obj)
    #     success_url = reverse('list_item:list_item', kwargs={'pk': pk})
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(success_url)
    # else:
    #     return render(request, "edit_list_item.html", {'form': form, 'obj': obj})
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
        success_url = reverse('list_item:list_item', kwargs={'pk': pk})
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, 'new_list_item.html', {'form': form, 'pk': pk})
