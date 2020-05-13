from django.db import models


# Create your models here.
class Listitem(models.Model):
    """ Модель элемента списка """
    name = models.CharField(max_length=128, verbose_name='Название задачи')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    list = models.ForeignKey('main.ListModel', on_delete=models.CASCADE, verbose_name='Список дел')
    is_done = models.BooleanField(default=False)
    expire_date = models.DateField(blank=True, null=True)
    priority = models.SmallIntegerField(verbose_name='Приоритет', default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        list_ = self.list
        if all(list_.listitem_set.all().values_list('is_done', flat=True)):
            # получаем одной строкой список всех значений is_done выбранного списка
            list_.is_done = True
            list_.save()
            # Если один из пунктов списка снова стало невыполненным, нужно сделать is_done у списка снова False
        else:
            if list_.is_done:
                list_.is_done = False
                list_.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент списка'
        unique_together = ('name', 'list', 'expire_date')
