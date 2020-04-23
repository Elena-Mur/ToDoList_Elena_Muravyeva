from django.shortcuts import render, reverse, redirect

data = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True, 'date': '04.06.20'},
        {'name': 'Заказать торт', 'is_done': False, 'date': '05.06.20'},
        {'name': 'Разослать приглашения', 'is_done': True}
    ],
    'user_name': 'admin'
}


# Create your views here.
def list_item_view(request,pk):
    context = data
    return render(request, 'list.html', context)
