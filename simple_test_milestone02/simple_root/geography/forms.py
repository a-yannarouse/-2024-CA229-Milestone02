# geography/forms.py

from django import forms
from .models import Attraction

class AttractionImageForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ['image']
