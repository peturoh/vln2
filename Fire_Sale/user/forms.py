from django.forms import ModelForm, widgets
from user.models import Profile
from django import forms


class EditProfileForm(ModelForm):
    name: forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Profile
        exclude = ['id', 'avg_rating']
        widgets = {
            'profile_bio': widgets.Textarea(attrs={ 'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' })
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'avg_rating', 'profile_image']
        widgets = {
            'profile_user': widgets.Textarea(attrs={'class': 'form-control'}),
            'profile_bio': widgets.Textarea(attrs={'size': '50'})
        }
