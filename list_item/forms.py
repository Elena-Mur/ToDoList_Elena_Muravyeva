from django import forms

from list_item.models import Listitem
from django.core.exceptions import NON_FIELD_ERRORS


class ListitemForm(forms.ModelForm):
    """
    Форма натсроек расписания обмена
    """
    name = forms.CharField(required=True, widget=forms.TextInput())
    expire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Listitem
        fields = ('name', 'expire_date', 'list')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'Введите другое имя...',

            }
        }
