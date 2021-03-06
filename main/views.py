from django.shortcuts import render, reverse, redirect
from main.forms import ListModel, ListForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse

PAGE_COUNT = 6


@login_required(login_url='registration/login/')
def main_view(request):
    """главная view"""
    user = request.user
    lists = ListModel.objects.filter(
        user=user
    ).order_by('-created').order_by('-modified')

    paginator = Paginator(lists, PAGE_COUNT)
    page = request.GET.get('page')

    try:
        list_page = paginator.page(page)
    except PageNotAnInteger:
        list_page = paginator.page(1)
    except EmptyPage:
        list_page = paginator.page(paginator.num_pages)

    context = {'lists': list_page,
               'user': request.user.username,
               'pages': list(paginator.page_range)
               }
    return render(request, 'index.html', context)


@login_required(login_url='registration/login/')
def edit_view(request, pk):
    list_ = ListModel.objects.filter(id=pk).first()

    if request.method == "POST":
        form = ListForm({
            'name': request.POST['name'],
            'user': request.user
        }, instance=list_)
        success_url = reverse('main:main')
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = ListForm(instance=list_)
    return render(request, "edit_list.html", {'form': form})


@login_required(login_url='registration/login/')
def delete_view(request, pk):
    if request.method == 'POST':
        list_ = ListModel.objects.filter(id=pk).first()
        if list_:
            list_.delete()
            return HttpResponse(status=201)
    return HttpResponse(status=404)


@login_required(login_url='registration/login/')
def create_view(request):
    """view создания нового списка"""
    form = ListForm()
    if request.method == 'POST':
        name = request.POST['name']

        form = ListForm({
            'name': name,
            'user': request.user
        })
        success_url = reverse('main:main')
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, 'new_list.html', {'form': form})
