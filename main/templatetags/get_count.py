from django.template.defaulttags import register
from ToDoList.settings import DIV_COUNT


@register.filter
def get_count(lists):
    """
    Возвращает список - количество для генерации пустых блоков
    """

    return list(range(DIV_COUNT - len(lists)))
