from django import forms
from .models import ProviderProfile

class ProviderProfileForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ['skills', 'experience_years', 'bio']