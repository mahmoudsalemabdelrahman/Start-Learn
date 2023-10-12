from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.


def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()  
    return render(request,'registration/signup.html', {'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit = False)
            myprofile.user =request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))



    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform':userform, 'profileform':profileform})








def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'accounts/login.html', context={'form': form, 'message': message})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('blog:blog_home')
    else:
        return redirect('login')
    
    return render(request,'registration/logged_out.html')

    

