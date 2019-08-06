'''
Created on Jul 30, 2019

@author: franklincarrilho
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from fcsSimpleMooc.core.mail import send_mail_template
from fcsSimpleMooc.core.utils import generate_hash_key

from .models import PasswordReset

User = get_user_model()


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label = 'E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            return email
        raise forms.ValidationError('Sorry! No User found for the informed e-mail!')

    def save(self):
        user = User.objects.get(email = self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key = key, user = user)
        reset.save()
        #
        template_name = 'accounts/password_reset_mail.html'
        subject = 'Create new password'
        context = {'reset': reset,}
        #
        send_mail_template(subject, template_name, context, [user.email])


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Sorry! Passwords don't match")
        return password2

    def save(self, commit = True):
        user = super(RegisterForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
##########                  END                ###########