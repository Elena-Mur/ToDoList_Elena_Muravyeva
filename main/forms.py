from django import forms

from main.models import ListModel
from django.core.exceptions import NON_FIELD_ERRORS


class ListForm(forms.ModelForm):
    """
    Форма натсроек расписания обмена
    """
    name = forms.CharField(required=True, widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
        error_messages = {
            NON_FIELD_ERRORS:{
                'unique_together': 'Введите другое имя...',

            }
        }

