from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'avg_rating']
        widgets = {
            'profile_user': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'size': '40'}),
            'profile_bio': widgets.Textarea(attrs={'size': '50'})
        }

