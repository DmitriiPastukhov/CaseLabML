import re
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        # Проверка: английские буквы, пробелы и знаки препинания (, . ! ? ' " - :)
        if not re.match(r'^[A-Za-z\s.,!?\'"()\-:]+$', text):
            raise forms.ValidationError('Можно вводить только текст на английском языке, включая знаки препинания.')
        return text