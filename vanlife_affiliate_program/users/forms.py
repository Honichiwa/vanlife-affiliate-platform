from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import ProfileIcon


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    icon = forms.ModelChoiceField(ProfileIcon.objects.all(), widget=forms.RadioSelect())

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'icon', 'about_you', 'reason']