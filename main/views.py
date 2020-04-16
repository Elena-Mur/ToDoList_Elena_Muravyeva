from django.shortcuts import render

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#  user = User('Bob',23)
data = {
    'lists': [
        {'name': 'Работа', 'is_done': True},
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учеба', 'is_done': True}
    ],
    'user_name': 'admin'
}


# Create your views here.
def main_view(request):
    context = data
    return render(request, 'index.html', context)
