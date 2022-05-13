from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'avg_rating']
        widgets = {
            'profile_image': widgets.Textarea(attrs={'class': 'form-control'}),
            'profile_bio': widgets.Textarea(attrs={'class': 'form control'})
        }

