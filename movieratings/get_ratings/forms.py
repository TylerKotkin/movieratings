from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    movie_review = forms.CharField(label='Movie Review', max_length=500)

    class Meta:
        model = Rating
        fields = ('stars',)
