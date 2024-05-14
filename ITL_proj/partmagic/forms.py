from django import forms
from .models import Pubs

class PubsForm(forms.ModelForm):
    class Meta:
        model = Pubs
        fields = ['auth', 'pub_title', 'topic', 'pub_date']
