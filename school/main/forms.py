from .models import News
from django.forms import ModelForm, Textarea, TextInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }