from list_item.models import Listitem
from main.models import ListModel
from list_item.forms import ListitemForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import json

PAGE_COUNT = 6


@login_required(login_url='/registration/login/')
# Create your views here.
def list_item_view(request, pk):
    """view для элементов списка"""

    user = request.user
    list_name = get_object_or_404(ListModel, id=pk, user_id=request.user.id)
    list_items = Listitem.objects.filter(list=pk, list__user=user
                                         ).order_by('-created').order_by('-modified')

    paginator = Paginator(list_items, PAGE_COUNT)
    list_item_page = request.GET.get('list_item_page')

    try:
        list_item_page = paginator.page(list_item_page)
    except PageNotAnInteger:
        list_item_page = paginator.page(1)
    except EmptyPage:
        list_item_page = paginator.page(paginator.num_pages)

    context = {'list_items': list_item_page,
               'user': user.username,
               'list_name': list_name,
               'list_pages': list(paginator.page_range),
               'pk': pk

               }

    return render(request, 'list.html', context)


@login_required(login_url='/registration/login/')
def list_item_edit(request, pk):
    list_item = Listitem.objects.filter(id=pk).first()

    list_id = list_item.list_id

    if request.method == "POST":
        form = ListitemForm({
            'name': request.POST['name'],
            'expire_date': request.POST['expire_date'],
            'list': list_id
        }, instance=list_item)
        success_url = reverse('list_item:list_item', kwargs={'pk': list_id})
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = ListitemForm(instance=list_item)
    return render(request, "edit_list_item.html", {'form': form, 'pk': list_id})


@login_required(login_url='/registration/login/')
def list_item_delete(request, pk):
    if request.method == 'POST':
        list_item = Listitem.objects.filter(id=pk).first()
        if list_item:
            list_item.delete()
            return HttpResponse(status=201)
    return HttpResponse(status=404)


@login_required(login_url='/registration/login/')
def all_done_view(request):
    pass


@login_required(login_url='/registration/login/')
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


@login_required(login_url='/registration/login/')
def done_view(request):
    data = json.loads(request.body.decode())
    pk = int(data['id'])
    list_item = Listitem.objects.get(id=pk)
    value = not list_item.is_done
    list_item.is_done = value
    list_item.save()
    return HttpResponse(status=201)
