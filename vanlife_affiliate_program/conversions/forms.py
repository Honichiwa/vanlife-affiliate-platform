from django import forms
from . import models
from .models import Conversion
from django.contrib.auth import get_user_model

class ConversionForm(forms.ModelForm):
    class Meta:
        model = models.Conversion
        fields = ('make', 'model', 'year', 'conversion_slug', 
                  'side_picture', 'veichle_cost', 'conversion_cost',
                  'summary', 'interior1', 'interior2', 'interior3',
                  'interior4', 'outro', 'visible', 'owner',
                  'c_type'
                  )
        widgets = {
            'owner': forms.HiddenInput(),
            'c_type': forms.HiddenInput(),
        }