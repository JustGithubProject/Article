from django.forms import ModelForm, TextInput, Textarea
from .models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name', 'text']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название",
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание",
            }),
        }


