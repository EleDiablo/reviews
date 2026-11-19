import re
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    device_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Review
        fields = ['author_name', 'text', 'rating']

        def clean_device_id(self):
            dev_id = self.cleaned_data.get('device_id', '')
            # Разрешаем только корректный UUID или наш резервный формат dev-...
            pattern = (r'^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}'
                       r'-[0-9a-f]{12}|dev-[a-z0-9]{15,35})$')
            if not re.match(pattern, dev_id):
                raise forms.ValidationError('Некорректный идентификатор\
                                            устройства.')
            return dev_id
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Иван'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control',
                                               'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'rows': 4,
                                          'placeholder': 'Поделитесь \
                                            впечатлениями...'})
        }
