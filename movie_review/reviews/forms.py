from django import forms
from .models import Review
import re

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        # Проверка, содержит ли текст только английские буквы и пробелы
        if not re.match(r'^[A-Za-z\s]+$', text):
            raise forms.ValidationError('Вводить можно только текст на английском языке.')
        return text