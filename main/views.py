from django.shortcuts import render, reverse, redirect
from main.forms import ListModel, ListForm


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
