'''

Views for Accounts

    . dashboard
    . register
    . password_reset
    . password_reset_confirm
    . edit
    . edit_password
    . logout_request

'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
#
from fcsSimpleMooc.core.utils import generate_hash_key
from fcsSimpleMooc.courses.models import Enrollment
#
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {"dashboard_page": "active"}
#     context['enrollments'] = Enrollment.object.filter(user = request.user)
    return render(request, template_name, context)

def register(request):
    #
    MESSAGE_SUCCESS = 'Success! Your registration was processed!'
    template_name = 'accounts/register.html'
    
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            
            user = form.save()
            user = authenticate(username = user.username, password = form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, MESSAGE_SUCCESS) # new
            
            return redirect('core:home')
    else:
        
        form = RegisterForm()
    
    context = {'form': form}
    
    return render(request, template_name, context)

def password_reset(request):
    #
    MESSAGE_SUCCESS = 'Success! Your password was changed!'
    #
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    
    if form.is_valid():
        
        form.save()
        messages.success(request, MESSAGE_SUCCESS) # new
        context['success'] = True
    
    context['form'] = form
    
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    #
    MESSAGE_SUCCESS = 'Success! Your password was changed!'
    #
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key = key)
    form = SetPasswordForm(user = reset.user, data = request.POST or None)
    
    if form.is_valid():
        
        form.save()
        messages.success(request, MESSAGE_SUCCESS) # new
        context['success'] = True
    
    context['form'] = form
    
    return render(request, template_name, context)

@login_required
def edit(request):
    #
    MESSAGE_SUCCESS = 'Success! Your information were updated!'
    #
    template_name = 'accounts/edit.html'
    context = {}
    
    if request.method == 'POST':
        
        form = EditAccountForm(request.POST, instance = request.user)
        
        if form.is_valid():
            
            form.save()
            messages.success(request, MESSAGE_SUCCESS) # new
            
            return redirect('accounts:dashboard') # new
#             form = EditAccountForm(instance=request.user)
#             context['success'] = True

    else:
        
        form = EditAccountForm(instance = request.user)
    
    context['form'] = form
    
    return render(request, template_name, context)

@login_required
def edit_password(request):
    #
    MESSAGE_SUCCESS = 'Success! Your password was updated!'
    #
    template_name = 'accounts/edit_password.html'
    context = {}
    
    if request.method == 'POST':
        
        form = PasswordChangeForm(data = request.POST, user = request.user)
        
        if form.is_valid():
            
            form.save()
            messages.success(request, MESSAGE_SUCCESS) # new
            context['success'] = True
    else:
        
        form = PasswordChangeForm(user = request.user)
    
    context['form'] = form
    
    return render(request, template_name, context)

@login_required
def logout_request(request):
    
    logout(request)
    
    return redirect("core:home")
##########                  END                ###########