from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from user.models import Profile
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})



def profile(request):
    profile_data = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/profile.html', {
        'form': profile_data
    })

def edit_profile(request):
    profile_data = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile_data, data=request.POST)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = request.user
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile_data, data=request.POST)
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile_data)
    })





