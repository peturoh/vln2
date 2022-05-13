
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
    profile_data = Profile.objects.filter(user=request.user).first()
    return render(request, 'user/profile.html', {
        'form': profile_data
    })

def edit_profile(request):
    # instance = get_object_or_404(User, id=request.user.id)
    # user = User.objects.get(id=request.user.id)
    # if request.method == 'POST':
    #     form = ProfileForm(data=request.POST)
    #     if form.is_valid():
    #         profile_bio = form.cleaned_data.get('profile_bio')
    #         user.profile_bio = profile_bio
    #         user.save()
    #         profile_image = form.cleaned_data.get('profile_image')
    #         user.profile_image = profile_image
    #         user.save()
    #         return redirect('profile')
    #     else:
    #         print("nonono")
    #         print(form.errors)
    #         form = ProfileForm(instance=instance)
    #     return render(request, 'user/edit_profile.html', {
    #          'form': form,
    #          'id': id
    #      })

    profile_data = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile_data, data=request.POST)
        form.user = request.user
        print(form.user)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = request.user
            profile_data.save()
            return redirect('profile')
        else:
            print("nonono")
            print(form.errors)
            print(request.user)
    else:
        form = ProfileForm(instance=profile_data, data=request.POST)
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile_data)
    })





