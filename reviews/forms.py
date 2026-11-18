from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    device_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Review
        fields = ['author_name', 'text', 'rating']
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
