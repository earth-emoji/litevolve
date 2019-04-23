from django import forms
from tinymce.widgets import TinyMCE

from .models import World

class WorldForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(attrs={'class': 'form-control rounded-0'}))
    overview = forms.CharField(widget=TinyMCE(attrs={'class': 'description', 'cols': 80, 'rows': 15}))

    class Meta:
        model = World
        fields = ['name', 'overview']