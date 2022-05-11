from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'avg_rating', 'profile_image']
        widgets = {
            'profile_user': widgets.Textarea(attrs={'class': 'form-control'}),
            'profile_bio': widgets.Textarea(attrs={'size': '50'})
        }

