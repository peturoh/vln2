from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from user.models import Profile

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
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


def editprofile(request):
    editprofile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=editprofile, data=request.POST)
        if form.is_valid():
            editprofile = form.save(commit=False)
            editprofile.user = request.user
            profile.save()
            return redirect('profile')
        return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=profile)
        })