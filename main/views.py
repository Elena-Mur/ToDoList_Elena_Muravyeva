from django.shortcuts import render

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#  user = User('Bob',23)
data = {
    'lists': [
        {'id': 1, 'name': 'Позвонить', 'is_done': True},
        {'id': 2, 'name': 'Написать', 'is_done': False},
        {'id': 3, 'name': 'Заказать', 'is_done': True},
        {'id': 4, 'name': 'Сделать', 'is_done': False},

    ],
    'user_name': 'admin'
}


# Create your views here.
def main_view(request):
    context = data
    return render(request, 'index.html', context)


def edit_view(request, pk):
    pass
