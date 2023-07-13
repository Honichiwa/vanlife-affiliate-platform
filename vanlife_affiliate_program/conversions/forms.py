from django import forms
from . import models
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

class GadgetForm(forms.ModelForm):
    type = forms.ModelChoiceField(models.GadgetType.objects.all(), widget=forms.RadioSelect())
    class Meta:
        model = models.Gadget
        fields = ('type', 'name', 'picture', 'aff_link', 'conversion')
        widgets = {
            'conversion': forms.HiddenInput(),
        }


class ConversionSocialForm(forms.ModelForm):
    class Meta:
        model = models.ConversionSocial
        fields = ('conversion', 'social', 'link', 'social_username')